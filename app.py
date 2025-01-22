import pyodbc

def list_databases():
  """
  Lists all databases available on the SQL Server instance.

  Returns:
    A list of database names.
  """

  # Detailed connection parameters
  # server = '10.0.0.33'
  server = 'bhs-sql2'
  database = 'Gsgroup_backup'
  username = 'bulkattain_reader'
  password = 'Efteraar2023!'
  trusted_connection = 'yes'  # Windows authentication
  port = '1433'  # Default SQL Server port

  connection_string =f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'
  
  # connection_string = f"""
  # DRIVER={{ODBC Driver 18 for SQL Server}};
  # SERVER={server},{port};
  # DATABASE={database};
  # UID={username};
  # PWD={password};
  # Encrypt=yes;
  # Trusted_Connection={trusted_connection};
  # TrustServerCertificate=yes;
  # Connection Timeout=60;
  # Login Timeout=60;
  # """



  # try:
  #     conn = pyodbc.connect(connection_string)
  #     print("Connection successful!")

  #     cursor = conn.cursor()
  #     cursor.execute("SELECT name FROM sys.databases")
  #     rows = cursor.fetchall()

  #     print("List of databases:")
  #     for row in rows:
  #         print(row[0]) 

  # except pyodbc.Error as ex:
  #     print("Connection error:", ex)
  #     # Handle the connection error here (e.g., log the error, send an alert)
  # finally:
  #     if conn:
  #         conn.close()
    
    
    
    
    
    
    
    
    
    
    
    
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

if __name__ == "__main__":
  databases = list_databases()

  if databases:
    print("Available databases:")
    for db in databases:
      print(db)
  else:
    print("No databases found.")
