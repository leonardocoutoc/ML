import json
import csv
import p_owners_m
import mysql.connector.errors

def get_owners():
     # OPEN JSON FILE:
    file = open('dblist.json', encoding='utf-8')
    data = json.load(file)
    file.close

    # OPEN ORIGINAL CSV:
    csv_file = open('user_manager.csv')
    csv_reader_f = csv.reader(csv_file)
    csv_file.close

    # CREATE NEW CSV WITH PROPER HEADER BASED ON ORIGINAL CSV:
    new_csv = 'user_manager_2.csv'
    dict_header = ['number', 'uid', 'status', 'email_manager']
    csv_list=list(csv_reader_f)
    with open(new_csv, 'w', newline="") as file_2:
            csvwriter = csv.writer(file_2)
            csvwriter.writerow(dict_header)
            csvwriter.writerows(csv_list)
    file_2.close

    # FUNCTION TO GET MAIL MANAGER FROM CSV
    def get_mail_manager(owner_uid):
        csv_file2 = open('user_manager_2.csv')
        csv_reader_f2 = csv.DictReader(csv_file2)
        csv_file2.close
        for infos in csv_reader_f2:
            owner_manager_email=None
            owner_curr_status=None
            try:  
                if owner_uid == infos['uid']:
                    owner_manager_email = infos['email_manager']
                    owner_curr_status = infos['status']
                    return owner_manager_email, owner_curr_status
                else:
                    continue
            except:
                print("Warning: in get_mail_manager function")

    # CLEAR OWNERS TABLE AND COLECT NEEDED DATA FROM JSON AND CSV:
    p_owners_m.truncate_owners()

    dbs_list = data['db_list']
    for db in dbs_list:
        owner_uid=None
        owner_name=None
        owner_email=None
        owner_manager_email_status=None
        owner_manager_email=None
        owner_status=None
        
        try:
            owner_uid = (db['owner']['uid'])
            owner_name = (db['owner']['name'])
            owner_email = (db['owner']['email'])
        except KeyError as ke:
            print("Warning: ", ke)
        except TypeError as te:
            print("Warning: ", te)

        try:
            owner_manager_email_status=get_mail_manager(owner_uid)
            owner_manager_email = owner_manager_email_status[0]
            owner_status = owner_manager_email_status[1]
        except:
            print("Warning: Get mail manager function")

        try:
            p_owners_m.inserir_owners(owner_name,owner_uid,owner_manager_email,owner_email,owner_status)            
        except mysql.connector.errors.IntegrityError as msqlIE:
            print("Warning: ", msqlIE)
            

        # try:
        #     owner_manager_email_status=get_mail_manager(owner_uid)
        #     if owner_manager_email_status is not None:                
        #         owner_manager_email = owner_manager_email_status[0]
        #         owner_status = owner_manager_email_status[1]
        #         #print("MGMT Email de ", owner_name , owner_uid, "é " , owner_manager_email, " seu status: ", owner_status)  
        #     p_owners_m.inserir_owners(owner_name,owner_uid,owner_manager_email,owner_email,owner_status)            

        
