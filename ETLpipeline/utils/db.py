import mysql.connector
from mysql.connector import Error
from ETLpipeline.config import config

database_config = config.get_database_config()

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=database_config['host'],
            user=database_config['user'],
            password=database_config['password'],
            database=database_config['name']
        )
        if conn.is_connected():
            print("Successfully connected to the database.")
            return conn
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
get_db_connection()