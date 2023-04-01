import mysql.connector
import json

# OPEN JSON FILE:
file = open('db_settings.json', encoding='utf-8')
data = json.load(file)
file.close

db_connection = data['db_connection']
for config in db_connection:
    host_srv=config['host']
    user_bd=config['user']
    password_bd=config['password']
    database_name=config['database']


def db_connect():
    db_con = mysql.connector.connect(
        host     = host_srv,
        user     = user_bd,
        password = password_bd,
        database = database_name
                 )
    return db_con

def db_close(cursor, conn):
        cursor.close()
        conn.close()

