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

    try:
        db_con = mysql.connector.connect(
            host     = host_srv,
            user     = user_bd,
            password = password_bd,
            database = database_name
                    )    
    except UnboundLocalError as dbule:
        print("Error creation of database: ", dbule)
    except mysql.connector.DataError as dbde:
        print("Error creation of database: ", dbde)
    except mysql.connector.InterfaceError as dbie:
        print("Error creation of database: ", dbie)
    except mysql.connector.OperationalError as dboe:
        print("Error creation of database: ", dboe)
    except mysql.connector.DatabaseError as dbde:
        print("Error creation of database: ", dbde)
    return db_con

def db_close(cursor, conn):
    try:
        cursor.close()
        conn.close()
    except UnboundLocalError as dbule:
        print("Error creation of database: ", dbule)
    except mysql.connector.DataError as dbde:
        print("Error creation of database: ", dbde)
    except mysql.connector.InterfaceError as dbie:
        print("Error creation of database: ", dbie)
    except mysql.connector.OperationalError as dboe:
        print("Error creation of database: ", dboe)
    except mysql.connector.DatabaseError as dbde:
        print("Error creation of database: ", dbde)

