import mysql.connector
import json
import time

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

def create_database():

    i=1
    j=15
    while i <= j:
        print("Waiting for MySQL service, please wait...")
        time.sleep(1)
        i=i+1

    try:    
        db_con_2 = mysql.connector.connect(
            host     = host_srv,
            user     = user_bd,
            password = password_bd
        )
        conn_2 = db_con_2
        cursor_2 = conn_2.cursor()
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
       
    
    sql_create_db="CREATE DATABASE IF NOT EXISTS `bds_classification`"
    sql_use_db="USE `bds_classification`"    
    sql_create_tables="/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */; /*!40101 SET NAMES utf8 */; /*!50503 SET NAMES utf8mb4 */; /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */; /*!40103 SET TIME_ZONE='+00:00' */; /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */; /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */; /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;   CREATE TABLE IF NOT EXISTS `dbs_list` (   `bd_id` int NOT NULL AUTO_INCREMENT,   `uid_owner` varchar(50) NOT NULL DEFAULT '',   `bd_confidentiality` varchar(50) DEFAULT '',   `bd_integrity` varchar(50) DEFAULT '',   `bd_availability` varchar(50) DEFAULT '',   `bd_name` varchar(50) NOT NULL DEFAULT '',   PRIMARY KEY (`bd_id`) USING BTREE,   KEY `Index 2` (`uid_owner`),   CONSTRAINT `FK_dbs_list_owners` FOREIGN KEY (`uid_owner`) REFERENCES `owners` (`owner_id`) ) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;  CREATE TABLE IF NOT EXISTS `owners` (   `o_id` int NOT NULL AUTO_INCREMENT,   `owner_id` varchar(50) NOT NULL DEFAULT '',   `owner_manager_email` varchar(50) DEFAULT NULL,   `owner_email` varchar(50) DEFAULT NULL,   `owner_status` varchar(50) DEFAULT NULL,   `owner_name` varchar(50) DEFAULT NULL,   PRIMARY KEY (`o_id`) USING BTREE,   KEY `owner_id` (`owner_id`) USING BTREE ) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;  CREATE TABLE `owners_dbs` ( 	`owner_name` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci', 	`owner_id` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci', 	`owner_manager_email` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci', 	`owner_email` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci', 	`owner_status` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci', 	`bd_name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci', 	`bd_confidentiality` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci', 	`bd_integrity` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci', 	`bd_availability` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci' ) ENGINE=MyISAM;  DROP TABLE IF EXISTS `owners_dbs`; CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `owners_dbs` AS select `ow`.`owner_name` AS `owner_name`,`ow`.`owner_id` AS `owner_id`,`ow`.`owner_manager_email` AS `owner_manager_email`,`ow`.`owner_email` AS `owner_email`,`ow`.`owner_status` AS `owner_status`,`dbl`.`bd_name` AS `bd_name`,`dbl`.`bd_confidentiality` AS `bd_confidentiality`,`dbl`.`bd_integrity` AS `bd_integrity`,`dbl`.`bd_availability` AS `bd_availability` from (`owners` `ow` join `dbs_list` `dbl` on((`ow`.`owner_id` = `dbl`.`uid_owner`)));  /*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */; /*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */; /*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */; /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */; /*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;"
    
    try:
        cursor_2.execute(sql_create_db)
        cursor_2.execute(sql_use_db)
        cursor_2.execute(sql_create_tables, multi=True)

        print("Verifying tables...")
        time.sleep(5)

        cursor_2.close()
        conn_2.close()
    
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
    

    