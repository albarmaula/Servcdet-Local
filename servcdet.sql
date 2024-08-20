<<<<<<< HEAD
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: servcdet
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `detection`
--

DROP TABLE IF EXISTS detection;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE detection (
  detection_id int NOT NULL AUTO_INCREMENT,
  image longtext COLLATE utf8mb4_general_ci NOT NULL,
  label varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  patient_id int NOT NULL,
  note varchar(5000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  user_id int NOT NULL,
  confidence varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (detection_id)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detection`
--

LOCK TABLES detection WRITE;
/*!40000 ALTER TABLE detection DISABLE KEYS */;
INSERT INTO detection VALUES (1,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','normal','2024-05-14 08:03:19',1,'-Tidak ada kelainan\n-normal',2,'80','non-aktif'),(2,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','abnormal','2024-06-14 08:03:19',1,NULL,2,'80','non-aktif'),(3,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','abnormal','2024-06-14 08:03:19',1,NULL,2,'75','non-aktif'),(4,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','abnormal','2024-06-14 08:03:19',1,NULL,2,'75','non-aktif'),(37,'det_b9ecaf15-2ae6-11ef-b997-409f38674562_157183828-157183877-001.BMP','normal','2024-06-15 07:13:22',1,'-Tidak ada kelainan\r\n-normal\r\n-alhamdulillah',2,'90.06107661833367','aktif'),(38,'det_b7d6f83a-2af7-11ef-a997-409f38674562_153956279-153956296-001.BMP','abnormal','2024-06-15 09:14:59',3,'percobaan',2,'85.80004436406912','aktif'),(39,'det_1fe0f970-2af8-11ef-bc3b-409f38674562_153955676-153955721-001.BMP','normal','2024-06-15 09:17:46',2,'-Tidak ada kelainan -normal',2,'90.20014168221728','aktif'),(40,'det_8878a9c3-2af8-11ef-9a21-409f38674562_157222647-157222687-001.BMP','normal','2024-06-15 09:20:41',4,'-Tidak ada kelainan\n-normal',2,'92.02862337923716','aktif'),(41,'det_a0fa54ae-2af8-11ef-b4f9-409f38674562_157222801-157222811-002.BMP','normal','2024-06-15 09:21:22',3,'-Tidak ada kelainan\n-normal',2,'92.16625810699365','aktif'),(42,'det_60e25c75-2afa-11ef-af19-409f38674562_157183332-157183388-002.BMP','normal','2024-06-15 09:33:54',2,'-Tidak ada kelainan\r\n-normal',2,'89.41389245548005','aktif'),(43,'det_b713527d-3fb6-11ef-8a75-409f38674562_153958345-153958392-001.BMP','abnormal','2024-07-11 18:52:40',1,'',2,'71.28640387648835','aktif'),(44,'det_faa4b614-3fb6-11ef-9ec4-409f38674562_157181671-157181686-001.BMP','normal','2024-07-11 18:54:19',1,'',2,'88.5512553422646','aktif'),(45,'det_e835d87b-3fb9-11ef-88fe-409f38674562_NL_1__10.jpg','normal','2024-07-11 19:15:17',1,'',2,'92.4607006780852','aktif'),(46,'det_efb60a38-3fb9-11ef-8071-409f38674562_NL_3__5.jpg','normal','2024-07-11 19:15:29',1,'',2,'91.47729926424537','aktif'),(47,'det_f44d70f1-3fb9-11ef-b5cc-409f38674562_NL_5__3.jpg','abnormal','2024-07-11 19:15:37',1,'',2,'66.74431082368352','aktif'),(48,'det_002b2899-3fba-11ef-82d4-409f38674562_NL_30__6.jpg','abnormal','2024-07-11 19:15:57',1,'',2,'86.21110771989954','aktif'),(49,'det_064be71d-3fba-11ef-b615-409f38674562_scc_1_9.jpg','abnormal','2024-07-11 19:16:07',1,'',2,'85.7233450533998','aktif'),(50,'det_0b255a54-3fba-11ef-9855-409f38674562_scc_2_3.jpg','abnormal','2024-07-11 19:16:15',1,'',2,'85.69551848853708','aktif'),(51,'det_0f39217f-3fba-11ef-904c-409f38674562_SCC_4_1.jpg','normal','2024-07-11 19:16:22',1,'',2,'86.23014278286445','aktif'),(52,'det_918eb73e-3ff2-11ef-b1a1-409f38674562_scc_1_1.jpg','abnormal','2024-07-12 02:01:10',2,NULL,2,'86.26988804019278','aktif'),(53,'det_0157d547-3ff3-11ef-a6f7-409f38674562_153958547-153958572-003.BMP','abnormal','2024-07-12 02:04:01',1,'',2,'85.6955718559852','aktif'),(54,'det_5b4b8d1b-4406-11ef-9545-aa3f0eedc792_153955676-153955721-001.BMP','normal','2024-07-17 06:32:43',3,'-ga ada kelainan',2,'90.19706200011684','aktif'),(55,'det_888edc50-4407-11ef-a5d3-aa3f0eedc792_scc_1_1.jpg','abnormal','2024-07-17 06:41:03',1,'',2,'86.26988804019278','aktif'),(56,'det_aef5bdf1-4408-11ef-8495-aa3f0eedc792_153955676-153955721-001.BMP','normal','2024-07-17 06:49:23',1,'',2,'90.19706200011684','aktif'),(57,'det_06e99c20-4e78-11ef-b079-409f38674562_HSIL_1_1.jpg','abnormal','2024-07-30 13:31:39',5,'',2,'75.91115656319899','aktif'),(58,'det_0609ee7a-5099-11ef-932a-409f38674562_153955676-153955721-001.BMP','normal','2024-08-02 06:32:49',5,'',2,'90.19706200011684','aktif');
/*!40000 ALTER TABLE detection ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS patient;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE patient (
  id int NOT NULL AUTO_INCREMENT,
  nik varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  username varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  phone varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  birthday date NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES patient WRITE;
/*!40000 ALTER TABLE patient DISABLE KEYS */;
INSERT INTO patient VALUES (1,'35781565980003','Anisa','081234568989','2011-06-15','2024-06-12 22:16:20','belum menikah'),(2,'35782312320001','Siti','085657579212','2024-06-15','2024-06-15 10:53:12','menikah'),(3,'35781123210002','Sari','081256871456','2024-06-13','2024-06-15 10:53:33','belum menikah'),(4,'35786512010002','Sumini','085654872369','2024-05-28','2024-06-15 10:54:01','belum menikah'),(5,'35781329123124','Miris Sumiris','085649415896','2024-07-24','2024-07-30 18:30:07','belum menikah');
/*!40000 ALTER TABLE patient ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS user;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  user_id int NOT NULL AUTO_INCREMENT,
  username varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  phone varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  email varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `role` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `status` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  profile_picture varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (user_id),
  UNIQUE KEY email (email)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES user WRITE;
/*!40000 ALTER TABLE user DISABLE KEYS */;
INSERT INTO user VALUES (1,'Gianluigi Buffon','085649415981','superadmin1@gmail.com','scrypt:32768:8:1$QIjCokfRHz1ARA3L$f02b724c6539ad4caf63cc47a5703c9720a6911e3b8b31a972d8c442eec398949d75ce5b80201dc3651df2ce8e306ea3be1dbb1c32581c776f44ac56ed7c782a','2024-03-24 17:00:00','superadmin','aktif','pp_5dd5abec-5ec3-11ef-93bc-409f38674562_farhan.png'),(2,'Adudu Adidi','085658541256','dokter@gmail.com','scrypt:32768:8:1$WwbjFqFqDJuLhCxr$de967e1c462d9c1f667f175980f886c38f5c660024cb9ae7e69c191c3a4e80cfd3f1a95c6032afbb5035e6a8c0747409289ad164f98499620e36a1811c248e47','2024-03-29 17:00:00','dokter','aktif','pp_e63ca0a4-5ec3-11ef-8a68-409f38674562_a.png'),(6,'Lala Lele','081259709492','asd@gmail.com','scrypt:32768:8:1$0oP4aARporv6cgiF$d3840c839d4cfb087f2bde79d22710c373372416077ddf75c34a264fa18ca4077ce7bbe27a5e25c6bbcffe9b802bb740108b59add6935f8a23ab0a55299a2cd0','2024-05-01 12:53:04','dokter','non-aktif','user-black.png'),(7,'Mina Mino','085649872121','admin@gmail.com','scrypt:32768:8:1$ZUo2fAGHpPezqUbz$6c2135e317b7dfb7383758c2c126ef5ff0671ef4d9c5c2d1b0a6f0ed1cd5af4473bde8531a31cac4dadfdaf5cfd657083c40cc88faeadf4bd6f3d1efc3617df0','2024-06-12 10:16:16','admin','aktif','pp_f24d9369-5ec3-11ef-87f1-409f38674562_Screenshot_1asd.png'),(9,'Santi Sinta','081256849512','tes2@gmail.com','scrypt:32768:8:1$tfYXk9HoY6syJqG2$a5f5dbc0b268031c5d61298989a38e74b6a7a546528dbae720768dae09336732237a469bbea107446c202314375c3a400cb1549a43f513db3740a7698c8f5828','2024-06-12 11:15:42','admin','non-aktif','user-black.png'),(10,'Delle Ali','081259709492','superadmin@gmail.com','scrypt:32768:8:1$80dmLfaIlpV0bwjm$72c657cbb2e880174e8765c8c7bc07fd31b2f08c463925027b6acb07c39604a2a111799275a2abc84afd81ca3af267dbfe7f340fd88355519bc0dab46981267c','2024-06-12 11:17:39','superadmin','aktif','pp_4bc13b75-5ec3-11ef-a9e0-409f38674562_skiploafer.png'),(11,'Gareth Southgate','085648953215','dokter2@gmail.com','scrypt:32768:8:1$RN6zhtuDbdtC0hL7$332462a52e1e35f1262488e8d670d0c458d45092022f4ba6ff2f7d6d8b8e3707811fd6f69538a38456952aad3faeae96f5358fafa011594997a6d2d4ff22d7a5','2024-06-15 04:16:14','dokter','aktif','user-black.png'),(12,'Jurgen Klop','082156547485','jurgen@gmail.com','scrypt:32768:8:1$VVWOR4KRrvwAgIQe$7ce518a07c25e4db37d99d0d5d5a6d36678e0a0ea6d4ee39beb0ae6735e136f581f4650ce5dff09aebc6781ece96753ddd97884031e94d770293d53dc7ca5c07','2024-07-30 11:00:04','dokter','aktif','user-black.png');
/*!40000 ALTER TABLE user ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-20 14:24:04
=======
-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: servcdet
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `detection`
--

DROP TABLE IF EXISTS detection;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE detection (
  detection_id int NOT NULL AUTO_INCREMENT,
  image longtext COLLATE utf8mb4_general_ci NOT NULL,
  label varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  patient_id int NOT NULL,
  note varchar(5000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  user_id int NOT NULL,
  confidence varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (detection_id)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detection`
--

LOCK TABLES detection WRITE;
/*!40000 ALTER TABLE detection DISABLE KEYS */;
INSERT INTO detection VALUES (1,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','normal','2024-05-14 08:03:19',1,'-Tidak ada kelainan\n-normal',2,'80','non-aktif'),(2,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','abnormal','2024-06-14 08:03:19',1,NULL,2,'80','non-aktif'),(3,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','abnormal','2024-06-14 08:03:19',1,NULL,2,'75','non-aktif'),(4,'det_4ac16a54-2150-11ef-879f-b06ebf1f7c31_153955676-153955721-001.BMP','abnormal','2024-06-14 08:03:19',1,NULL,2,'75','non-aktif'),(37,'det_b9ecaf15-2ae6-11ef-b997-409f38674562_157183828-157183877-001.BMP','normal','2024-06-15 07:13:22',1,'-Tidak ada kelainan\r\n-normal\r\n-alhamdulillah',2,'90.06107661833367','aktif'),(38,'det_b7d6f83a-2af7-11ef-a997-409f38674562_153956279-153956296-001.BMP','abnormal','2024-06-15 09:14:59',3,'percobaan',2,'85.80004436406912','aktif'),(39,'det_1fe0f970-2af8-11ef-bc3b-409f38674562_153955676-153955721-001.BMP','normal','2024-06-15 09:17:46',2,'-Tidak ada kelainan -normal',2,'90.20014168221728','aktif'),(40,'det_8878a9c3-2af8-11ef-9a21-409f38674562_157222647-157222687-001.BMP','normal','2024-06-15 09:20:41',4,'-Tidak ada kelainan\n-normal',2,'92.02862337923716','aktif'),(41,'det_a0fa54ae-2af8-11ef-b4f9-409f38674562_157222801-157222811-002.BMP','normal','2024-06-15 09:21:22',3,'-Tidak ada kelainan\n-normal',2,'92.16625810699365','aktif'),(42,'det_60e25c75-2afa-11ef-af19-409f38674562_157183332-157183388-002.BMP','normal','2024-06-15 09:33:54',2,'-Tidak ada kelainan\r\n-normal',2,'89.41389245548005','aktif'),(43,'det_b713527d-3fb6-11ef-8a75-409f38674562_153958345-153958392-001.BMP','abnormal','2024-07-11 18:52:40',1,'',2,'71.28640387648835','aktif'),(44,'det_faa4b614-3fb6-11ef-9ec4-409f38674562_157181671-157181686-001.BMP','normal','2024-07-11 18:54:19',1,'',2,'88.5512553422646','aktif'),(45,'det_e835d87b-3fb9-11ef-88fe-409f38674562_NL_1__10.jpg','normal','2024-07-11 19:15:17',1,'',2,'92.4607006780852','aktif'),(46,'det_efb60a38-3fb9-11ef-8071-409f38674562_NL_3__5.jpg','normal','2024-07-11 19:15:29',1,'',2,'91.47729926424537','aktif'),(47,'det_f44d70f1-3fb9-11ef-b5cc-409f38674562_NL_5__3.jpg','abnormal','2024-07-11 19:15:37',1,'',2,'66.74431082368352','aktif'),(48,'det_002b2899-3fba-11ef-82d4-409f38674562_NL_30__6.jpg','abnormal','2024-07-11 19:15:57',1,'',2,'86.21110771989954','aktif'),(49,'det_064be71d-3fba-11ef-b615-409f38674562_scc_1_9.jpg','abnormal','2024-07-11 19:16:07',1,'',2,'85.7233450533998','aktif'),(50,'det_0b255a54-3fba-11ef-9855-409f38674562_scc_2_3.jpg','abnormal','2024-07-11 19:16:15',1,'',2,'85.69551848853708','aktif'),(51,'det_0f39217f-3fba-11ef-904c-409f38674562_SCC_4_1.jpg','normal','2024-07-11 19:16:22',1,'',2,'86.23014278286445','aktif'),(52,'det_918eb73e-3ff2-11ef-b1a1-409f38674562_scc_1_1.jpg','abnormal','2024-07-12 02:01:10',2,NULL,2,'86.26988804019278','aktif'),(53,'det_0157d547-3ff3-11ef-a6f7-409f38674562_153958547-153958572-003.BMP','abnormal','2024-07-12 02:04:01',1,'',2,'85.6955718559852','aktif'),(54,'det_5b4b8d1b-4406-11ef-9545-aa3f0eedc792_153955676-153955721-001.BMP','normal','2024-07-17 06:32:43',3,'-ga ada kelainan',2,'90.19706200011684','aktif'),(55,'det_888edc50-4407-11ef-a5d3-aa3f0eedc792_scc_1_1.jpg','abnormal','2024-07-17 06:41:03',1,'',2,'86.26988804019278','aktif'),(56,'det_aef5bdf1-4408-11ef-8495-aa3f0eedc792_153955676-153955721-001.BMP','normal','2024-07-17 06:49:23',1,'',2,'90.19706200011684','aktif'),(57,'det_06e99c20-4e78-11ef-b079-409f38674562_HSIL_1_1.jpg','abnormal','2024-07-30 13:31:39',5,'',2,'75.91115656319899','aktif'),(58,'det_0609ee7a-5099-11ef-932a-409f38674562_153955676-153955721-001.BMP','normal','2024-08-02 06:32:49',5,'',2,'90.19706200011684','aktif');
/*!40000 ALTER TABLE detection ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS patient;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE patient (
  id int NOT NULL AUTO_INCREMENT,
  nik varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  username varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  phone varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  birthday date NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(25) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES patient WRITE;
/*!40000 ALTER TABLE patient DISABLE KEYS */;
INSERT INTO patient VALUES (1,'35781565980003','Anisa','081234568989','2011-06-15','2024-06-12 22:16:20','belum menikah'),(2,'35782312320001','Siti','085657579212','2024-06-15','2024-06-15 10:53:12','menikah'),(3,'35781123210002','Sari','081256871456','2024-06-13','2024-06-15 10:53:33','belum menikah'),(4,'35786512010002','Sumini','085654872369','2024-05-28','2024-06-15 10:54:01','belum menikah'),(5,'35781329123124','Miris Sumiris','085649415896','2024-07-24','2024-07-30 18:30:07','belum menikah');
/*!40000 ALTER TABLE patient ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS user;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  user_id int NOT NULL AUTO_INCREMENT,
  username varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  phone varchar(15) COLLATE utf8mb4_general_ci NOT NULL,
  email varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `role` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `status` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  profile_picture varchar(1000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (user_id),
  UNIQUE KEY email (email)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES user WRITE;
/*!40000 ALTER TABLE user DISABLE KEYS */;
INSERT INTO user VALUES (1,'Gianluigi Buffon','085649415981','superadmin1@gmail.com','scrypt:32768:8:1$QIjCokfRHz1ARA3L$f02b724c6539ad4caf63cc47a5703c9720a6911e3b8b31a972d8c442eec398949d75ce5b80201dc3651df2ce8e306ea3be1dbb1c32581c776f44ac56ed7c782a','2024-03-24 17:00:00','superadmin','aktif','pp_5dd5abec-5ec3-11ef-93bc-409f38674562_farhan.png'),(2,'Adudu Adidi','085658541256','dokter@gmail.com','scrypt:32768:8:1$WwbjFqFqDJuLhCxr$de967e1c462d9c1f667f175980f886c38f5c660024cb9ae7e69c191c3a4e80cfd3f1a95c6032afbb5035e6a8c0747409289ad164f98499620e36a1811c248e47','2024-03-29 17:00:00','dokter','aktif','pp_e63ca0a4-5ec3-11ef-8a68-409f38674562_a.png'),(6,'Lala Lele','081259709492','asd@gmail.com','scrypt:32768:8:1$0oP4aARporv6cgiF$d3840c839d4cfb087f2bde79d22710c373372416077ddf75c34a264fa18ca4077ce7bbe27a5e25c6bbcffe9b802bb740108b59add6935f8a23ab0a55299a2cd0','2024-05-01 12:53:04','dokter','non-aktif','user-black.png'),(7,'Mina Mino','085649872121','admin@gmail.com','scrypt:32768:8:1$ZUo2fAGHpPezqUbz$6c2135e317b7dfb7383758c2c126ef5ff0671ef4d9c5c2d1b0a6f0ed1cd5af4473bde8531a31cac4dadfdaf5cfd657083c40cc88faeadf4bd6f3d1efc3617df0','2024-06-12 10:16:16','admin','aktif','pp_f24d9369-5ec3-11ef-87f1-409f38674562_Screenshot_1asd.png'),(9,'Santi Sinta','081256849512','tes2@gmail.com','scrypt:32768:8:1$tfYXk9HoY6syJqG2$a5f5dbc0b268031c5d61298989a38e74b6a7a546528dbae720768dae09336732237a469bbea107446c202314375c3a400cb1549a43f513db3740a7698c8f5828','2024-06-12 11:15:42','admin','non-aktif','user-black.png'),(10,'Delle Ali','081259709492','superadmin@gmail.com','scrypt:32768:8:1$80dmLfaIlpV0bwjm$72c657cbb2e880174e8765c8c7bc07fd31b2f08c463925027b6acb07c39604a2a111799275a2abc84afd81ca3af267dbfe7f340fd88355519bc0dab46981267c','2024-06-12 11:17:39','superadmin','aktif','pp_4bc13b75-5ec3-11ef-a9e0-409f38674562_skiploafer.png'),(11,'Gareth Southgate','085648953215','dokter2@gmail.com','scrypt:32768:8:1$RN6zhtuDbdtC0hL7$332462a52e1e35f1262488e8d670d0c458d45092022f4ba6ff2f7d6d8b8e3707811fd6f69538a38456952aad3faeae96f5358fafa011594997a6d2d4ff22d7a5','2024-06-15 04:16:14','dokter','aktif','user-black.png'),(12,'Jurgen Klop','082156547485','jurgen@gmail.com','scrypt:32768:8:1$VVWOR4KRrvwAgIQe$7ce518a07c25e4db37d99d0d5d5a6d36678e0a0ea6d4ee39beb0ae6735e136f581f4650ce5dff09aebc6781ece96753ddd97884031e94d770293d53dc7ca5c07','2024-07-30 11:00:04','dokter','aktif','user-black.png');
/*!40000 ALTER TABLE user ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-20 14:24:04
>>>>>>> 7917c81abca7cc4b446cc217fa1118a11e2d5904
