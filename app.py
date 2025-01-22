# import requests
# from bs4 import BeautifulSoup
# import json
# import html
# import sys
# import pyodbc



# def scrape_table_data():
#     try:
#         # URLs
#         login_page_url = "https://c4api.care4all.dk/login"
#         login_url = "https://c4api.care4all.dk/login"
#         data_url = "https://c4api.care4all.dk/units"

#         # User credentials
#         username = "gsgroup-service@bhslogistics.dk"
#         password = "CHSC6ZFM"

#         # Create a session
#         session = requests.Session()

#         # Headers to mimic a browser
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#             "Referer": login_page_url
#         }

#         # Step 1: Get the login page
#         response = session.get(login_page_url, headers=headers)
#         response.encoding = "utf-8"  # Ensure correct encoding
#         if response.status_code != 200:
#             return {"error": f"Failed to load login page: {response.status_code}"}

#         # Parse the login page to extract CSRF token
#         soup = BeautifulSoup(response.text, "html.parser")
#         csrf_token = soup.find("input", {"name": "csrf"})["value"]
#         if not csrf_token:
#             return {"error": "CSRF token not found in the login page."}

#         # Step 2: Log in with credentials
#         credentials = {
#             "username": username,
#             "password": password,
#             "csrf": csrf_token
#         }

#         login_response = session.post(login_url, data=credentials, headers=headers)
#         if login_response.status_code != 200:
#             return {"error": "Login failed. Please check your credentials or CSRF handling."}

#         # Step 3: Access the data page
#         data_response = session.get(data_url, headers=headers)
#         data_response.encoding = "utf-8"  # Ensure correct encoding
#         if data_response.status_code != 200:
#             return {"error": f"Failed to access data page: {data_response.status_code}"}

#         # Parse the table data
#         soup = BeautifulSoup(data_response.text, "html.parser")
#         table = soup.find("table")
#         if not table:
#             return {"error": "No table found on the page."}

#         # Extract table data
#         table_data = []
#         rows = table.find("tbody").find_all("tr")
#         for row in rows:
#             cells = row.find_all("td")
#             row_data = [html.unescape(cell.text.strip()) for cell in cells]  # Decode HTML entities
#             table_data.append(", ".join(row_data))

#         return {"Table Data": table_data}

#     except Exception as e:
#         return {"error": str(e)}


# def list_databases():
#   """
#   Lists all databases available on the SQL Server instance.

#   Returns:
#     A list of database names.
#   """

#   # Detailed connection parameters
#   # server = '10.0.0.33'
#   server = 'bhs-sql2'
#   database = 'Gsgroup_backup'
#   username = 'bulkattain_reader'
#   password = 'Efteraar2023!'
#   trusted_connection = 'yes'  # Windows authentication
#   port = '1433'  # Default SQL Server port

#   connection_string =f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    
#   try:
#     conn = pyodbc.connect(connection_string)
#     print("Connection successful!")
#     cursor = conn.cursor()

#     cursor.execute("SELECT name FROM sys.databases")
#     databases = [row[0] for row in cursor.fetchall()]

#     cursor.close()
#     conn.close()

#     return databases

#   except pyodbc.Error as e:
#     print(f"Error: {e}")
#     return []


# def main(args):
#     data = scrape_table_data()
#     print(json.dumps(data, indent=4, ensure_ascii=False))  # ensure_ascii=False for proper character rendering
    
    
#     databases = list_databases()

#     if databases:
#       print("Available databases:")
#       for db in databases:
#           print(db)
#     else:
#       print("No databases found.")



# if __name__ == '__main__':
#     main(sys.argv)











# import requests
# from bs4 import BeautifulSoup
# import json
# import html
# import sys
# import pyodbc

# def scrape_table_data():
#     try:
#         # URLs
#         login_page_url = "https://c4api.care4all.dk/login"
#         login_url = "https://c4api.care4all.dk/login"
#         data_url = "https://c4api.care4all.dk/units"

#         # User credentials
#         username = "gsgroup-service@bhslogistics.dk"
#         password = "CHSC6ZFM"

#         # Create a session
#         session = requests.Session()

#         # Headers to mimic a browser
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#             "Referer": login_page_url
#         }

#         # Step 1: Get the login page
#         response = session.get(login_page_url, headers=headers)
#         response.encoding = "utf-8"  # Ensure correct encoding
#         if response.status_code != 200:
#             return {"error": f"Failed to load login page: {response.status_code}"}

#         # Parse the login page to extract CSRF token
#         soup = BeautifulSoup(response.text, "html.parser")
#         csrf_token = soup.find("input", {"name": "csrf"})["value"]
#         if not csrf_token:
#             return {"error": "CSRF token not found in the login page."}

#         # Step 2: Log in with credentials
#         credentials = {
#             "username": username,
#             "password": password,
#             "csrf": csrf_token
#         }

#         login_response = session.post(login_url, data=credentials, headers=headers)
#         if login_response.status_code != 200:
#             return {"error": "Login failed. Please check your credentials or CSRF handling."}

#         # Step 3: Access the data page
#         data_response = session.get(data_url, headers=headers)
#         data_response.encoding = "utf-8"  # Ensure correct encoding
#         if data_response.status_code != 200:
#             return {"error": f"Failed to access data page: {data_response.status_code}"}

