import os
import pyodbc
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

def get_database_connection(): #Gets database connection
    connect = pyodbc.connect( 
        f"DRIVER={{ODBC Driver 17 for SQL Server}};" #Environmental variables used to keep sensitive data secure, pulled from separate .env file
        f"SERVER={os.environ['MSSQL_HOST']};"
        f"DATABASE={os.environ['MSSQL_DATABASE']};"
        f"UID={os.environ['MSSQL_USERNAME']};"
        f"PWD={os.environ['MSSQL_PASSWORD']}",
        autocommit=True
    )

    return connect
