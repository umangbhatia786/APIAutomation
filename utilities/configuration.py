import configparser
import mysql.connector as my_sql
from mysql.connector import Error


def get_config():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Umang Bhatia\Documents\Udemy\BackEndAutomation\utilities\properties.ini')

    return config


connect_config = {
    'user': get_config()['SQL']['user'],
    'password': get_config()['SQL']['password'],
    'host': get_config()['SQL']['host'],
    'database': get_config()['SQL']['database']
}


def get_connection():
    # print(connect_config['user'])
    try:
        conn = my_sql.connect(**connect_config)
        # print(conn.is_connected())
        if conn.is_connected():
            return conn

    except Error as e:
        print(e)


def get_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()

    return row
