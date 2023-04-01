import p_db_connection
import mysql.connector.errors

def inserir_owners(owner_name,owner_id, owner_manager_email, owner_email, owner_status):
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()

    #print("Vou inserir em owners: ", "owner_name: ", owner_name, "owner_id: ",owner_id, "owner_manager_email: ", owner_manager_email, "owner_email: ", owner_email, "owner_status: ", owner_status)
    sql_statement = "INSERT INTO owners (owner_name, owner_id, owner_manager_email, owner_email, owner_status) VALUES (%s,%s,%s, %s, %s)"
    sql_values = (owner_name,owner_id, owner_manager_email, owner_email, owner_status)
    try:        
        cursor.execute(sql_statement, sql_values)
        conn.commit()
        p_db_connection.db_close(cursor,conn)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Error MySQL:", msqlIE)

def truncate_owners():
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0")
        cursor.execute("TRUNCATE `owners`")
        cursor.execute("SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1)")
        p_db_connection.db_close(cursor,conn)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Error MySQL:", msqlIE)