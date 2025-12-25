import os
import pyodbc
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

def get_database_connection():
    # Use an f-string to correctly embed the environment variables
    connect = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.environ['MSSQL_HOST']};"
        f"DATABASE={os.environ['MSSQL_DB']};"
        f"UID={os.environ['MSSQL_USER']};"
        f"PWD={os.environ['MSSQL_PASS']}",
        autocommit=True
    )

    return connect
