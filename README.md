How to configure database?

Execute below queries on mysql workbench or any db viewer
1. CREATE DATABASE `web_data` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
<br />
<br />
2. CREATE TABLE `info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `end_year` varchar(10) DEFAULT NULL,
  `intensity` int DEFAULT NULL,
  `sector` varchar(50) DEFAULT NULL,
  `topic` varchar(50) DEFAULT NULL,
  `insight` varchar(100) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `region` varchar(50) DEFAULT NULL,
  `start_year` varchar(10) DEFAULT NULL,
  `impact` varchar(50) DEFAULT NULL,
  `added` timestamp NULL DEFAULT NULL,
  `published` timestamp NULL DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `relevance` int DEFAULT NULL,
  `pestle` varchar(50) DEFAULT NULL,
  `source` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `likelihood` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; 
<br />
<br />
3. SET @@global.sql_mode= ''
NOTE: MySQL will truncate any insert value that exceeds the specified column width.
to make this without error try switch your SQL mode to not use STRICT.