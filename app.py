import requests
from bs4 import BeautifulSoup
import json
import html
import sys
import pyodbc

def scrape_table_data():
    try:
        # URLs
        login_page_url = "https://c4api.care4all.dk/login"
        login_url = "https://c4api.care4all.dk/login"
        data_url = "https://c4api.care4all.dk/units"
        
        # User credentials
        username = "gsgroup-service@bhslogistics.dk"
        password = "CHSC6ZFM"
        
        # Create a session
        session = requests.Session()
        
        # Headers to mimic a browser
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Referer": login_page_url
        }

        # Step 1: Get the login page
        response = session.get(login_page_url, headers=headers)
        response.encoding = "utf-8"  # Ensure correct encoding
        if response.status_code != 200:
            return {"error": f"Failed to load login page: {response.status_code}"}

        # Parse the login page to extract CSRF token
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find("input", {"name": "csrf"})["value"]
        if not csrf_token:
            return {"error": "CSRF token not found in the login page."}

        # Step 2: Log in with credentials
        credentials = {
            "username": username,
            "password": password,
            "csrf": csrf_token
        }
        
        login_response = session.post(login_url, data=credentials, headers=headers)
        if login_response.status_code != 200:
            return {"error": "Login failed. Please check your credentials or CSRF handling."}

        # Step 3: Access the data page
        data_response = session.get(data_url, headers=headers)
        data_response.encoding = "utf-8"  # Ensure correct encoding
        if data_response.status_code != 200:
            return {"error": f"Failed to access data page: {data_response.status_code}"}

        # Parse the table data
        soup = BeautifulSoup(data_response.text, "html.parser")
        table = soup.find("table")
        if not table:
            return {"error": "No table found on the page."}

        # Extract table data while preserving cell contents
        table_data = []
        rows = table.find("tbody").find_all("tr")
        for row in rows:
            # Get each cell's complete content, regardless of commas
            cells = row.find_all("td")
            row_data = [html.unescape(cell.text.strip()) for cell in cells]
            
            # Ensure we have exactly 10 columns (adding NULL if needed)
            while len(row_data) < 10:
                row_data.append("NULL")
                
            # Convert empty strings to NULL
            row_data = ["NULL" if not cell else cell for cell in row_data]
            
            table_data.append(row_data)
            
        return {"Table Data": table_data}
    except Exception as e:
        return {"error": str(e)}

def insert_into_database(table_data):
    server = 'bhs-sql2'
    database = 'Gsgroup_backup'
    trusted_connection = 'yes'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        for row in table_data:
            # Extract values (now we know we have exactly 10 elements)
            id = row[0]
            number = row[1]
            sequence = row[2]
            name = row[3]
            description = row[4]
            guid = row[5]
            model = row[6]
            locale = row[7]
            subscription = row[8]
            timezone = row[9]
            
            # SQL insert statement
            sql = """
            INSERT INTO Gsgroup_backup.dbo.units
            (ID, Number, Sequence, Name, Description, GUID, Model, Locale, Subscription, Timezone)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            ordered_values = [id, number, sequence, name, description, guid, model, 
                            locale, subscription, timezone]
            
            try:
                cursor.execute(sql, ordered_values)
                conn.commit()
                print(f"Successfully inserted row with ID: {id}")
            except pyodbc.Error as row_error:
                print(f"Error inserting row: {str(row_error)}")
                print(f"Problematic values: {ordered_values}")
                conn.rollback()
                continue

        cursor.close()
        conn.close()
        return True
    except pyodbc.Error as e:
        print(f"Database Error: {str(e)}")
        return False

def list_databases():
    """
    Lists all databases available on the SQL Server instance.
    Returns:
        A list of database names.
    """
    server = 'bhs-sql2'
    database = 'Gsgroup_backup'
    trusted_connection = 'yes'
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    
    try:
        conn = pyodbc.connect(connection_string)
        print("Connection successful!")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.databases")
        databases = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return databases
    except pyodbc.Error as e:
        print(f"Error: {e}")
        return []

def main(args):
    # Scrape data
    data = scrape_table_data()
    
    if "error" in data:
        print("Error scraping data:", data["error"])
        return

    if "Table Data" in data:
        success = insert_into_database(data["Table Data"])
        if success:
            print("Data successfully inserted into database")
        else:
            print("Failed to insert data into database")

if __name__ == '__main__':
    main(sys.argv)
