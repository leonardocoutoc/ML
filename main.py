import owners_m
import databases_m
import notifica_m
#import time

# i=1
# j=15
# while i <= 15:
#     print("Waiting for MySQL service, please wait... ", j,"s" )
#     time.sleep(1)
#     i=i+1
#     j=j-1

owners_m.get_owners()
databases_m.get_database()
notifica_m.send_mail_to_managers()