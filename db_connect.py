import mariadb
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = mariadb.connect(
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=3306,
            database=os.environ['DB_NAME']
        )
        return connection
    except Exception as e:
        print(f"Unable to Connect to Database: {e}")

