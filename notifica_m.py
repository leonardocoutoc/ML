import smtplib, ssl
import p_notifica_m

# FUNCTION TO SEND MAIL:
def send_mail(owner_name,to_email, bd_name, item_affected):
    port = 465  # For SSL
    password = "lqrgtuynbdagnoxv"

    # Create a secure SSL context
    context = ssl.create_default_context()

    sender_email = "notifica.bd.criticity@gmail.com"
    bcc = "maisquetrilhas@gmail.com"
    receiver_email = to_email
    rcpt = [bcc] + [receiver_email]
    message = """\
Subject: Check Data Base Classification

Hi,

Kindly give us your OK related to HIGH classification to the following Database:

Approver:  """ +str(to_email)+ """
Database: """ +str(bd_name)+ """ 
DB Owner name: """ +str(owner_name)+ """
Impacted Item: """ +str(item_affected)+ """ 
Classification: HIGH

"""
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("notifica.bd.criticity@gmail.com", password)
            #server.sendmail(sender_email, receiver_email, message.encode())
            server.sendmail(sender_email, rcpt, message.encode())
    except:
        print("Erro envio de email.")

# COLLECT NEEDED DATA TO SEND MAIL TO MANAGERS:
def send_mail_to_managers():
    confidentiality_data=p_notifica_m.get_bd_confidentiality()
    for row in confidentiality_data:
        manager_email=row[0]
        bd_name=row[1]
        owner_name=row[2]

        if manager_email and bd_name and owner_name is not None:
            print("Sending mail to:", manager_email, "Owner, DB and Classification: ", owner_name, bd_name ,"confidentiality")
            send_mail(owner_name,manager_email,bd_name,"confidentiality")        
            
    integrity_data=p_notifica_m.get_bd_integrity()
    for row in integrity_data:
        manager_email=row[0]
        bd_name=row[1]
        owner_name=row[2]
        if manager_email and bd_name and owner_name is not None:
            print("Sending mail to:", manager_email, "Owner, DB and Classification: ", owner_name, bd_name ,"integrity")
            send_mail(owner_name,manager_email,bd_name,"integrity")            

    availability_data=p_notifica_m.get_bd_availability()
    for row in availability_data:
        manager_email=row[0]
        bd_name=row[1]
        owner_name=row[2]
        if manager_email and bd_name and owner_name is not None:
            print("Sending mail to:", manager_email, "Owner, DB amd Classification: ", owner_name, bd_name ,"availability")
            send_mail(owner_name,manager_email,bd_name,"availability")
            



