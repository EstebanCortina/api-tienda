import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': 'localhost',
    'database': 'tienda',
    'auth_plugin': 'mysql_native_password'
}


def get_connection():
    try:
        mysqlConn = mysql.connector.connect(**db_config)
        print('BD connection succesful')
        return mysqlConn
    except mysql.connector.Error as e:
        print(e)