#         # Parse the table data
#         soup = BeautifulSoup(data_response.text, "html.parser")
#         table = soup.find("table")
#         if not table:
#             return {"error": "No table found on the page."}

#         # Extract table data
#         table_data = []
#         rows = table.find("tbody").find_all("tr")
#         for row in rows:
#             cells = row.find_all("td")
#             row_data = [html.unescape(cell.text.strip()) for cell in cells]  # Decode HTML entities
#             table_data.append(", ".join(row_data))

#         return {"Table Data": table_data}

#     except Exception as e:
#         return {"error": str(e)}


# def list_databases():
#   """
#   Lists all databases available on the SQL Server instance.

#   Returns:
#     A list of database names.
#   """

#   # Detailed connection parameters
#   # server = '10.0.0.33'
#   server = 'bhs-sql2'
#   database = 'Gsgroup_backup'
#   username = 'bulkattain_reader'
#   password = 'Efteraar2023!'
#   trusted_connection = 'yes'  # Windows authentication
#   port = '1433'  # Default SQL Server port

#   connection_string =f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    
#   try:
#     conn = pyodbc.connect(connection_string)
#     print("Connection successful!")
#     cursor = conn.cursor()

#     cursor.execute("SELECT name FROM sys.databases")
#     databases = [row[0] for row in cursor.fetchall()]

#     cursor.close()
#     conn.close()

#     return databases

#   except pyodbc.Error as e:
#     print(f"Error: {e}")
#     return []

# def insert_data(data_row):
#   """
#   Inserts a data row into the specified table.

#   Args:
#       data_row (list): A list containing the values to be inserted into the table columns.

#   Returns:
#       dict: A dictionary with a message indicating success or failure.
#   """
#   # Detailed connection parameters
#   server = 'bhs-sql2'
#   database = 'Gsgroup_backup'
#   username = 'bulkattain_reader'
#   password = 'Efteraar2023!'
#   trusted_connection = 'yes'  # Windows authentication
#   port = '1433'  # Default SQL Server port

#   connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

#   try:
#     conn = pyodbc.connect(connection_string)
#     cursor = conn.cursor()

#     # Construct the INSERT statement with placeholders for values
#     columns = ", ".join(["ID", "Name", "Number", "Sequence", "Description", "GUID", "Model", "Locale", "Subscription", "Timezone"])
#     placeholders = ", ".join(["?"] * len(data_row))
#     insert_stmt = f"INSERT INTO [dbo].[units01] ({columns}) VALUES ({placeholders})"

#     # Execute the insert statement with the data row values
#     cursor.execute(insert_stmt, data_row)
#     conn.commit()

#     return {"message": "Data inserted successfully!"}

#   except pyodbc.Error as e:
#     print(f"Error inserting data: {e}")
#     return {"error": str(e)}

#   finally:
#     if conn:
#       conn.close()

# def main(args):
#     data = scrape_table_data()
#     print(json.dumps(data, indent=4, ensure_ascii=False))  # ensure_ascii=False for proper character rendering
    
    
#     databases = list_databases()

#     if databases:
#       print("Available databases:")
#       for db in databases:
#           print(db)
#     else:
#       print("No databases found.")


#     # Example data row (replace with actual data from scraping or user input)
#     data_row = [
#         "3ecc948b-0c87-48f6-ab22-a6b83dd899da",
#         "2328001283",
#         0,
#         "ED 27 618 afd410 Van Pharma",
#         "",
#         "43cf4184-a469-4091-9793-a366aec94693",
#         "7L2-D",
#         "da_DK",
#         4,
#         "Europe/Copenhagen"
#     ]

#     # Insert the data into the table
#     insert_result = insert_data(data_row)
#     print(json.dumps(insert_result, indent=4))

    

# if __name__ == '__main__':
#     main(sys.argv)





    
    
    
    
    
    
    
    
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
        rows = table.find("tbody").find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            row_data = []
            for cell in cells:
                value = html.unescape(cell.text.strip())
                row_data.append("NULL" if value == "" else value)
            table_data.append(", ".join(row_data))

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
            guid = processed_values[0]
            number = processed_values[1]
            sequence = processed_values[2]
            name = processed_values[3]
            description = processed_values[4]
            model = processed_values[5]
            locale = processed_values[6]
            subscription = processed_values[7]
            timezone = processed_values[8] if len(processed_values) > 8 else None
            
            # SQL insert statement with correct column order
            sql = """
            INSERT INTO Gsgroup_backup.dbo.units01 
            (GUID, Number, Sequence, Name, Description, Model, Locale, Subscription, Timezone)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            
            ordered_values = [guid, number, sequence, name, description, model, 
                            locale, subscription, timezone]
            
            try:
                cursor.execute(sql, ordered_values)
                conn.commit()
                print(f"Successfully inserted row with GUID: {guid}")
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
    
    # Print the scraped data
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
    # List available databases
    databases = list_databases()
    if databases:
        print("\nAvailable databases:")
        for db in databases:
            print(db)
    else:
        print("\nNo databases found.")

if __name__ == '__main__':
    main(sys.argv)  
    
    
    
    
    
    
    
    
