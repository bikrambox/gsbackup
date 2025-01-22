# # import requests
# # from bs4 import BeautifulSoup
# # import json
# # import html
# # import sys
# # import pyodbc



# # def scrape_table_data():
# #     try:
# #         # URLs
# #         login_page_url = "https://c4api.care4all.dk/login"
# #         login_url = "https://c4api.care4all.dk/login"
# #         data_url = "https://c4api.care4all.dk/units"

# #         # User credentials
# #         username = "gsgroup-service@bhslogistics.dk"
# #         password = "CHSC6ZFM"

# #         # Create a session
# #         session = requests.Session()

# #         # Headers to mimic a browser
# #         headers = {
# #             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# #             "Referer": login_page_url
# #         }

# #         # Step 1: Get the login page
# #         response = session.get(login_page_url, headers=headers)
# #         response.encoding = "utf-8"  # Ensure correct encoding
# #         if response.status_code != 200:
# #             return {"error": f"Failed to load login page: {response.status_code}"}

# #         # Parse the login page to extract CSRF token
# #         soup = BeautifulSoup(response.text, "html.parser")
# #         csrf_token = soup.find("input", {"name": "csrf"})["value"]
# #         if not csrf_token:
# #             return {"error": "CSRF token not found in the login page."}

# #         # Step 2: Log in with credentials
# #         credentials = {
# #             "username": username,
# #             "password": password,
# #             "csrf": csrf_token
# #         }

# #         login_response = session.post(login_url, data=credentials, headers=headers)
# #         if login_response.status_code != 200:
# #             return {"error": "Login failed. Please check your credentials or CSRF handling."}

# #         # Step 3: Access the data page
# #         data_response = session.get(data_url, headers=headers)
# #         data_response.encoding = "utf-8"  # Ensure correct encoding
# #         if data_response.status_code != 200:
# #             return {"error": f"Failed to access data page: {data_response.status_code}"}

# #         # Parse the table data
# #         soup = BeautifulSoup(data_response.text, "html.parser")
# #         table = soup.find("table")
# #         if not table:
# #             return {"error": "No table found on the page."}

# #         # Extract table data
# #         table_data = []
# #         rows = table.find("tbody").find_all("tr")
# #         for row in rows:
# #             cells = row.find_all("td")
# #             row_data = [html.unescape(cell.text.strip()) for cell in cells]  # Decode HTML entities
# #             table_data.append(", ".join(row_data))

# #         return {"Table Data": table_data}

# #     except Exception as e:
# #         return {"error": str(e)}


# # def list_databases():
# #   """
# #   Lists all databases available on the SQL Server instance.

# #   Returns:
# #     A list of database names.
# #   """

# #   # Detailed connection parameters
# #   # server = '10.0.0.33'
# #   server = 'bhs-sql2'
# #   database = 'Gsgroup_backup'
# #   username = 'bulkattain_reader'
# #   password = 'Efteraar2023!'
# #   trusted_connection = 'yes'  # Windows authentication
# #   port = '1433'  # Default SQL Server port

# #   connection_string =f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
    
# #   try:
# #     conn = pyodbc.connect(connection_string)
# #     print("Connection successful!")
# #     cursor = conn.cursor()

# #     cursor.execute("SELECT name FROM sys.databases")
# #     databases = [row[0] for row in cursor.fetchall()]

# #     cursor.close()
# #     conn.close()

# #     return databases

# #   except pyodbc.Error as e:
# #     print(f"Error: {e}")
# #     return []


# # def main(args):
# #     data = scrape_table_data()
# #     print(json.dumps(data, indent=4, ensure_ascii=False))  # ensure_ascii=False for proper character rendering
    
    
# #     databases = list_databases()

# #     if databases:
# #       print("Available databases:")
# #       for db in databases:
# #           print(db)
# #     else:
# #       print("No databases found.")



# # if __name__ == '__main__':
# #     main(sys.argv)











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
    """
    Scrapes table data from the specified URL.

    Returns:
        dict: A dictionary containing the scraped table data.
    """
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
            return {"error": f"Failed to access data page: {response.status_code}"}

        # Parse the table data
        soup = BeautifulSoup(data_response.text, "html.parser")
        table = soup.find("table")

        if not table:
            return {"error": "No table found on the page."}

        # Extract table data
        table_data = []
        rows = table.find("tbody").find_all("tr")

        for row in rows:
            cells = row.find_all("td")
            row_data = [html.unescape(cell.text.strip()) for cell in cells]  # Decode HTML entities
            table_data.append(row_data)

        return {"Table Data": table_data}

    except Exception as e:
        return {"error": str(e)}

def list_databases():
    """
    Lists all databases available on the SQL Server instance.

    Returns:
        A list of database names.
    """
    # Detailed connection parameters
    server = 'bhs-sql2'  # Replace with your server name
    database = 'Gsgroup_backup'
    username = 'bulkattain_reader'
    password = 'Efteraar2023!'
    trusted_connection = 'yes'  # Windows authentication
    port = '1433'  # Default SQL Server port

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

def insert_data(data_row):
    """
    Inserts a data row into the specified table.

    Args:
        data_row (list): A list containing the values to be inserted into the table columns.

    Returns:
        dict: A dictionary with a message indicating success or failure.
    """
    # Detailed connection parameters
    server = 'bhs-sql2'  # Replace with your server name
    database = 'Gsgroup_backup'
    username = 'bulkattain_reader'
    password = 'Efteraar2023!'
    trusted_connection = 'yes'  # Windows authentication
    port = '1433'  # Default SQL Server port

    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        columns = ["ID", "Name", "Number", "Sequence", "Description", "GUID", "Model", "Locale", "Subscription", "Timezone"]
        placeholders = ", ".join(["?"] * len(columns))
        insert_stmt = f"INSERT INTO [dbo].[units01] ({columns}) VALUES ({placeholders})"

        # Handle empty data and convert to NULL
        cleaned_data_row = []
        for value in data_row:
            if value.strip() == "":
                cleaned_data_row.append(None)
            else:
                cleaned_data_row.append(value)

        cursor.execute(insert_stmt, cleaned_data_row)
        conn.commit()
        return {"message": "Data inserted successfully!"}

    except pyodbc.Error as e:
        print(f"Error inserting data: {e}")
        return {"error": str(e)}

    finally:
        if conn:
            conn.close()

def main(args):
    data = scrape_table_data()

    if "error" in data:
        print(f"Error: {data['error']}")
    else:
        for row in data["Table Data"]:
            insert_result = insert_data(row)
            print(insert_result)

    # ... (code to list databases can be removed if not needed)

if __name__ == '__main__':
    main(sys.argv)
