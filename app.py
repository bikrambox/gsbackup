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

        # Extract table data with proper NULL handling
        table_data = []
        # rows = table.find("tbody").find_all("tr")
        # for row in rows:
        #     cells = row.find_all("td")
        #     row_data = []
        #     for cell in cells:
        #         value = html.unescape(cell.text.strip())
        #         row_data.append("NULL" if value == "" else value)
        #     table_data.append(", ".join(row_data))
        table_data = ["g6r4f6fc-c8ef-4e4d-97f1-291c4f18a9d3, 1128000993, 1, FD 3971 Afd101 K°l Ophµng, Trailer, 1EtqEOAXuHuWEV00000000, 7A2, da_DK, 4, NULL",
        "98a5fb2a-728f-44e5-839f-16e44c4e6ff4, 1128001343, 1, CU 93 552 Afd105 Kran, Vehicle, 3RjFWcAZmHuWIV00000000, 7A2, da_DK, 4, NULL",
        "5b815c19-41ca-4c37-a2fa-b697e458bab0, 1129000173, 3, CP 5647 Afd101 K°l SideÕbner, Trailer, 0LVtt4AhyHuWMV00000000, 7A2, da_DK, 4, NULL",
        "f64132cf-ee95-44a7-aa6b-1bd69b90d7fb, 1129000183, 2, FD 1644 Afd101 K°l Ophµng, Trailer, 2m4_$SAhyHuWMV00000000, 7A2, da_DK, 4, NULL"]

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
            # Split the row string into individual values
            values = row.split(", ")
            
            # Process values for insertion
            processed_values = []
            for i, v in enumerate(values):
                if i == 3:  # Name column (non-nullable)
                    processed_values.append(v if v != "NULL" else "")
                else:
                    processed_values.append(None if v == "NULL" else v)
            
            # Reorder values to match the table structure (GUID, Number, Sequence, etc.)
            id = processed_values[0]
            number = processed_values[1]
            sequence = processed_values[2]
            name = processed_values[3]
            description = processed_values[4]
            guid = processed_values[5]
            model = processed_values[6]
            locale = processed_values[7]
            subscription = processed_values[8]
            timezone = processed_values[9] if len(processed_values) > 9 else None
            
            # SQL insert statement with correct column order
            sql = """
            INSERT INTO Gsgroup_backup.dbo.units 
            (ID, Number, Sequence, Name, Description, GUID, Model, Locale, Subscription, Timezone)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            ordered_values = [id, number, sequence, name, description, guid,  model, 
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
    
    # Insert data into database
    if "Table Data" in data:
        success = insert_into_database(data["Table Data"])
        if success:
            print("Data successfully inserted into database")
        else:
            print("Failed to insert data into database")
    
    # # Print the scraped data
    # print(json.dumps(data, indent=4, ensure_ascii=False))
    
    # # List available databases
    # databases = list_databases()
    # if databases:
    #     print("\nAvailable databases:")
    #     for db in databases:
    #         print(db)
    # else:
    #     print("\nNo databases found.")

if __name__ == '__main__':
    main(sys.argv)
