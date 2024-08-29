import mysql.connector
import configparser


config = configparser.ConfigParser()
config.read('app.properties')

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=config['DATABASE']['host'],
            user=config['DATABASE']['user'],
            password=config['DATABASE']['password'],
            database=config['DATABASE']['database']
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
