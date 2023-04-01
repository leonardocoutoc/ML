import p_create_database_m
import owners_m
import databases_m
import notifica_m

p_create_database_m.create_database()
owners_m.get_owners()
databases_m.get_database()
notifica_m.send_mail_to_managers()

