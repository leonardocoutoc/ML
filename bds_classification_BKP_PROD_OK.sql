-- --------------------------------------------------------
-- Servidor:                     192.168.0.72
-- Versão do servidor:           8.0.32-0ubuntu0.22.04.2 - (Ubuntu)
-- OS do Servidor:               Linux
-- HeidiSQL Versão:              12.4.0.6659
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Copiando estrutura do banco de dados para bds_classification
CREATE DATABASE IF NOT EXISTS `bds_classification` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bds_classification`;

-- Copiando estrutura para tabela bds_classification.dbs_list
CREATE TABLE IF NOT EXISTS `dbs_list` (
  `bd_id` int NOT NULL AUTO_INCREMENT,
  `uid_owner` varchar(50) NOT NULL DEFAULT '',
  `bd_confidentiality` varchar(50) DEFAULT '',
  `bd_integrity` varchar(50) DEFAULT '',
  `bd_availability` varchar(50) DEFAULT '',
  `bd_name` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`bd_id`) USING BTREE,
  KEY `Index 2` (`uid_owner`),
  CONSTRAINT `FK_dbs_list_owners` FOREIGN KEY (`uid_owner`) REFERENCES `owners` (`owner_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela bds_classification.dbs_list: ~0 rows (aproximadamente)
INSERT INTO `dbs_list` (`bd_id`, `uid_owner`, `bd_confidentiality`, `bd_integrity`, `bd_availability`, `bd_name`) VALUES
	(1, 'ausuriaga', 'low', 'low', 'medium', 'users'),
	(2, 'dbertoni', 'medium', 'low', 'high', 'items'),
	(3, 'jopastoriza', 'high', 'high', 'low', 'locations'),
	(4, 'dgarnero', 'low', 'medium', 'medium', 'sellers'),
	(5, 'rbochini', 'low', 'low', 'medium', 'sellers'),
	(6, 'laislas', 'high', 'medium', 'medium', 'orders'),
	(7, 'etrossero', 'high', '', 'low', 'questions');

-- Copiando estrutura para tabela bds_classification.owners
CREATE TABLE IF NOT EXISTS `owners` (
  `o_id` int NOT NULL AUTO_INCREMENT,
  `owner_id` varchar(50) NOT NULL DEFAULT '',
  `owner_manager_email` varchar(50) DEFAULT NULL,
  `owner_email` varchar(50) DEFAULT NULL,
  `owner_status` varchar(50) DEFAULT NULL,
  `owner_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`o_id`) USING BTREE,
  KEY `owner_id` (`owner_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Copiando dados para a tabela bds_classification.owners: ~0 rows (aproximadamente)
INSERT INTO `owners` (`o_id`, `owner_id`, `owner_manager_email`, `owner_email`, `owner_status`, `owner_name`) VALUES
	(1, 'ausuriaga', 'leonardocoutoc@gmail.com', 'albeiro@mercadolibre.com', 'contractor', 'Albeiro Usuriaga'),
	(2, 'dbertoni', 'notifica.bd.criticity@gmail.com', '', 'disable', 'Daniel Bertoni'),
	(3, 'jopastoriza', 'leonardocoutoc@gmail.com', 'jose.omar.pastoriza@mercadolibre.com', 'activo', 'José Pastoriza'),
	(4, 'dgarnero', 'leonardocoutoc@gmail.com', 'dani.garnero@mercadolibre.com', 'transferred', 'Daniel Garnero'),
	(5, 'rbochini', 'notifica.bd.criticity@gmail.com', 'ricardo.bochini@mercadolibre.com', 'activo', 'Ricardo Bochini'),
	(6, 'laislas', 'leonardocoutoc@gmail.com', 'luis.islas@mercadolibre.com', 'vacation', 'Luis Alberto Islas'),
	(7, 'etrossero', 'notifica.bd.criticity@gmail.com', 'enzo.trossero@mercadolibre.com', 'activo', 'Enzo Trossero');

-- Copiando estrutura para view bds_classification.owners_dbs
-- Criando tabela temporária para evitar erros de dependência de VIEW
CREATE TABLE `owners_dbs` (
	`owner_name` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`owner_id` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`owner_manager_email` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`owner_email` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`owner_status` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`bd_name` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_0900_ai_ci',
	`bd_confidentiality` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`bd_integrity` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`bd_availability` VARCHAR(50) NULL COLLATE 'utf8mb4_0900_ai_ci'
) ENGINE=MyISAM;

-- Copiando estrutura para view bds_classification.owners_dbs
-- Removendo tabela temporária e criando a estrutura VIEW final
DROP TABLE IF EXISTS `owners_dbs`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `owners_dbs` AS select `ow`.`owner_name` AS `owner_name`,`ow`.`owner_id` AS `owner_id`,`ow`.`owner_manager_email` AS `owner_manager_email`,`ow`.`owner_email` AS `owner_email`,`ow`.`owner_status` AS `owner_status`,`dbl`.`bd_name` AS `bd_name`,`dbl`.`bd_confidentiality` AS `bd_confidentiality`,`dbl`.`bd_integrity` AS `bd_integrity`,`dbl`.`bd_availability` AS `bd_availability` from (`owners` `ow` join `dbs_list` `dbl` on((`ow`.`owner_id` = `dbl`.`uid_owner`)));

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
