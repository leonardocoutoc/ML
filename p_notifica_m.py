import p_db_connection
import mysql.connector.errors


def get_bd_confidentiality():
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()

    sql_statement="SELECT owner_manager_email,bd_name,owner_name FROM owners_dbs WHERE bd_confidentiality = 'high'"
    try:
        cursor.execute(sql_statement)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Warning: ", msqlIE)
    record = cursor.fetchall()
    p_db_connection.db_close(cursor,conn)
    return record

def get_bd_integrity():
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()

    sql_statement="SELECT owner_manager_email,bd_name,owner_name FROM owners_dbs WHERE bd_integrity = 'high'"
    try:
        cursor.execute(sql_statement)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Warning: ", msqlIE)
    record = cursor.fetchall()
    p_db_connection.db_close(cursor,conn)
    return record

def get_bd_availability():
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()
    
    sql_statement="SELECT owner_manager_email,bd_name,owner_name FROM owners_dbs WHERE bd_availability = 'high'"
    try:
        cursor.execute(sql_statement)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Warning: ", msqlIE)
    record = cursor.fetchall()
    p_db_connection.db_close(cursor,conn)
    return record
