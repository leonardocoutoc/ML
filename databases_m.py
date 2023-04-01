import mysql.connector.errors
import json
import p_databases_m

def get_database():
    # OPEN JSON FILE:
    file = open('dblist.json', encoding='utf-8')
    data = json.load(file)
    file.close

    # CLEAR dbs_list TABLE AND COLECT NEEDED DATA FROM JSON AND CSV:
    p_databases_m.truncate_dbs_list()

    dbs_list = data['db_list']
    for db in dbs_list:
        database_name = None
        database_owner_uid = None
        database_confidentiality = None
        database_integrity = None
        database_availability = None
        try:
            database_name = (db['dn_name'])
            database_owner_uid = (db['owner']['uid'])
            database_confidentiality = (db['classification']['confidentiality'])
            database_integrity = (db['classification']['integrity'])
            database_availability = (db['classification']['availability'])
            p_databases_m.inserir_databases(database_owner_uid,database_confidentiality,database_integrity,database_availability,database_name)
            #print("owner ", database_owner_uid, " db_name ", database_name, " confidentiality ", database_confidentiality, " integrity ", database_integrity, " availability ", database_availability)
        except KeyError as KE:
            print("Warning: ", KE)
        except mysql.connector.errors.IntegrityError as msqlIE:
            print("Warning: ", msqlIE)


