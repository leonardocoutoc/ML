import p_db_connection
import mysql.connector.errors


def inserir_databases(uid_owner, bd_confidentiality, bd_integrity, bd_availability, bd_name):
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()
    #print("Vou inserir bd_databases: ", "uid_owner:",uid_owner, "bd_confidentiality:", bd_confidentiality, "bd_integrity:", bd_integrity, "bd_availability:", bd_availability, "bd_name:", bd_name)
    sql_statement = "INSERT INTO dbs_list (uid_owner, bd_confidentiality, bd_integrity, bd_availability, bd_name) VALUES (%s, %s, %s, %s,%s)"
    sql_values = (uid_owner, bd_confidentiality, bd_integrity, bd_availability, bd_name)
    try:
        cursor.execute(sql_statement, sql_values)
        #cursor.execute(sql_statement)
        conn.commit()
        p_db_connection.db_close(cursor,conn)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Error MySQL:", msqlIE)

def truncate_dbs_list():
    conn = p_db_connection.db_connect()
    cursor = conn.cursor()

    try:
        cursor.execute("SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0")
        cursor.execute("TRUNCATE `dbs_list`")
        cursor.execute("SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1)")
        p_db_connection.db_close(cursor,conn)
    except mysql.connector.errors.IntegrityError as msqlIE:
        print("Error MySQL:", msqlIE)
        




