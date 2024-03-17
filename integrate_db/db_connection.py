import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB_NAME = os.getenv('POSTGRES_DB_NAME')
POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

def remote_db_connection():
    #Establishing the connection
    conn = psycopg2.connect(
        database=POSTGRES_DB_NAME, user=POSTGRES_USERNAME, password=POSTGRES_PASSWORD, host='0.0.0.0', port= '5432'
    )
    return conn
