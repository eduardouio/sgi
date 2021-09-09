-- modelo inicial con usuarios y campos adicionales no creados por django despues del migrae





-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: skeel
-- ------------------------------------------------------
-- Server version	8.0.26

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add group object permission',7,'add_groupobjectpermission'),(26,'Can change group object permission',7,'change_groupobjectpermission'),(27,'Can delete group object permission',7,'delete_groupobjectpermission'),(28,'Can view group object permission',7,'view_groupobjectpermission'),(29,'Can add user object permission',8,'add_userobjectpermission'),(30,'Can change user object permission',8,'change_userobjectpermission'),(31,'Can delete user object permission',8,'delete_userobjectpermission'),(32,'Can view user object permission',8,'view_userobjectpermission'),(33,'Can add rights support',9,'add_rightssupport'),(34,'Can change rights support',9,'change_rightssupport'),(35,'Can delete rights support',9,'delete_rightssupport'),(36,'Can view rights support',9,'view_rightssupport'),(37,'Permisos globales para costos',9,'module_costs_rights'),(38,'Permisos globales para importaciones',9,'module_importations_rights'),(39,'Permisos globales para archivos',9,'module_filemanager_rights'),(40,'Permisos globales para migraciones SAP',9,'module_migrationSap_rights'),(41,'Permisos globales para Pedidos',9,'module_orders_rights'),(42,'Permisos globales para Pagos',9,'module_paids_rights'),(43,'Permisos globales para Parciales',9,'module_partials_rights'),(44,'Permisos globales para productos',9,'module_products_rights'),(45,'Permisos globales para proveedores',9,'module_suppliers_rights'),(46,'Permisos globales para Bodega',9,'module_warenhouse_rights'),(47,'Can add historical file manager',10,'add_historicalfilemanager'),(48,'Can change historical file manager',10,'change_historicalfilemanager'),(49,'Can delete historical file manager',10,'delete_historicalfilemanager'),(50,'Can view historical file manager',10,'view_historicalfilemanager'),(51,'Can add file manager',11,'add_filemanager'),(52,'Can change file manager',11,'change_filemanager'),(53,'Can delete file manager',11,'delete_filemanager'),(54,'Can view file manager',11,'view_filemanager'),(55,'Can add historical ledger',12,'add_historicalledger'),(56,'Can change historical ledger',12,'change_historicalledger'),(57,'Can delete historical ledger',12,'delete_historicalledger'),(58,'Can view historical ledger',12,'view_historicalledger'),(59,'Can add ledger',13,'add_ledger'),(60,'Can change ledger',13,'change_ledger'),(61,'Can delete ledger',13,'delete_ledger'),(62,'Can view ledger',13,'view_ledger'),(63,'Can add supplier',14,'add_supplier'),(64,'Can change supplier',14,'change_supplier'),(65,'Can delete supplier',14,'delete_supplier'),(66,'Can view supplier',14,'view_supplier'),(67,'Can add historical supplier',15,'add_historicalsupplier'),(68,'Can change historical supplier',15,'change_historicalsupplier'),(69,'Can delete historical supplier',15,'delete_historicalsupplier'),(70,'Can view historical supplier',15,'view_historicalsupplier'),(71,'Can add historical order',16,'add_historicalorder'),(72,'Can change historical order',16,'change_historicalorder'),(73,'Can delete historical order',16,'delete_historicalorder'),(74,'Can view historical order',16,'view_historicalorder'),(75,'Can add order',17,'add_order'),(76,'Can change order',17,'change_order'),(77,'Can delete order',17,'delete_order'),(78,'Can view order',17,'view_order'),(79,'Can add historical order invoice',18,'add_historicalorderinvoice'),(80,'Can change historical order invoice',18,'change_historicalorderinvoice'),(81,'Can delete historical order invoice',18,'delete_historicalorderinvoice'),(82,'Can view historical order invoice',18,'view_historicalorderinvoice'),(83,'Can add order invoice',19,'add_orderinvoice'),(84,'Can change order invoice',19,'change_orderinvoice'),(85,'Can delete order invoice',19,'delete_orderinvoice'),(86,'Can view order invoice',19,'view_orderinvoice'),(87,'Can add historical order invoice detail',20,'add_historicalorderinvoicedetail'),(88,'Can change historical order invoice detail',20,'change_historicalorderinvoicedetail'),(89,'Can delete historical order invoice detail',20,'delete_historicalorderinvoicedetail'),(90,'Can view historical order invoice detail',20,'view_historicalorderinvoicedetail'),(91,'Can add order invoice detail',21,'add_orderinvoicedetail'),(92,'Can change order invoice detail',21,'change_orderinvoicedetail'),(93,'Can delete order invoice detail',21,'delete_orderinvoicedetail'),(94,'Can view order invoice detail',21,'view_orderinvoicedetail'),(95,'Can add historical expense',22,'add_historicalexpense'),(96,'Can change historical expense',22,'change_historicalexpense'),(97,'Can delete historical expense',22,'delete_historicalexpense'),(98,'Can view historical expense',22,'view_historicalexpense'),(99,'Can add expense',23,'add_expense'),(100,'Can change expense',23,'change_expense'),(101,'Can delete expense',23,'delete_expense'),(102,'Can view expense',23,'view_expense'),(103,'Can add historical paid invoice',24,'add_historicalpaidinvoice'),(104,'Can change historical paid invoice',24,'change_historicalpaidinvoice'),(105,'Can delete historical paid invoice',24,'delete_historicalpaidinvoice'),(106,'Can view historical paid invoice',24,'view_historicalpaidinvoice'),(107,'Can add paid invoice',25,'add_paidinvoice'),(108,'Can change paid invoice',25,'change_paidinvoice'),(109,'Can delete paid invoice',25,'delete_paidinvoice'),(110,'Can view paid invoice',25,'view_paidinvoice'),(111,'Can add historical paid invoice detail',26,'add_historicalpaidinvoicedetail'),(112,'Can change historical paid invoice detail',26,'change_historicalpaidinvoicedetail'),(113,'Can delete historical paid invoice detail',26,'delete_historicalpaidinvoicedetail'),(114,'Can view historical paid invoice detail',26,'view_historicalpaidinvoicedetail'),(115,'Can add paid invoice detail',27,'add_paidinvoicedetail'),(116,'Can change paid invoice detail',27,'change_paidinvoicedetail'),(117,'Can delete paid invoice detail',27,'delete_paidinvoicedetail'),(118,'Can view paid invoice detail',27,'view_paidinvoicedetail'),(119,'Can add historical rate expense',28,'add_historicalrateexpense'),(120,'Can change historical rate expense',28,'change_historicalrateexpense'),(121,'Can delete historical rate expense',28,'delete_historicalrateexpense'),(122,'Can view historical rate expense',28,'view_historicalrateexpense'),(123,'Can add rate expense',29,'add_rateexpense'),(124,'Can change rate expense',29,'change_rateexpense'),(125,'Can delete rate expense',29,'delete_rateexpense'),(126,'Can view rate expense',29,'view_rateexpense'),(127,'Can add historical rate incoterm',30,'add_historicalrateincoterm'),(128,'Can change historical rate incoterm',30,'change_historicalrateincoterm'),(129,'Can delete historical rate incoterm',30,'delete_historicalrateincoterm'),(130,'Can view historical rate incoterm',30,'view_historicalrateincoterm'),(131,'Can add rate incoterm',31,'add_rateincoterm'),(132,'Can change rate incoterm',31,'change_rateincoterm'),(133,'Can delete rate incoterm',31,'delete_rateincoterm'),(134,'Can view rate incoterm',31,'view_rateincoterm'),(135,'Can add historical partial',32,'add_historicalpartial'),(136,'Can change historical partial',32,'change_historicalpartial'),(137,'Can delete historical partial',32,'delete_historicalpartial'),(138,'Can view historical partial',32,'view_historicalpartial'),(139,'Can add partial',33,'add_partial'),(140,'Can change partial',33,'change_partial'),(141,'Can delete partial',33,'delete_partial'),(142,'Can view partial',33,'view_partial'),(143,'Can add historical apportionment',34,'add_historicalapportionment'),(144,'Can change historical apportionment',34,'change_historicalapportionment'),(145,'Can delete historical apportionment',34,'delete_historicalapportionment'),(146,'Can view historical apportionment',34,'view_historicalapportionment'),(147,'Can add apportionment',35,'add_apportionment'),(148,'Can change apportionment',35,'change_apportionment'),(149,'Can delete apportionment',35,'delete_apportionment'),(150,'Can view apportionment',35,'view_apportionment'),(151,'Can add historical apportionment detail',36,'add_historicalapportionmentdetail'),(152,'Can change historical apportionment detail',36,'change_historicalapportionmentdetail'),(153,'Can delete historical apportionment detail',36,'delete_historicalapportionmentdetail'),(154,'Can view historical apportionment detail',36,'view_historicalapportionmentdetail'),(155,'Can add apportionment detail',37,'add_apportionmentdetail'),(156,'Can change apportionment detail',37,'change_apportionmentdetail'),(157,'Can delete apportionment detail',37,'delete_apportionmentdetail'),(158,'Can view apportionment detail',37,'view_apportionmentdetail'),(159,'Can add historical info invoice',38,'add_historicalinfoinvoice'),(160,'Can change historical info invoice',38,'change_historicalinfoinvoice'),(161,'Can delete historical info invoice',38,'delete_historicalinfoinvoice'),(162,'Can view historical info invoice',38,'view_historicalinfoinvoice'),(163,'Can add info invoice',39,'add_infoinvoice'),(164,'Can change info invoice',39,'change_infoinvoice'),(165,'Can delete info invoice',39,'delete_infoinvoice'),(166,'Can view info invoice',39,'view_infoinvoice'),(167,'Can add historical info invoice detail',40,'add_historicalinfoinvoicedetail'),(168,'Can change historical info invoice detail',40,'change_historicalinfoinvoicedetail'),(169,'Can delete historical info invoice detail',40,'delete_historicalinfoinvoicedetail'),(170,'Can view historical info invoice detail',40,'view_historicalinfoinvoicedetail'),(171,'Can add info invoice detail',41,'add_infoinvoicedetail'),(172,'Can change info invoice detail',41,'change_infoinvoicedetail'),(173,'Can delete info invoice detail',41,'delete_infoinvoicedetail'),(174,'Can view info invoice detail',41,'view_infoinvoicedetail'),(175,'Can add historical migrations',42,'add_historicalmigrations'),(176,'Can change historical migrations',42,'change_historicalmigrations'),(177,'Can delete historical migrations',42,'delete_historicalmigrations'),(178,'Can view historical migrations',42,'view_historicalmigrations'),(179,'Can add migrations',43,'add_migrations'),(180,'Can change migrations',43,'change_migrations'),(181,'Can delete migrations',43,'delete_migrations'),(182,'Can view migrations',43,'view_migrations'),(183,'Can add historical migrations detail',44,'add_historicalmigrationsdetail'),(184,'Can change historical migrations detail',44,'change_historicalmigrationsdetail'),(185,'Can delete historical migrations detail',44,'delete_historicalmigrationsdetail'),(186,'Can view historical migrations detail',44,'view_historicalmigrationsdetail'),(187,'Can add migrations detail',45,'add_migrationsdetail'),(188,'Can change migrations detail',45,'change_migrationsdetail'),(189,'Can delete migrations detail',45,'delete_migrationsdetail'),(190,'Can view migrations detail',45,'view_migrationsdetail'),(191,'Can add historical product',46,'add_historicalproduct'),(192,'Can change historical product',46,'change_historicalproduct'),(193,'Can delete historical product',46,'delete_historicalproduct'),(194,'Can view historical product',46,'view_historicalproduct'),(195,'Can add product',47,'add_product'),(196,'Can change product',47,'change_product'),(197,'Can delete product',47,'delete_product'),(198,'Can view product',47,'view_product');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'!yUWsz9t0BdLEUslWl7EX72EiypBQCrKuyWrfByGa',NULL,0,'AnonymousUser','','','',0,1,'2021-09-09 22:31:26.840870');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `costings_historicalledger`
--

DROP TABLE IF EXISTS `costings_historicalledger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `costings_historicalledger` (
  `id_mayor` int NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `id_parcial` smallint unsigned NOT NULL,
  `costo_inicial_producto` decimal(20,13) NOT NULL,
  `costo_producto` decimal(20,13) NOT NULL,
  `descargas` decimal(20,13) NOT NULL,
  `saldo_producto` decimal(20,13) NOT NULL,
  `precio_entrega` decimal(20,13) NOT NULL,
  `mayor_sap` decimal(20,13) NOT NULL,
  `provisiones_sap` decimal(20,13) NOT NULL,
  `mayor_sgi` decimal(20,13) NOT NULL,
  `provisiones_sgi` decimal(20,13) NOT NULL,
  `facturas_sgi` decimal(20,13) NOT NULL,
  `reliquidacion_ice` decimal(20,13) NOT NULL,
  `bg_mayor` smallint NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_user` int unsigned DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `nro_pedido` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `costings_historicall_history_user_id_63586741_fk_auth_user` (`history_user_id`),
  KEY `costings_historicalledger_id_mayor_ec01def2` (`id_mayor`),
  KEY `costings_historicalledger_nro_pedido_c02a95a7` (`nro_pedido`),
  CONSTRAINT `costings_historicall_history_user_id_63586741_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costings_historicalledger`
--

LOCK TABLES `costings_historicalledger` WRITE;
/*!40000 ALTER TABLE `costings_historicalledger` DISABLE KEYS */;
/*!40000 ALTER TABLE `costings_historicalledger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_documento_pago`
--

DROP TABLE IF EXISTS `detalle_documento_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_documento_pago` (
  `id_detalle_documento_pago` int NOT NULL AUTO_INCREMENT,
  `valor` decimal(8,2) NOT NULL,
  `valor_ajuste` decimal(8,2) NOT NULL,
  `bg_closed` int NOT NULL,
  `bg_isnotprovisioned` int NOT NULL,
  `bg_mayor` smallint NOT NULL,
  `id_user` smallint NOT NULL,
  `comentarios` longtext,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_documento_pago` int NOT NULL,
  `id_gastos_nacionalizacion` int NOT NULL,
  PRIMARY KEY (`id_detalle_documento_pago`),
  UNIQUE KEY `detalle_documento_pago_id_documento_pago_id_gas_d94f08cd_uniq` (`id_documento_pago`,`id_gastos_nacionalizacion`),
  KEY `detalle_documento_pa_id_gastos_nacionaliz_fd2b708b_fk_gastos_na` (`id_gastos_nacionalizacion`),
  CONSTRAINT `detalle_documento_pa_id_documento_pago_cb154384_fk_documento` FOREIGN KEY (`id_documento_pago`) REFERENCES `documento_pago` (`id_documento_pago`),
  CONSTRAINT `detalle_documento_pa_id_gastos_nacionaliz_fd2b708b_fk_gastos_na` FOREIGN KEY (`id_gastos_nacionalizacion`) REFERENCES `gastos_nacionalizacion` (`id_gastos_nacionalizacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_documento_pago`
--

LOCK TABLES `detalle_documento_pago` WRITE;
/*!40000 ALTER TABLE `detalle_documento_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_documento_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_pedido_factura`
--

DROP TABLE IF EXISTS `detalle_pedido_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_pedido_factura` (
  `detalle_pedido_factura` int NOT NULL AUTO_INCREMENT,
  `arancel_advalorem` decimal(20,13) NOT NULL,
  `arancel_advalorem_liberado` decimal(20,13) NOT NULL,
  `arancel_advalorem_pagar` decimal(20,13) NOT NULL,
  `arancel_advalorem_unitario` decimal(20,13) NOT NULL,
  `arancel_especifico` decimal(20,13) NOT NULL,
  `arancel_especifico_liberado` decimal(20,13) NOT NULL,
  `arancel_especifico_pagar` decimal(20,13) NOT NULL,
  `arancel_especifico_unitario` decimal(20,13) NOT NULL,
  `base_advalorem` decimal(20,13) NOT NULL,
  `base_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `base_ice_epecifico` decimal(20,13) NOT NULL,
  `cajas_importadas` decimal(20,13) NOT NULL,
  `cantidad_x_caja` decimal(20,13) NOT NULL,
  `capacidad_ml` decimal(20,13) NOT NULL,
  `cif` decimal(20,13) NOT NULL,
  `costo_botella` decimal(20,13) NOT NULL,
  `costo_caja` decimal(20,13) NOT NULL,
  `costo_caja_final` decimal(20,13) NOT NULL,
  `costo_total` decimal(20,13) NOT NULL,
  `costo_unidad` decimal(20,13) NOT NULL,
  `etiquetas_fiscales` decimal(20,13) NOT NULL,
  `ex_aduana` decimal(20,13) NOT NULL,
  `ex_aduana_unitario` decimal(20,13) NOT NULL,
  `ex_aduana_antes` decimal(20,13) NOT NULL,
  `ex_aduana_antes_unitario` decimal(20,13) NOT NULL,
  `exaduana_sin_etiquetas` decimal(20,13) NOT NULL,
  `exaduana_sin_tasa` decimal(20,13) NOT NULL,
  `flete` decimal(20,13) NOT NULL,
  `flete_aduana` decimal(20,13) NOT NULL,
  `fob` decimal(20,13) NOT NULL,
  `fob_tasa_trimestral` decimal(20,13) NOT NULL,
  `fob_percent` decimal(20,13) NOT NULL,
  `fodinfa` decimal(20,13) NOT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `gasto_origen_tasa_trimestral` decimal(20,13) NOT NULL,
  `grado_alcoholico` double NOT NULL,
  `ice_advalorem` decimal(20,13) NOT NULL,
  `ice_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `ice_advalorem_diferencia` decimal(20,13) NOT NULL,
  `ice_advalorem_pagado` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_etiquetas` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_tasa` decimal(20,13) NOT NULL,
  `ice_advalorem_unitario` decimal(20,13) NOT NULL,
  `ice_especifico` decimal(20,13) NOT NULL,
  `ice_especifico_unitario` decimal(20,13) NOT NULL,
  `ice_unitario` decimal(20,13) NOT NULL,
  `id_parcial` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `indirectos` decimal(20,13) NOT NULL,
  `iva` decimal(20,13) NOT NULL,
  `iva_total` decimal(20,13) NOT NULL,
  `iva_unidad` decimal(20,13) NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `nro_cajas` smallint NOT NULL,
  `nro_factura_informativa` decimal(20,13) NOT NULL,
  `nro_pedido` varchar(10) DEFAULT NULL,
  `otros` decimal(20,13) NOT NULL,
  `peso` decimal(20,13) NOT NULL,
  `product` varchar(200) DEFAULT NULL,
  `prorrateo_parcial` decimal(20,13) NOT NULL,
  `prorrateo_pedido` decimal(20,13) NOT NULL,
  `prorrateos_total` decimal(20,13) NOT NULL,
  `seguro` decimal(20,13) NOT NULL,
  `seguro_aduana` decimal(20,13) NOT NULL,
  `tasa_control` decimal(20,13) NOT NULL,
  `total_ice` decimal(20,13) NOT NULL,
  `unidades` decimal(20,13) NOT NULL,
  `unidades_importadas` decimal(20,13) NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `cod_contable` varchar(20) NOT NULL,
  `id_pedido_factura` int NOT NULL,
  PRIMARY KEY (`detalle_pedido_factura`),
  UNIQUE KEY `detalle_pedido_factura_id_pedido_factura_cod_co_ebcb4c07_uniq` (`id_pedido_factura`,`cod_contable`,`grado_alcoholico`,`date_create`),
  KEY `detalle_pedido_factu_cod_contable_9a94693c_fk_producto_` (`cod_contable`),
  CONSTRAINT `detalle_pedido_factu_cod_contable_9a94693c_fk_producto_` FOREIGN KEY (`cod_contable`) REFERENCES `producto` (`cod_contable`),
  CONSTRAINT `detalle_pedido_factu_id_pedido_factura_826e58b9_fk_pedido_fa` FOREIGN KEY (`id_pedido_factura`) REFERENCES `pedido_factura` (`id_pedido_factura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_pedido_factura`
--

LOCK TABLES `detalle_pedido_factura` WRITE;
/*!40000 ALTER TABLE `detalle_pedido_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_pedido_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'authentication','rightssupport'),(5,'contenttypes','contenttype'),(12,'costings','historicalledger'),(13,'costings','ledger'),(11,'filemanager','filemanager'),(10,'filemanager','historicalfilemanager'),(7,'guardian','groupobjectpermission'),(8,'guardian','userobjectpermission'),(42,'migrationSAP','historicalmigrations'),(44,'migrationSAP','historicalmigrationsdetail'),(43,'migrationSAP','migrations'),(45,'migrationSAP','migrationsdetail'),(16,'orders','historicalorder'),(18,'orders','historicalorderinvoice'),(20,'orders','historicalorderinvoicedetail'),(17,'orders','order'),(19,'orders','orderinvoice'),(21,'orders','orderinvoicedetail'),(23,'paids','expense'),(22,'paids','historicalexpense'),(24,'paids','historicalpaidinvoice'),(26,'paids','historicalpaidinvoicedetail'),(28,'paids','historicalrateexpense'),(30,'paids','historicalrateincoterm'),(25,'paids','paidinvoice'),(27,'paids','paidinvoicedetail'),(29,'paids','rateexpense'),(31,'paids','rateincoterm'),(35,'partials','apportionment'),(37,'partials','apportionmentdetail'),(34,'partials','historicalapportionment'),(36,'partials','historicalapportionmentdetail'),(38,'partials','historicalinfoinvoice'),(40,'partials','historicalinfoinvoicedetail'),(32,'partials','historicalpartial'),(39,'partials','infoinvoice'),(41,'partials','infoinvoicedetail'),(33,'partials','partial'),(46,'products','historicalproduct'),(47,'products','product'),(6,'sessions','session'),(15,'suppliers','historicalsupplier'),(14,'suppliers','supplier');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-09-09 22:31:25.002998'),(2,'auth','0001_initial','2021-09-09 22:31:25.129939'),(3,'admin','0001_initial','2021-09-09 22:31:25.313267'),(4,'admin','0002_logentry_remove_auto_add','2021-09-09 22:31:25.391558'),(5,'admin','0003_logentry_add_action_flag_choices','2021-09-09 22:31:25.420403'),(6,'contenttypes','0002_remove_content_type_name','2021-09-09 22:31:25.602753'),(7,'auth','0002_alter_permission_name_max_length','2021-09-09 22:31:25.639579'),(8,'auth','0003_alter_user_email_max_length','2021-09-09 22:31:25.681388'),(9,'auth','0004_alter_user_username_opts','2021-09-09 22:31:25.708838'),(10,'auth','0005_alter_user_last_login_null','2021-09-09 22:31:25.766076'),(11,'auth','0006_require_contenttypes_0002','2021-09-09 22:31:25.769335'),(12,'auth','0007_alter_validators_add_error_messages','2021-09-09 22:31:25.798808'),(13,'auth','0008_alter_user_username_max_length','2021-09-09 22:31:25.869349'),(14,'auth','0009_alter_user_last_name_max_length','2021-09-09 22:31:26.018719'),(15,'auth','0010_alter_group_name_max_length','2021-09-09 22:31:26.049079'),(16,'auth','0011_update_proxy_permissions','2021-09-09 22:31:26.159545'),(17,'guardian','0001_initial','2021-09-09 22:31:26.276897'),(18,'sessions','0001_initial','2021-09-09 22:31:26.462282'),(19,'suppliers','0001_initial','2021-09-09 22:31:26.554993'),(20,'products','0001_initial','2021-09-09 22:32:07.139725'),(21,'orders','0001_initial','2021-09-09 22:33:24.001006'),(22,'partials','0001_initial','2021-09-09 22:35:00.325005'),(23,'paids','0001_initial','2021-09-09 22:37:22.245610'),(24,'costings','0001_initial','2021-09-09 22:39:40.696071'),(25,'migrationSAP','0001_initial','2021-09-09 22:41:17.801822'),(26,'filemanager','0001_initial','2021-09-09 22:42:07.693691');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documento_pago`
--

DROP TABLE IF EXISTS `documento_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documento_pago` (
  `id_documento_pago` int NOT NULL AUTO_INCREMENT,
  `nro_factura` varchar(20) NOT NULL,
  `fecha_emision` date NOT NULL,
  `valor` decimal(8,2) NOT NULL,
  `saldo` decimal(20,13) NOT NULL,
  `comentarios` longtext,
  `comentarios_audit` longtext,
  `bg_closed` int NOT NULL,
  `bg_audit` int NOT NULL,
  `bg_isrejected` int NOT NULL,
  `audit_date` datetime(6) DEFAULT NULL,
  `audit_user` smallint DEFAULT NULL,
  `tipo` varchar(8) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  PRIMARY KEY (`id_documento_pago`),
  UNIQUE KEY `documento_pago_identificacion_proveedor_b8046270_uniq` (`identificacion_proveedor`,`nro_factura`),
  CONSTRAINT `documento_pago_identificacion_prove_a90f391c_fk_proveedor` FOREIGN KEY (`identificacion_proveedor`) REFERENCES `proveedor` (`identificacion_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documento_pago`
--

LOCK TABLES `documento_pago` WRITE;
/*!40000 ALTER TABLE `documento_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `documento_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura_informativa`
--

DROP TABLE IF EXISTS `factura_informativa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura_informativa` (
  `id_factura_informativa` int NOT NULL AUTO_INCREMENT,
  `nro_factura_informativa` varchar(8) NOT NULL,
  `fecha_emision` date NOT NULL,
  `flete_aduana` decimal(20,13) NOT NULL,
  `seguro_aduana` decimal(20,13) NOT NULL,
  `valor` decimal(20,13) DEFAULT NULL,
  `moneda` varchar(45) NOT NULL,
  `nro_refrendo` varchar(22) DEFAULT NULL,
  `tipo_cambio` decimal(20,13) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `comentarios_audit` longtext,
  `bg_isclosed` int NOT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `bg_gst_origen_por_factura` int NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_parcial` int NOT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  PRIMARY KEY (`id_factura_informativa`),
  UNIQUE KEY `nro_factura_informativa` (`nro_factura_informativa`),
  KEY `factura_informativa_id_parcial_618ee455_fk_parcial_id_parcial` (`id_parcial`),
  KEY `factura_informativa_identificacion_prove_733aa548_fk_proveedor` (`identificacion_proveedor`),
  CONSTRAINT `factura_informativa_id_parcial_618ee455_fk_parcial_id_parcial` FOREIGN KEY (`id_parcial`) REFERENCES `parcial` (`id_parcial`),
  CONSTRAINT `factura_informativa_identificacion_prove_733aa548_fk_proveedor` FOREIGN KEY (`identificacion_proveedor`) REFERENCES `proveedor` (`identificacion_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura_informativa`
--

LOCK TABLES `factura_informativa` WRITE;
/*!40000 ALTER TABLE `factura_informativa` DISABLE KEYS */;
/*!40000 ALTER TABLE `factura_informativa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factura_informativa_detalle`
--

DROP TABLE IF EXISTS `factura_informativa_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factura_informativa_detalle` (
  `id_factura_informativa_detalle` int NOT NULL AUTO_INCREMENT,
  `arancel_advalorem` decimal(20,13) NOT NULL,
  `arancel_advalorem_liberado` decimal(20,13) NOT NULL,
  `arancel_advalorem_pagar` decimal(20,13) NOT NULL,
  `arancel_advalorem_unitario` decimal(20,13) NOT NULL,
  `arancel_especifico` decimal(20,13) NOT NULL,
  `arancel_especifico_liberado` decimal(20,13) NOT NULL,
  `arancel_especifico_pagar` decimal(20,13) NOT NULL,
  `arancel_especifico_unitario` decimal(20,13) NOT NULL,
  `base_advalorem` decimal(20,13) NOT NULL,
  `base_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `base_ice_epecifico` decimal(20,13) NOT NULL,
  `cajas_importadas` decimal(20,13) NOT NULL,
  `capacidad_ml` decimal(20,13) NOT NULL,
  `cif` decimal(20,13) NOT NULL,
  `cod_contable` varchar(20) DEFAULT NULL,
  `costo_botella` decimal(20,13) NOT NULL,
  `costo_caja` decimal(20,13) NOT NULL,
  `costo_caja_final` decimal(20,13) NOT NULL,
  `costo_total` decimal(20,13) NOT NULL,
  `costo_unidad` decimal(20,13) NOT NULL,
  `etiquetas_fiscales` decimal(20,13) NOT NULL,
  `ex_aduana` decimal(20,13) NOT NULL,
  `ex_aduana_unitario` decimal(20,13) NOT NULL,
  `ex_aduana_antes` decimal(20,13) NOT NULL,
  `ex_aduana_antes_unitario` decimal(20,13) NOT NULL,
  `exaduana_sin_etiquetas` decimal(20,13) NOT NULL,
  `exaduana_sin_tasa` decimal(20,13) NOT NULL,
  `flete` decimal(20,13) NOT NULL,
  `flete_aduana` decimal(20,13) NOT NULL,
  `fob` decimal(20,13) NOT NULL,
  `fob_tasa_trimestral` decimal(20,13) NOT NULL,
  `fob_percent` decimal(20,13) NOT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `fodinfa` decimal(20,13) NOT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `gasto_origen_tasa_trimestral` decimal(20,13) NOT NULL,
  `grado_alcoholico` decimal(12,5) NOT NULL,
  `ice_advalorem` decimal(20,13) NOT NULL,
  `ice_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `ice_advalorem_diferencia` decimal(20,13) NOT NULL,
  `ice_advalorem_pagado` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_etiquetas` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_tasa` decimal(20,13) NOT NULL,
  `ice_advalorem_unitario` decimal(20,13) NOT NULL,
  `ice_especifico` decimal(20,13) NOT NULL,
  `ice_especifico_unitario` decimal(20,13) NOT NULL,
  `ice_unitario` decimal(20,13) NOT NULL,
  `id_parcial` decimal(20,13) NOT NULL,
  `indirectos` decimal(20,13) NOT NULL,
  `iva` decimal(20,13) NOT NULL,
  `iva_total` decimal(20,13) NOT NULL,
  `iva_unidad` decimal(20,13) NOT NULL,
  `nro_cajas` decimal(20,13) NOT NULL,
  `nro_factura_informativa` varchar(10) DEFAULT NULL,
  `nro_pedido` varchar(10) DEFAULT NULL,
  `otros` decimal(20,13) NOT NULL,
  `peso` decimal(20,13) NOT NULL,
  `product` varchar(200) DEFAULT NULL,
  `prorrateo_parcial` decimal(20,13) NOT NULL,
  `prorrateo_pedido` decimal(20,13) NOT NULL,
  `prorrateos_total` decimal(20,13) NOT NULL,
  `seguro` decimal(20,13) NOT NULL,
  `seguro_aduana` decimal(20,13) NOT NULL,
  `tasa_control` decimal(20,13) NOT NULL,
  `total_ice` decimal(20,13) NOT NULL,
  `unidades` decimal(20,13) NOT NULL,
  `unidades_importadas` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `detalle_pedido_factura` int NOT NULL,
  `id_factura_informativa` int NOT NULL,
  `cantidad_x_caja` decimal(12,3) DEFAULT NULL,
  PRIMARY KEY (`id_factura_informativa_detalle`),
  UNIQUE KEY `factura_informativa_deta_id_factura_informativa_d_4d61c5bd_uniq` (`id_factura_informativa`,`detalle_pedido_factura`,`date_create`),
  KEY `factura_informativa__detalle_pedido_factu_9c9f8ab7_fk_detalle_p` (`detalle_pedido_factura`),
  CONSTRAINT `factura_informativa__detalle_pedido_factu_9c9f8ab7_fk_detalle_p` FOREIGN KEY (`detalle_pedido_factura`) REFERENCES `detalle_pedido_factura` (`detalle_pedido_factura`),
  CONSTRAINT `factura_informativa__id_factura_informati_fcf8988a_fk_factura_i` FOREIGN KEY (`id_factura_informativa`) REFERENCES `factura_informativa` (`id_factura_informativa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factura_informativa_detalle`
--

LOCK TABLES `factura_informativa_detalle` WRITE;
/*!40000 ALTER TABLE `factura_informativa_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `factura_informativa_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `facturas_proveedor_pendientes`
--

DROP TABLE IF EXISTS `facturas_proveedor_pendientes`;
/*!50001 DROP VIEW IF EXISTS `facturas_proveedor_pendientes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `facturas_proveedor_pendientes` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `id_factura_proveedor`,
 1 AS `valor`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `filemanager_historicalfilemanager`
--

DROP TABLE IF EXISTS `filemanager_historicalfilemanager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `filemanager_historicalfilemanager` (
  `id_archivo` int NOT NULL,
  `id_registro` varchar(10) NOT NULL,
  `archivo` longtext NOT NULL,
  `nombre_fichero` varchar(125) NOT NULL,
  `observaciones` longtext,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `bg_isvalid` tinyint(1) NOT NULL,
  `bg_isvisible` tinyint(1) NOT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `model` int DEFAULT NULL,
  `usuario_id` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `filemanager_historic_history_user_id_5269fdc9_fk_auth_user` (`history_user_id`),
  KEY `filemanager_historicalfilemanager_id_archivo_33ba031d` (`id_archivo`),
  KEY `filemanager_historicalfilemanager_model_4fbbcf60` (`model`),
  KEY `filemanager_historicalfilemanager_usuario_id_24017f18` (`usuario_id`),
  CONSTRAINT `filemanager_historic_history_user_id_5269fdc9_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filemanager_historicalfilemanager`
--

LOCK TABLES `filemanager_historicalfilemanager` WRITE;
/*!40000 ALTER TABLE `filemanager_historicalfilemanager` DISABLE KEYS */;
/*!40000 ALTER TABLE `filemanager_historicalfilemanager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gastos_nacionalizacion`
--

DROP TABLE IF EXISTS `gastos_nacionalizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gastos_nacionalizacion` (
  `id_gastos_nacionalizacion` int NOT NULL AUTO_INCREMENT,
  `id_parcial` smallint unsigned NOT NULL,
  `concepto` varchar(45) NOT NULL,
  `tipo` varchar(15) DEFAULT NULL,
  `valor_provisionado` decimal(8,2) NOT NULL,
  `valor_ajuste` decimal(8,2) NOT NULL,
  `fecha` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `comentarios` longtext,
  `bg_closed` int NOT NULL,
  `bg_is_visible_gi` int NOT NULL,
  `bg_iscontabilizado` int NOT NULL,
  `bg_iscontabilizado_por` int DEFAULT NULL,
  `bg_isdrop` tinyint(1) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  `nro_pedido` varchar(6) NOT NULL,
  PRIMARY KEY (`id_gastos_nacionalizacion`),
  UNIQUE KEY `gastos_nacionalizacion_nro_pedido_id_parcial_co_9eee637b_uniq` (`nro_pedido`,`id_parcial`,`concepto`),
  KEY `gastos_nacionalizaci_identificacion_prove_6bd4953e_fk_proveedor` (`identificacion_proveedor`),
  CONSTRAINT `gastos_nacionalizaci_identificacion_prove_6bd4953e_fk_proveedor` FOREIGN KEY (`identificacion_proveedor`) REFERENCES `proveedor` (`identificacion_proveedor`),
  CONSTRAINT `gastos_nacionalizacion_nro_pedido_ba138890_fk_pedido_nro_pedido` FOREIGN KEY (`nro_pedido`) REFERENCES `pedido` (`nro_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gastos_nacionalizacion`
--

LOCK TABLES `gastos_nacionalizacion` WRITE;
/*!40000 ALTER TABLE `gastos_nacionalizacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `gastos_nacionalizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestor_archivos`
--

DROP TABLE IF EXISTS `gestor_archivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestor_archivos` (
  `id_archivo` int NOT NULL AUTO_INCREMENT,
  `id_registro` varchar(10) NOT NULL,
  `archivo` varchar(100) NOT NULL,
  `nombre_fichero` varchar(125) NOT NULL,
  `observaciones` longtext,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `bg_isvalid` tinyint(1) NOT NULL,
  `bg_isvisible` tinyint(1) NOT NULL,
  `model` int NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id_archivo`),
  KEY `gestor_archivos_model_49129248_fk_django_content_type_id` (`model`),
  KEY `gestor_archivos_usuario_id_cda21c7b_fk_auth_user_id` (`usuario_id`),
  CONSTRAINT `gestor_archivos_model_49129248_fk_django_content_type_id` FOREIGN KEY (`model`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `gestor_archivos_usuario_id_cda21c7b_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestor_archivos`
--

LOCK TABLES `gestor_archivos` WRITE;
/*!40000 ALTER TABLE `gestor_archivos` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestor_archivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guardian_groupobjectpermission`
--

DROP TABLE IF EXISTS `guardian_groupobjectpermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardian_groupobjectpermission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `object_pk` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `guardian_groupobjectperm_group_id_permission_id_o_3f189f7c_uniq` (`group_id`,`permission_id`,`object_pk`),
  KEY `guardian_groupobject_content_type_id_7ade36b8_fk_django_co` (`content_type_id`),
  KEY `guardian_groupobject_permission_id_36572738_fk_auth_perm` (`permission_id`),
  CONSTRAINT `guardian_groupobject_content_type_id_7ade36b8_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `guardian_groupobject_group_id_4bbbfb62_fk_auth_grou` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `guardian_groupobject_permission_id_36572738_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardian_groupobjectpermission`
--

LOCK TABLES `guardian_groupobjectpermission` WRITE;
/*!40000 ALTER TABLE `guardian_groupobjectpermission` DISABLE KEYS */;
/*!40000 ALTER TABLE `guardian_groupobjectpermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guardian_userobjectpermission`
--

DROP TABLE IF EXISTS `guardian_userobjectpermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardian_userobjectpermission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `object_pk` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `permission_id` int NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `guardian_userobjectpermi_user_id_permission_id_ob_b0b3d2fc_uniq` (`user_id`,`permission_id`,`object_pk`),
  KEY `guardian_userobjectp_content_type_id_2e892405_fk_django_co` (`content_type_id`),
  KEY `guardian_userobjectp_permission_id_71807bfc_fk_auth_perm` (`permission_id`),
  CONSTRAINT `guardian_userobjectp_content_type_id_2e892405_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `guardian_userobjectp_permission_id_71807bfc_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `guardian_userobjectpermission_user_id_d5c1e964_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardian_userobjectpermission`
--

LOCK TABLES `guardian_userobjectpermission` WRITE;
/*!40000 ALTER TABLE `guardian_userobjectpermission` DISABLE KEYS */;
/*!40000 ALTER TABLE `guardian_userobjectpermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `llegadas_almagro`
--

DROP TABLE IF EXISTS `llegadas_almagro`;
/*!50001 DROP VIEW IF EXISTS `llegadas_almagro`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `llegadas_almagro` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `cod_ice`,
 1 AS `fecha_ingreso_almacenera`,
 1 AS `pais_origen`,
 1 AS `nro_cajas`,
 1 AS `unidades`,
 1 AS `fob`,
 1 AS `Name_exp_9`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `ex_aduana_unitario`,
 1 AS `ice_especifico_unitario`,
 1 AS `ice_advalorem_unitario`,
 1 AS `ice_unitario`,
 1 AS `total_ice`,
 1 AS `costo_total`,
 1 AS `costo_caja_final`,
 1 AS `digitos`,
 1 AS `anio`,
 1 AS `reg`,
 1 AS `cons`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `llegadas_pendientes_almagro`
--

DROP TABLE IF EXISTS `llegadas_pendientes_almagro`;
/*!50001 DROP VIEW IF EXISTS `llegadas_pendientes_almagro`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `llegadas_pendientes_almagro` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `fecha_liquidacion`,
 1 AS `nro_factura_informativa`,
 1 AS `nro_refrendo`,
 1 AS `fecha_llegada_cliente`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `mayor`
--

DROP TABLE IF EXISTS `mayor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mayor` (
  `id_mayor` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) NOT NULL,
  `id_parcial` smallint unsigned NOT NULL,
  `costo_inicial_producto` decimal(20,13) NOT NULL,
  `costo_producto` decimal(20,13) NOT NULL,
  `descargas` decimal(20,13) NOT NULL,
  `saldo_producto` decimal(20,13) NOT NULL,
  `precio_entrega` decimal(20,13) NOT NULL,
  `mayor_sap` decimal(20,13) NOT NULL,
  `provisiones_sap` decimal(20,13) NOT NULL,
  `mayor_sgi` decimal(20,13) NOT NULL,
  `provisiones_sgi` decimal(20,13) NOT NULL,
  `facturas_sgi` decimal(20,13) NOT NULL,
  `reliquidacion_ice` decimal(20,13) NOT NULL,
  `bg_mayor` smallint NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_user` int unsigned DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `nro_pedido` varchar(6) NOT NULL,
  PRIMARY KEY (`id_mayor`),
  UNIQUE KEY `mayor_nro_pedido_id_parcial_tipo_9fb664a4_uniq` (`nro_pedido`,`id_parcial`,`tipo`),
  CONSTRAINT `mayor_nro_pedido_29bbf7b3_fk_pedido_nro_pedido` FOREIGN KEY (`nro_pedido`) REFERENCES `pedido` (`nro_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mayor`
--

LOCK TABLES `mayor` WRITE;
/*!40000 ALTER TABLE `mayor` DISABLE KEYS */;
/*!40000 ALTER TABLE `mayor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migracion`
--

DROP TABLE IF EXISTS `migracion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `migracion` (
  `nro_pedido` varchar(6) NOT NULL,
  `import_status` varchar(10) NOT NULL,
  `seguro_aduana` decimal(10,3) NOT NULL,
  `flete_aduana` decimal(10,3) NOT NULL,
  `pais_origen` varchar(50) NOT NULL,
  `ciudad_origen` varchar(50) NOT NULL,
  `moneda` varchar(25) NOT NULL,
  `tipo_cambio` decimal(10,3) NOT NULL,
  `proveedor` varchar(150) NOT NULL,
  `identificacion_proveedor` varchar(15) DEFAULT NULL,
  `id_factura_proveedor` varchar(45) DEFAULT NULL,
  `identificacion_proveedor_factura` varchar(15) DEFAULT NULL,
  `fecha_emision_factura` datetime(6) DEFAULT NULL,
  `fecha_vencimiento_factura` datetime(6) DEFAULT NULL,
  `valor_factura` decimal(12,3) DEFAULT NULL,
  `observaciones_pedido` varchar(300) DEFAULT NULL,
  `observaciones_proveedor` varchar(300) DEFAULT NULL,
  `observaciones_factura` varchar(300) DEFAULT NULL,
  `regimen` varchar(2) DEFAULT NULL,
  `incoterm` varchar(3) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `fecha_importacion` datetime(6) DEFAULT NULL,
  `bg_have_invoice` int NOT NULL,
  `bg_have_order_items` int NOT NULL,
  `bg_have_supplier` int NOT NULL,
  `bg_have_invoice_items` int NOT NULL,
  `bg_exist_in_local` int NOT NULL,
  `bg_supplier_exist_in_local` int NOT NULL,
  `bg_has_imported` int NOT NULL,
  `bg_log` longtext,
  `bg_migrated_order` int NOT NULL,
  `bg_migrated_order_detail` int NOT NULL,
  `bg_migrated_order_invoice` int NOT NULL,
  `bg_migrated_order_invoice_detail` int NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `gasto_origen` decimal(11,3) DEFAULT NULL,
  `docentry` int DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`nro_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migracion`
--

LOCK TABLES `migracion` WRITE;
/*!40000 ALTER TABLE `migracion` DISABLE KEYS */;
/*!40000 ALTER TABLE `migracion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migracion_detalle`
--

DROP TABLE IF EXISTS `migracion_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `migracion_detalle` (
  `id_migracion_detalle` int NOT NULL AUTO_INCREMENT,
  `cod_contable` varchar(20) NOT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  `cod_ice` varchar(39) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `nro_cajas` int DEFAULT NULL,
  `capacidad_ml` smallint NOT NULL,
  `cantidad_x_caja` smallint NOT NULL,
  `grado_alcoholico` double NOT NULL,
  `costo_caja` decimal(16,10) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `bg_product_exist_in_local` int NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `nro_pedido` varchar(6) NOT NULL,
  PRIMARY KEY (`id_migracion_detalle`),
  KEY `migracion_detalle_nro_pedido_764ad4a0_fk_migracion_nro_pedido` (`nro_pedido`),
  CONSTRAINT `migracion_detalle_nro_pedido_764ad4a0_fk_migracion_nro_pedido` FOREIGN KEY (`nro_pedido`) REFERENCES `migracion` (`nro_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migracion_detalle`
--

LOCK TABLES `migracion_detalle` WRITE;
/*!40000 ALTER TABLE `migracion_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `migracion_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrationSAP_historicalmigrations`
--

DROP TABLE IF EXISTS `migrationSAP_historicalmigrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `migrationSAP_historicalmigrations` (
  `nro_pedido` varchar(6) NOT NULL,
  `import_status` varchar(10) NOT NULL,
  `seguro_aduana` decimal(10,3) NOT NULL,
  `flete_aduana` decimal(10,3) NOT NULL,
  `pais_origen` varchar(50) NOT NULL,
  `ciudad_origen` varchar(50) NOT NULL,
  `moneda` varchar(25) NOT NULL,
  `tipo_cambio` decimal(10,3) NOT NULL,
  `proveedor` varchar(150) NOT NULL,
  `identificacion_proveedor` varchar(15) DEFAULT NULL,
  `id_factura_proveedor` varchar(45) DEFAULT NULL,
  `identificacion_proveedor_factura` varchar(15) DEFAULT NULL,
  `fecha_emision_factura` datetime(6) DEFAULT NULL,
  `fecha_vencimiento_factura` datetime(6) DEFAULT NULL,
  `valor_factura` decimal(12,3) DEFAULT NULL,
  `observaciones_pedido` varchar(300) DEFAULT NULL,
  `observaciones_proveedor` varchar(300) DEFAULT NULL,
  `observaciones_factura` varchar(300) DEFAULT NULL,
  `regimen` varchar(2) DEFAULT NULL,
  `incoterm` varchar(3) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `fecha_importacion` datetime(6) DEFAULT NULL,
  `bg_have_invoice` int NOT NULL,
  `bg_have_order_items` int NOT NULL,
  `bg_have_supplier` int NOT NULL,
  `bg_have_invoice_items` int NOT NULL,
  `bg_exist_in_local` int NOT NULL,
  `bg_supplier_exist_in_local` int NOT NULL,
  `bg_has_imported` int NOT NULL,
  `bg_log` longtext,
  `bg_migrated_order` int NOT NULL,
  `bg_migrated_order_detail` int NOT NULL,
  `bg_migrated_order_invoice` int NOT NULL,
  `bg_migrated_order_invoice_detail` int NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `gasto_origen` decimal(11,3) DEFAULT NULL,
  `docentry` int DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `migrationSAP_histori_history_user_id_d7df9d5d_fk_auth_user` (`history_user_id`),
  KEY `migrationSAP_historicalmigrations_nro_pedido_0b4836ed` (`nro_pedido`),
  CONSTRAINT `migrationSAP_histori_history_user_id_d7df9d5d_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrationSAP_historicalmigrations`
--

LOCK TABLES `migrationSAP_historicalmigrations` WRITE;
/*!40000 ALTER TABLE `migrationSAP_historicalmigrations` DISABLE KEYS */;
/*!40000 ALTER TABLE `migrationSAP_historicalmigrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migrationSAP_historicalmigrationsdetail`
--

DROP TABLE IF EXISTS `migrationSAP_historicalmigrationsdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `migrationSAP_historicalmigrationsdetail` (
  `id_migracion_detalle` int NOT NULL,
  `cod_contable` varchar(20) NOT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  `cod_ice` varchar(39) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `nro_cajas` int DEFAULT NULL,
  `capacidad_ml` smallint NOT NULL,
  `cantidad_x_caja` smallint NOT NULL,
  `grado_alcoholico` double NOT NULL,
  `costo_caja` decimal(16,10) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `bg_product_exist_in_local` int NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `nro_pedido` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `migrationSAP_histori_history_user_id_7bc0f957_fk_auth_user` (`history_user_id`),
  KEY `migrationSAP_historicalmigr_id_migracion_detalle_f2de6b63` (`id_migracion_detalle`),
  KEY `migrationSAP_historicalmigrationsdetail_nro_pedido_d0dd492b` (`nro_pedido`),
  CONSTRAINT `migrationSAP_histori_history_user_id_7bc0f957_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migrationSAP_historicalmigrationsdetail`
--

LOCK TABLES `migrationSAP_historicalmigrationsdetail` WRITE;
/*!40000 ALTER TABLE `migrationSAP_historicalmigrationsdetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `migrationSAP_historicalmigrationsdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_historicalorder`
--

DROP TABLE IF EXISTS `orders_historicalorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_historicalorder` (
  `nro_pedido` varchar(6) NOT NULL,
  `regimen` varchar(2) NOT NULL,
  `flete_aduana` decimal(10,4) NOT NULL,
  `seguro_aduana` decimal(10,4) NOT NULL,
  `incoterm` varchar(4) NOT NULL,
  `pais_origen` varchar(45) DEFAULT NULL,
  `ciudad_origen` varchar(45) DEFAULT NULL,
  `fecha_embarque` date DEFAULT NULL,
  `agente_embarque_forwarder` varchar(70) DEFAULT NULL,
  `tipo_carga` varchar(45) DEFAULT NULL,
  `tipo_flete` varchar(70) DEFAULT NULL,
  `peso_carga` int unsigned DEFAULT NULL,
  `volumen_carga_cbm` int unsigned DEFAULT NULL,
  `nro_seguimiento_formarder` varchar(50) DEFAULT NULL,
  `fecha_arribo` date DEFAULT NULL,
  `dias_libres` int unsigned NOT NULL,
  `fecha_salida_bodega_puerto` date DEFAULT NULL,
  `fecha_ingreso_almacenera` date DEFAULT NULL,
  `fecha_salida_almacenera` date DEFAULT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `fecha_llegada_cliente` date DEFAULT NULL,
  `fecha_salida_autorizada_puerto` datetime(6) DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `fecha_salida_origen` date DEFAULT NULL,
  `fecha_declaracion_inicial` date DEFAULT NULL,
  `fecha_ingreso_puerta` date DEFAULT NULL,
  `fecha_movilizacion_contenedor` date DEFAULT NULL,
  `fecha_envio_documentos` date DEFAULT NULL,
  `fecha_entrega_etiquetas_senae` date DEFAULT NULL,
  `fecha_pegado_etiquetas` date DEFAULT NULL,
  `fecha_aforo` date DEFAULT NULL,
  `fecha_envio_de_documentos` date DEFAULT NULL,
  `fecha_aprovacion_compra` date DEFAULT NULL,
  `fecha_llegada_documentos` date DEFAULT NULL,
  `fecha_aprovacion_dai` date DEFAULT NULL,
  `fecha_emision_bl` date DEFAULT NULL,
  `otros` decimal(8,3) DEFAULT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `observaciones` varchar(500) DEFAULT NULL,
  `nro_refrendo` varchar(22) DEFAULT NULL,
  `nro_aplicacion` varchar(8) DEFAULT NULL,
  `nro_poliza` varchar(8) DEFAULT NULL,
  `tipo_cambio_impuestosR10` decimal(14,12) DEFAULT NULL,
  `tipo_cambio_almaceneraR70` decimal(14,12) DEFAULT NULL,
  `exoneracion_arancel` decimal(8,2) DEFAULT NULL,
  `nro_liquidacion` varchar(12) DEFAULT NULL,
  `fodinfa` decimal(10,3) DEFAULT NULL,
  `fodinfa_pagado` decimal(10,3) DEFAULT NULL,
  `ice_advalorem` decimal(10,3) DEFAULT NULL,
  `ice_advalorem_reliquidado` decimal(12,3) DEFAULT NULL,
  `ice_advalorem_pagado` decimal(10,3) DEFAULT NULL,
  `ice_especifico` decimal(10,3) DEFAULT NULL,
  `ice_especifico_pagado` decimal(10,3) DEFAULT NULL,
  `iva` decimal(10,3) DEFAULT NULL,
  `iva_pagado` decimal(10,3) DEFAULT NULL,
  `arancel_especifico_pagar` decimal(16,3) DEFAULT NULL,
  `arancel_especifico_pagar_pagado` decimal(16,3) DEFAULT NULL,
  `arancel_advalorem_pagar` decimal(16,3) DEFAULT NULL,
  `arancel_advalorem_pagar_pagado` decimal(16,0) DEFAULT NULL,
  `liquidacion_con_tasa` int DEFAULT NULL,
  `base_arancel_advalorem` decimal(16,3) DEFAULT NULL,
  `base_arancel_especifico` decimal(16,3) DEFAULT NULL,
  `base_ice_especifico` decimal(16,3) DEFAULT NULL,
  `base_ice_advalorem` decimal(16,3) DEFAULT NULL,
  `porcentaje_ice_advalorem` decimal(16,3) DEFAULT NULL,
  `base_iva` decimal(16,3) DEFAULT NULL,
  `base_fodinfa` decimal(16,3) DEFAULT NULL,
  `base_etiquetas` decimal(16,3) DEFAULT NULL,
  `tipo_cambio_go` decimal(12,2) DEFAULT NULL,
  `id_user_cierre` smallint unsigned DEFAULT NULL,
  `gasto_origen` decimal(16,3) DEFAULT NULL,
  `notas_cierre` varchar(200) DEFAULT NULL,
  `bg_have_close_parcial` int DEFAULT NULL,
  `docentry` int DEFAULT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `url_dai_1` varchar(600) DEFAULT NULL,
  `url_dai_2` varchar(600) DEFAULT NULL,
  `url_dai_3` varchar(600) DEFAULT NULL,
  `path_dai_1` longtext,
  `path_dai_2` longtext,
  `path_dai_3` longtext,
  `url_liquidacion_1` varchar(600) DEFAULT NULL,
  `url_liquidacion_2` varchar(600) DEFAULT NULL,
  `url_liquidacion_3` varchar(600) DEFAULT NULL,
  `tipo_aforo` varchar(50) DEFAULT NULL,
  `estado_senae` varchar(50) DEFAULT NULL,
  `estado_embarque` varchar(70) DEFAULT NULL,
  `nro_proforma` varchar(25) NOT NULL,
  `path_liquidacion_1` longtext,
  `path_liquidacion_2` longtext,
  `path_liquidacion_3` longtext,
  `nro_bl` varchar(70) DEFAULT NULL,
  `nro_hbl_awb` varchar(70) DEFAULT NULL,
  `puerto_destino` varchar(70) DEFAULT NULL,
  `nro_matricula` varchar(11) DEFAULT NULL,
  `numero_de_carga_mrn` varchar(30) DEFAULT NULL,
  `embarcador` varchar(70) DEFAULT NULL,
  `agente_aduana` varchar(100) DEFAULT NULL,
  `ruc_agente_aduana` varchar(13) DEFAULT NULL,
  `punto_lledada` varchar(60) DEFAULT NULL,
  `etiquetas_pegadas` int DEFAULT NULL,
  `bg_have_tasa_control` int DEFAULT NULL,
  `bg_isliquidated` int DEFAULT NULL,
  `bg_isclosed` int DEFAULT NULL,
  `bg_haveExpenses` int DEFAULT NULL,
  `have_etiquetas_fiscales` int DEFAULT NULL,
  `bg_is_tracked` tinyint(1) DEFAULT NULL,
  `bg_is_closed_checked` tinyint(1) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `saldo_mayor` decimal(10,3) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_pedido` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `orders_historicalorder_history_user_id_30fb2c8b_fk_auth_user_id` (`history_user_id`),
  KEY `orders_historicalorder_nro_pedido_d8ef898c` (`nro_pedido`),
  CONSTRAINT `orders_historicalorder_history_user_id_30fb2c8b_fk_auth_user_id` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_historicalorder`
--

LOCK TABLES `orders_historicalorder` WRITE;
/*!40000 ALTER TABLE `orders_historicalorder` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_historicalorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_historicalorderinvoice`
--

DROP TABLE IF EXISTS `orders_historicalorderinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_historicalorderinvoice` (
  `id_pedido_factura` int NOT NULL,
  `id_factura_proveedor` varchar(16) NOT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `fecha_emision` date DEFAULT NULL,
  `valor` decimal(20,13) DEFAULT NULL,
  `fob_tasa_trimestral` decimal(20,13) DEFAULT NULL,
  `moneda` varchar(45) NOT NULL,
  `tipo_cambio` decimal(20,13) NOT NULL,
  `vencimiento_pago` date DEFAULT NULL,
  `fecha_pago` date DEFAULT NULL,
  `id_user` smallint DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `bg_isclosed` int DEFAULT NULL,
  `bg_audit` int NOT NULL,
  `bg_isrejected` int NOT NULL,
  `audit_date` datetime(6) DEFAULT NULL,
  `audit_user` smallint DEFAULT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `gasto_origen_tasa_trimestral` decimal(20,13) DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `identificacion_proveedor` varchar(16) DEFAULT NULL,
  `nro_pedido` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `orders_historicalord_history_user_id_f544ae1f_fk_auth_user` (`history_user_id`),
  KEY `orders_historicalorderinvoice_id_pedido_factura_402ff2a3` (`id_pedido_factura`),
  KEY `orders_historicalorderinvoice_identificacion_proveedor_7462e7a6` (`identificacion_proveedor`),
  KEY `orders_historicalorderinvoice_nro_pedido_32e5d0b6` (`nro_pedido`),
  CONSTRAINT `orders_historicalord_history_user_id_f544ae1f_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_historicalorderinvoice`
--

LOCK TABLES `orders_historicalorderinvoice` WRITE;
/*!40000 ALTER TABLE `orders_historicalorderinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_historicalorderinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders_historicalorderinvoicedetail`
--

DROP TABLE IF EXISTS `orders_historicalorderinvoicedetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders_historicalorderinvoicedetail` (
  `detalle_pedido_factura` int NOT NULL,
  `arancel_advalorem` decimal(20,13) NOT NULL,
  `arancel_advalorem_liberado` decimal(20,13) NOT NULL,
  `arancel_advalorem_pagar` decimal(20,13) NOT NULL,
  `arancel_advalorem_unitario` decimal(20,13) NOT NULL,
  `arancel_especifico` decimal(20,13) NOT NULL,
  `arancel_especifico_liberado` decimal(20,13) NOT NULL,
  `arancel_especifico_pagar` decimal(20,13) NOT NULL,
  `arancel_especifico_unitario` decimal(20,13) NOT NULL,
  `base_advalorem` decimal(20,13) NOT NULL,
  `base_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `base_ice_epecifico` decimal(20,13) NOT NULL,
  `cajas_importadas` decimal(20,13) NOT NULL,
  `cantidad_x_caja` decimal(20,13) NOT NULL,
  `capacidad_ml` decimal(20,13) NOT NULL,
  `cif` decimal(20,13) NOT NULL,
  `costo_botella` decimal(20,13) NOT NULL,
  `costo_caja` decimal(20,13) NOT NULL,
  `costo_caja_final` decimal(20,13) NOT NULL,
  `costo_total` decimal(20,13) NOT NULL,
  `costo_unidad` decimal(20,13) NOT NULL,
  `etiquetas_fiscales` decimal(20,13) NOT NULL,
  `ex_aduana` decimal(20,13) NOT NULL,
  `ex_aduana_unitario` decimal(20,13) NOT NULL,
  `ex_aduana_antes` decimal(20,13) NOT NULL,
  `ex_aduana_antes_unitario` decimal(20,13) NOT NULL,
  `exaduana_sin_etiquetas` decimal(20,13) NOT NULL,
  `exaduana_sin_tasa` decimal(20,13) NOT NULL,
  `flete` decimal(20,13) NOT NULL,
  `flete_aduana` decimal(20,13) NOT NULL,
  `fob` decimal(20,13) NOT NULL,
  `fob_tasa_trimestral` decimal(20,13) NOT NULL,
  `fob_percent` decimal(20,13) NOT NULL,
  `fodinfa` decimal(20,13) NOT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `gasto_origen_tasa_trimestral` decimal(20,13) NOT NULL,
  `grado_alcoholico` double NOT NULL,
  `ice_advalorem` decimal(20,13) NOT NULL,
  `ice_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `ice_advalorem_diferencia` decimal(20,13) NOT NULL,
  `ice_advalorem_pagado` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_etiquetas` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_tasa` decimal(20,13) NOT NULL,
  `ice_advalorem_unitario` decimal(20,13) NOT NULL,
  `ice_especifico` decimal(20,13) NOT NULL,
  `ice_especifico_unitario` decimal(20,13) NOT NULL,
  `ice_unitario` decimal(20,13) NOT NULL,
  `id_parcial` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `indirectos` decimal(20,13) NOT NULL,
  `iva` decimal(20,13) NOT NULL,
  `iva_total` decimal(20,13) NOT NULL,
  `iva_unidad` decimal(20,13) NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `nro_cajas` smallint NOT NULL,
  `nro_factura_informativa` decimal(20,13) NOT NULL,
  `nro_pedido` varchar(10) DEFAULT NULL,
  `otros` decimal(20,13) NOT NULL,
  `peso` decimal(20,13) NOT NULL,
  `product` varchar(200) DEFAULT NULL,
  `prorrateo_parcial` decimal(20,13) NOT NULL,
  `prorrateo_pedido` decimal(20,13) NOT NULL,
  `prorrateos_total` decimal(20,13) NOT NULL,
  `seguro` decimal(20,13) NOT NULL,
  `seguro_aduana` decimal(20,13) NOT NULL,
  `tasa_control` decimal(20,13) NOT NULL,
  `total_ice` decimal(20,13) NOT NULL,
  `unidades` decimal(20,13) NOT NULL,
  `unidades_importadas` decimal(20,13) NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `cod_contable` varchar(20) DEFAULT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_pedido_factura` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `orders_historicalord_history_user_id_4802c37a_fk_auth_user` (`history_user_id`),
  KEY `orders_historicalorderinvoi_detalle_pedido_factura_3ff4a3bf` (`detalle_pedido_factura`),
  KEY `orders_historicalorderinvoicedetail_cod_contable_d770addd` (`cod_contable`),
  KEY `orders_historicalorderinvoicedetail_id_pedido_factura_8a173d6d` (`id_pedido_factura`),
  CONSTRAINT `orders_historicalord_history_user_id_4802c37a_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders_historicalorderinvoicedetail`
--

LOCK TABLES `orders_historicalorderinvoicedetail` WRITE;
/*!40000 ALTER TABLE `orders_historicalorderinvoicedetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `orders_historicalorderinvoicedetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paids_historicalexpense`
--

DROP TABLE IF EXISTS `paids_historicalexpense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paids_historicalexpense` (
  `id_gastos_nacionalizacion` int NOT NULL,
  `id_parcial` smallint unsigned NOT NULL,
  `concepto` varchar(45) NOT NULL,
  `tipo` varchar(15) DEFAULT NULL,
  `valor_provisionado` decimal(8,2) NOT NULL,
  `valor_ajuste` decimal(8,2) NOT NULL,
  `fecha` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `comentarios` longtext,
  `bg_closed` int NOT NULL,
  `bg_is_visible_gi` int NOT NULL,
  `bg_iscontabilizado` int NOT NULL,
  `bg_iscontabilizado_por` int DEFAULT NULL,
  `bg_isdrop` tinyint(1) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `identificacion_proveedor` varchar(16) DEFAULT NULL,
  `nro_pedido` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `paids_historicalexpense_history_user_id_a720fa6e_fk_auth_user_id` (`history_user_id`),
  KEY `paids_historicalexpense_id_gastos_nacionalizacion_574ce82d` (`id_gastos_nacionalizacion`),
  KEY `paids_historicalexpense_identificacion_proveedor_989df2d3` (`identificacion_proveedor`),
  KEY `paids_historicalexpense_nro_pedido_67aaa34b` (`nro_pedido`),
  CONSTRAINT `paids_historicalexpense_history_user_id_a720fa6e_fk_auth_user_id` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paids_historicalexpense`
--

LOCK TABLES `paids_historicalexpense` WRITE;
/*!40000 ALTER TABLE `paids_historicalexpense` DISABLE KEYS */;
/*!40000 ALTER TABLE `paids_historicalexpense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paids_historicalpaidinvoice`
--

DROP TABLE IF EXISTS `paids_historicalpaidinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paids_historicalpaidinvoice` (
  `id_documento_pago` int NOT NULL,
  `nro_factura` varchar(20) NOT NULL,
  `fecha_emision` date NOT NULL,
  `valor` decimal(8,2) NOT NULL,
  `saldo` decimal(20,13) NOT NULL,
  `comentarios` longtext,
  `comentarios_audit` longtext,
  `bg_closed` int NOT NULL,
  `bg_audit` int NOT NULL,
  `bg_isrejected` int NOT NULL,
  `audit_date` datetime(6) DEFAULT NULL,
  `audit_user` smallint DEFAULT NULL,
  `tipo` varchar(8) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `identificacion_proveedor` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `paids_historicalpaid_history_user_id_512830d4_fk_auth_user` (`history_user_id`),
  KEY `paids_historicalpaidinvoice_id_documento_pago_c8deddce` (`id_documento_pago`),
  KEY `paids_historicalpaidinvoice_identificacion_proveedor_de29d1fd` (`identificacion_proveedor`),
  CONSTRAINT `paids_historicalpaid_history_user_id_512830d4_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paids_historicalpaidinvoice`
--

LOCK TABLES `paids_historicalpaidinvoice` WRITE;
/*!40000 ALTER TABLE `paids_historicalpaidinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `paids_historicalpaidinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paids_historicalpaidinvoicedetail`
--

DROP TABLE IF EXISTS `paids_historicalpaidinvoicedetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paids_historicalpaidinvoicedetail` (
  `id_detalle_documento_pago` int NOT NULL,
  `valor` decimal(8,2) NOT NULL,
  `valor_ajuste` decimal(8,2) NOT NULL,
  `bg_closed` int NOT NULL,
  `bg_isnotprovisioned` int NOT NULL,
  `bg_mayor` smallint NOT NULL,
  `id_user` smallint NOT NULL,
  `comentarios` longtext,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_documento_pago` int DEFAULT NULL,
  `id_gastos_nacionalizacion` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `paids_historicalpaid_history_user_id_8396bf95_fk_auth_user` (`history_user_id`),
  KEY `paids_historicalpaidinvoice_id_detalle_documento_pago_5b4b8908` (`id_detalle_documento_pago`),
  KEY `paids_historicalpaidinvoicedetail_id_documento_pago_fa58899f` (`id_documento_pago`),
  KEY `paids_historicalpaidinvoice_id_gastos_nacionalizacion_51dca8e3` (`id_gastos_nacionalizacion`),
  CONSTRAINT `paids_historicalpaid_history_user_id_8396bf95_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paids_historicalpaidinvoicedetail`
--

LOCK TABLES `paids_historicalpaidinvoicedetail` WRITE;
/*!40000 ALTER TABLE `paids_historicalpaidinvoicedetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `paids_historicalpaidinvoicedetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paids_historicalrateexpense`
--

DROP TABLE IF EXISTS `paids_historicalrateexpense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paids_historicalrateexpense` (
  `id_tarifa_gastos` int NOT NULL,
  `regimen` varchar(5) NOT NULL,
  `tipo_gasto` varchar(21) NOT NULL,
  `concepto` varchar(120) NOT NULL,
  `valor` decimal(8,4) NOT NULL,
  `estado` int NOT NULL,
  `pais_origen` varchar(45) NOT NULL,
  `porcentaje` decimal(7,4) NOT NULL,
  `comentarios` varchar(550) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `identificacion_proveedor` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `paids_historicalrate_history_user_id_98203902_fk_auth_user` (`history_user_id`),
  KEY `paids_historicalrateexpense_id_tarifa_gastos_ddb5a070` (`id_tarifa_gastos`),
  KEY `paids_historicalrateexpense_identificacion_proveedor_2505adfe` (`identificacion_proveedor`),
  CONSTRAINT `paids_historicalrate_history_user_id_98203902_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paids_historicalrateexpense`
--

LOCK TABLES `paids_historicalrateexpense` WRITE;
/*!40000 ALTER TABLE `paids_historicalrateexpense` DISABLE KEYS */;
/*!40000 ALTER TABLE `paids_historicalrateexpense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paids_historicalrateincoterm`
--

DROP TABLE IF EXISTS `paids_historicalrateincoterm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paids_historicalrateincoterm` (
  `id_incoterm` int NOT NULL,
  `tipo` varchar(12) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `incoterms` varchar(4) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `tarifa` decimal(8,2) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `paids_historicalrate_history_user_id_f699c7ab_fk_auth_user` (`history_user_id`),
  KEY `paids_historicalrateincoterm_id_incoterm_a3a0619b` (`id_incoterm`),
  CONSTRAINT `paids_historicalrate_history_user_id_f699c7ab_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paids_historicalrateincoterm`
--

LOCK TABLES `paids_historicalrateincoterm` WRITE;
/*!40000 ALTER TABLE `paids_historicalrateincoterm` DISABLE KEYS */;
/*!40000 ALTER TABLE `paids_historicalrateincoterm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parcial`
--

DROP TABLE IF EXISTS `parcial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parcial` (
  `id_parcial` int NOT NULL AUTO_INCREMENT,
  `fecha_nacionalizacion` date DEFAULT NULL,
  `fecha_declaracion_inicial` date DEFAULT NULL,
  `fecha_entrega_etiquetas_senae` date DEFAULT NULL,
  `fecha_pegado_etiquetas` date DEFAULT NULL,
  `fecha_solicitud_salida_almagro` date DEFAULT NULL,
  `fecha_aforo` date DEFAULT NULL,
  `fecha_llegada_documentos` date DEFAULT NULL,
  `fecha_envio_de_documentos` date DEFAULT NULL,
  `fecha_envio_documentos` date DEFAULT NULL,
  `fecha_aprovacion_dai` date DEFAULT NULL,
  `fecha_salida_almacenera` date DEFAULT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `fecha_llegada_cliente` date DEFAULT NULL,
  `fecha_salida_autorizada_almagro` datetime(6) DEFAULT NULL,
  `proximo_almacenaje_desde` date DEFAULT NULL,
  `otros` decimal(8,3) NOT NULL,
  `observaciones` varchar(250) DEFAULT NULL,
  `tipo_cambio` decimal(15,10) NOT NULL,
  `nro_refrendo` varchar(22) DEFAULT NULL,
  `exoneracion_arancel` decimal(8,2) NOT NULL,
  `fodinfa` decimal(10,3) NOT NULL,
  `fodinfa_pagado` decimal(10,3) NOT NULL,
  `ice_advalorem` decimal(10,3) NOT NULL,
  `ice_advalorem_reliquidado` decimal(12,3) NOT NULL,
  `ice_advalorem_pagado` decimal(10,3) NOT NULL,
  `ice_especifico` decimal(10,3) NOT NULL,
  `ice_especifico_pagado` decimal(10,3) NOT NULL,
  `iva` decimal(10,3) NOT NULL,
  `iva_pagado` decimal(10,3) NOT NULL,
  `arancel_advalorem_pagar` decimal(16,3) NOT NULL,
  `arancel_advalorem_pagar_pagado` decimal(16,3) NOT NULL,
  `arancel_especifico_pagar_pagado` decimal(16,3) NOT NULL,
  `arancel_especifico_pagar` decimal(16,3) NOT NULL,
  `base_arancel_advalorem` decimal(16,3) NOT NULL,
  `base_arancel_especifico` decimal(16,3) NOT NULL,
  `base_ice_especifico` decimal(16,3) NOT NULL,
  `base_ice_advalorem` decimal(16,3) NOT NULL,
  `porcentaje_ice_advalorem` decimal(16,3) NOT NULL,
  `base_iva` decimal(16,3) NOT NULL,
  `base_fodinfa` decimal(16,3) NOT NULL,
  `base_etiquetas` decimal(16,8) NOT NULL,
  `nro_liquidacion` varchar(22) DEFAULT NULL,
  `notas_cierre` varchar(200) DEFAULT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `url_dai_1` varchar(600) DEFAULT NULL,
  `url_dai_2` varchar(600) DEFAULT NULL,
  `url_dai_3` varchar(600) DEFAULT NULL,
  `path_dai_1` varchar(600) DEFAULT NULL,
  `path_dai_2` varchar(600) DEFAULT NULL,
  `path_dai_3` varchar(600) DEFAULT NULL,
  `url_liquidacion_1` varchar(600) DEFAULT NULL,
  `url_liquidacion_2` varchar(600) DEFAULT NULL,
  `url_liquidacion_3` varchar(600) DEFAULT NULL,
  `path_liquidacion_1` varchar(600) DEFAULT NULL,
  `path_liquidacion_2` varchar(600) DEFAULT NULL,
  `path_liquidacion_3` varchar(600) DEFAULT NULL,
  `agente_aduana` varchar(100) DEFAULT NULL,
  `ruc_agente_aduana` varchar(13) DEFAULT NULL,
  `etiquetas_pegadas` int DEFAULT NULL,
  `punto_lledada` varchar(60) DEFAULT NULL,
  `liquidacion_con_tasa` int DEFAULT NULL,
  `bg_isclosed` int DEFAULT NULL,
  `bg_have_etiquetas_fiscales` int DEFAULT NULL,
  `tipo_aforo` varchar(50) DEFAULT NULL,
  `estado_senae` varchar(50) DEFAULT NULL,
  `bg_isliquidated` int DEFAULT NULL,
  `bg_have_tasa_control` int DEFAULT NULL,
  `id_user_cierre` smallint unsigned DEFAULT NULL,
  `saldo_mayor` decimal(10,3) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `nro_pedido` varchar(6) NOT NULL,
  PRIMARY KEY (`id_parcial`),
  KEY `parcial_nro_pedido_fd7c0239_fk_pedido_nro_pedido` (`nro_pedido`),
  CONSTRAINT `parcial_nro_pedido_fd7c0239_fk_pedido_nro_pedido` FOREIGN KEY (`nro_pedido`) REFERENCES `pedido` (`nro_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parcial`
--

LOCK TABLES `parcial` WRITE;
/*!40000 ALTER TABLE `parcial` DISABLE KEYS */;
/*!40000 ALTER TABLE `parcial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partials_historicalapportionment`
--

DROP TABLE IF EXISTS `partials_historicalapportionment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partials_historicalapportionment` (
  `id_prorrateo` int NOT NULL,
  `porcentaje_parcial` decimal(20,13) NOT NULL,
  `fob_parcial_razon_inicial` decimal(20,13) NOT NULL,
  `fob_parcial_razon_saldo` decimal(20,13) NOT NULL,
  `fob_proximo_parcial` decimal(20,13) NOT NULL,
  `fob_inicial` decimal(20,13) NOT NULL,
  `fob_saldo` decimal(20,13) NOT NULL,
  `fob_parcial` decimal(20,13) NOT NULL,
  `almacenaje_parcial` decimal(20,13) NOT NULL,
  `almacenaje_anterior` decimal(20,13) NOT NULL,
  `almacenaje_aplicado` decimal(20,13) NOT NULL,
  `almacenaje_proximo_parcial` decimal(20,13) NOT NULL,
  `prorrateo_flete_aduana` decimal(20,13) NOT NULL,
  `prorrateo_seguro_aduana` decimal(20,13) NOT NULL,
  `gastos_drop_parcial` decimal(20,13) NOT NULL,
  `gastos_drop_parcial_anterior` decimal(20,13) NOT NULL,
  `gastos_drop_parcial_aplicado` decimal(20,13) NOT NULL,
  `gastos_drop_parcial_proximo_parcial` decimal(20,13) NOT NULL,
  `gastos_origen_incial` decimal(20,13) NOT NULL,
  `gastos_origen_anterior_parcial` decimal(20,13) NOT NULL,
  `gastos_origen_aplicado` decimal(20,13) NOT NULL,
  `gastos_origen_proximo_parcial` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_parcial` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `partials_historicala_history_user_id_2101795a_fk_auth_user` (`history_user_id`),
  KEY `partials_historicalapportionment_id_prorrateo_4765e7da` (`id_prorrateo`),
  KEY `partials_historicalapportionment_id_parcial_84fea3c9` (`id_parcial`),
  CONSTRAINT `partials_historicala_history_user_id_2101795a_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partials_historicalapportionment`
--

LOCK TABLES `partials_historicalapportionment` WRITE;
/*!40000 ALTER TABLE `partials_historicalapportionment` DISABLE KEYS */;
/*!40000 ALTER TABLE `partials_historicalapportionment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partials_historicalapportionmentdetail`
--

DROP TABLE IF EXISTS `partials_historicalapportionmentdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partials_historicalapportionmentdetail` (
  `id_prorrateo_detalle` int NOT NULL,
  `id_gastos_nacionalizacion` int unsigned NOT NULL,
  `tipo` varchar(13) NOT NULL,
  `concepto` varchar(90) NOT NULL,
  `valor_prorrateado` decimal(20,13) DEFAULT NULL,
  `valor_provisionado` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_prorrateo` int DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `partials_historicala_history_user_id_3d40beca_fk_auth_user` (`history_user_id`),
  KEY `partials_historicalapportio_id_prorrateo_detalle_50304c94` (`id_prorrateo_detalle`),
  KEY `partials_historicalapportionmentdetail_id_prorrateo_6de63a78` (`id_prorrateo`),
  CONSTRAINT `partials_historicala_history_user_id_3d40beca_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partials_historicalapportionmentdetail`
--

LOCK TABLES `partials_historicalapportionmentdetail` WRITE;
/*!40000 ALTER TABLE `partials_historicalapportionmentdetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `partials_historicalapportionmentdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partials_historicalinfoinvoice`
--

DROP TABLE IF EXISTS `partials_historicalinfoinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partials_historicalinfoinvoice` (
  `id_factura_informativa` int NOT NULL,
  `nro_factura_informativa` varchar(8) NOT NULL,
  `fecha_emision` date NOT NULL,
  `flete_aduana` decimal(20,13) NOT NULL,
  `seguro_aduana` decimal(20,13) NOT NULL,
  `valor` decimal(20,13) DEFAULT NULL,
  `moneda` varchar(45) NOT NULL,
  `nro_refrendo` varchar(22) DEFAULT NULL,
  `tipo_cambio` decimal(20,13) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `comentarios_audit` longtext,
  `bg_isclosed` int NOT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `bg_gst_origen_por_factura` int NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_parcial` int DEFAULT NULL,
  `identificacion_proveedor` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `partials_historicali_history_user_id_32ed3a35_fk_auth_user` (`history_user_id`),
  KEY `partials_historicalinfoinvoice_id_factura_informativa_d4f7839c` (`id_factura_informativa`),
  KEY `partials_historicalinfoinvoice_nro_factura_informativa_a809ec95` (`nro_factura_informativa`),
  KEY `partials_historicalinfoinvoice_id_parcial_1655ada8` (`id_parcial`),
  KEY `partials_historicalinfoinvoice_identificacion_proveedor_d1677b6d` (`identificacion_proveedor`),
  CONSTRAINT `partials_historicali_history_user_id_32ed3a35_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partials_historicalinfoinvoice`
--

LOCK TABLES `partials_historicalinfoinvoice` WRITE;
/*!40000 ALTER TABLE `partials_historicalinfoinvoice` DISABLE KEYS */;
/*!40000 ALTER TABLE `partials_historicalinfoinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partials_historicalinfoinvoicedetail`
--

DROP TABLE IF EXISTS `partials_historicalinfoinvoicedetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partials_historicalinfoinvoicedetail` (
  `id_factura_informativa_detalle` int NOT NULL,
  `arancel_advalorem` decimal(20,13) NOT NULL,
  `arancel_advalorem_liberado` decimal(20,13) NOT NULL,
  `arancel_advalorem_pagar` decimal(20,13) NOT NULL,
  `arancel_advalorem_unitario` decimal(20,13) NOT NULL,
  `arancel_especifico` decimal(20,13) NOT NULL,
  `arancel_especifico_liberado` decimal(20,13) NOT NULL,
  `arancel_especifico_pagar` decimal(20,13) NOT NULL,
  `arancel_especifico_unitario` decimal(20,13) NOT NULL,
  `base_advalorem` decimal(20,13) NOT NULL,
  `base_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `base_ice_epecifico` decimal(20,13) NOT NULL,
  `cajas_importadas` decimal(20,13) NOT NULL,
  `capacidad_ml` decimal(20,13) NOT NULL,
  `cif` decimal(20,13) NOT NULL,
  `cod_contable` varchar(20) DEFAULT NULL,
  `costo_botella` decimal(20,13) NOT NULL,
  `costo_caja` decimal(20,13) NOT NULL,
  `costo_caja_final` decimal(20,13) NOT NULL,
  `costo_total` decimal(20,13) NOT NULL,
  `costo_unidad` decimal(20,13) NOT NULL,
  `etiquetas_fiscales` decimal(20,13) NOT NULL,
  `ex_aduana` decimal(20,13) NOT NULL,
  `ex_aduana_unitario` decimal(20,13) NOT NULL,
  `ex_aduana_antes` decimal(20,13) NOT NULL,
  `ex_aduana_antes_unitario` decimal(20,13) NOT NULL,
  `exaduana_sin_etiquetas` decimal(20,13) NOT NULL,
  `exaduana_sin_tasa` decimal(20,13) NOT NULL,
  `flete` decimal(20,13) NOT NULL,
  `flete_aduana` decimal(20,13) NOT NULL,
  `fob` decimal(20,13) NOT NULL,
  `fob_tasa_trimestral` decimal(20,13) NOT NULL,
  `fob_percent` decimal(20,13) NOT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `fodinfa` decimal(20,13) NOT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `gasto_origen_tasa_trimestral` decimal(20,13) NOT NULL,
  `grado_alcoholico` decimal(12,5) NOT NULL,
  `ice_advalorem` decimal(20,13) NOT NULL,
  `ice_advalorem_reliquidado` decimal(20,13) NOT NULL,
  `ice_advalorem_diferencia` decimal(20,13) NOT NULL,
  `ice_advalorem_pagado` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_etiquetas` decimal(20,13) NOT NULL,
  `ice_advalorem_sin_tasa` decimal(20,13) NOT NULL,
  `ice_advalorem_unitario` decimal(20,13) NOT NULL,
  `ice_especifico` decimal(20,13) NOT NULL,
  `ice_especifico_unitario` decimal(20,13) NOT NULL,
  `ice_unitario` decimal(20,13) NOT NULL,
  `id_parcial` decimal(20,13) NOT NULL,
  `indirectos` decimal(20,13) NOT NULL,
  `iva` decimal(20,13) NOT NULL,
  `iva_total` decimal(20,13) NOT NULL,
  `iva_unidad` decimal(20,13) NOT NULL,
  `nro_cajas` decimal(20,13) NOT NULL,
  `nro_factura_informativa` varchar(10) DEFAULT NULL,
  `nro_pedido` varchar(10) DEFAULT NULL,
  `otros` decimal(20,13) NOT NULL,
  `peso` decimal(20,13) NOT NULL,
  `product` varchar(200) DEFAULT NULL,
  `prorrateo_parcial` decimal(20,13) NOT NULL,
  `prorrateo_pedido` decimal(20,13) NOT NULL,
  `prorrateos_total` decimal(20,13) NOT NULL,
  `seguro` decimal(20,13) NOT NULL,
  `seguro_aduana` decimal(20,13) NOT NULL,
  `tasa_control` decimal(20,13) NOT NULL,
  `total_ice` decimal(20,13) NOT NULL,
  `unidades` decimal(20,13) NOT NULL,
  `unidades_importadas` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `detalle_pedido_factura` int DEFAULT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_factura_informativa` int DEFAULT NULL,
  `cantidad_x_caja` decimal(12,3) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `partials_historicali_history_user_id_ff978053_fk_auth_user` (`history_user_id`),
  KEY `partials_historicalinfoinvo_id_factura_informativa_deta_96291f9f` (`id_factura_informativa_detalle`),
  KEY `partials_historicalinfoinvo_detalle_pedido_factura_8987d862` (`detalle_pedido_factura`),
  KEY `partials_historicalinfoinvo_id_factura_informativa_33a03f30` (`id_factura_informativa`),
  CONSTRAINT `partials_historicali_history_user_id_ff978053_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partials_historicalinfoinvoicedetail`
--

LOCK TABLES `partials_historicalinfoinvoicedetail` WRITE;
/*!40000 ALTER TABLE `partials_historicalinfoinvoicedetail` DISABLE KEYS */;
/*!40000 ALTER TABLE `partials_historicalinfoinvoicedetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `partials_historicalpartial`
--

DROP TABLE IF EXISTS `partials_historicalpartial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `partials_historicalpartial` (
  `id_parcial` int NOT NULL,
  `fecha_nacionalizacion` date DEFAULT NULL,
  `fecha_declaracion_inicial` date DEFAULT NULL,
  `fecha_entrega_etiquetas_senae` date DEFAULT NULL,
  `fecha_pegado_etiquetas` date DEFAULT NULL,
  `fecha_solicitud_salida_almagro` date DEFAULT NULL,
  `fecha_aforo` date DEFAULT NULL,
  `fecha_llegada_documentos` date DEFAULT NULL,
  `fecha_envio_de_documentos` date DEFAULT NULL,
  `fecha_envio_documentos` date DEFAULT NULL,
  `fecha_aprovacion_dai` date DEFAULT NULL,
  `fecha_salida_almacenera` date DEFAULT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `fecha_llegada_cliente` date DEFAULT NULL,
  `fecha_salida_autorizada_almagro` datetime(6) DEFAULT NULL,
  `proximo_almacenaje_desde` date DEFAULT NULL,
  `otros` decimal(8,3) NOT NULL,
  `observaciones` varchar(250) DEFAULT NULL,
  `tipo_cambio` decimal(15,10) NOT NULL,
  `nro_refrendo` varchar(22) DEFAULT NULL,
  `exoneracion_arancel` decimal(8,2) NOT NULL,
  `fodinfa` decimal(10,3) NOT NULL,
  `fodinfa_pagado` decimal(10,3) NOT NULL,
  `ice_advalorem` decimal(10,3) NOT NULL,
  `ice_advalorem_reliquidado` decimal(12,3) NOT NULL,
  `ice_advalorem_pagado` decimal(10,3) NOT NULL,
  `ice_especifico` decimal(10,3) NOT NULL,
  `ice_especifico_pagado` decimal(10,3) NOT NULL,
  `iva` decimal(10,3) NOT NULL,
  `iva_pagado` decimal(10,3) NOT NULL,
  `arancel_advalorem_pagar` decimal(16,3) NOT NULL,
  `arancel_advalorem_pagar_pagado` decimal(16,3) NOT NULL,
  `arancel_especifico_pagar_pagado` decimal(16,3) NOT NULL,
  `arancel_especifico_pagar` decimal(16,3) NOT NULL,
  `base_arancel_advalorem` decimal(16,3) NOT NULL,
  `base_arancel_especifico` decimal(16,3) NOT NULL,
  `base_ice_especifico` decimal(16,3) NOT NULL,
  `base_ice_advalorem` decimal(16,3) NOT NULL,
  `porcentaje_ice_advalorem` decimal(16,3) NOT NULL,
  `base_iva` decimal(16,3) NOT NULL,
  `base_fodinfa` decimal(16,3) NOT NULL,
  `base_etiquetas` decimal(16,8) NOT NULL,
  `nro_liquidacion` varchar(22) DEFAULT NULL,
  `notas_cierre` varchar(200) DEFAULT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `url_dai_1` varchar(600) DEFAULT NULL,
  `url_dai_2` varchar(600) DEFAULT NULL,
  `url_dai_3` varchar(600) DEFAULT NULL,
  `path_dai_1` longtext,
  `path_dai_2` longtext,
  `path_dai_3` longtext,
  `url_liquidacion_1` varchar(600) DEFAULT NULL,
  `url_liquidacion_2` varchar(600) DEFAULT NULL,
  `url_liquidacion_3` varchar(600) DEFAULT NULL,
  `path_liquidacion_1` longtext,
  `path_liquidacion_2` longtext,
  `path_liquidacion_3` longtext,
  `agente_aduana` varchar(100) DEFAULT NULL,
  `ruc_agente_aduana` varchar(13) DEFAULT NULL,
  `etiquetas_pegadas` int DEFAULT NULL,
  `punto_lledada` varchar(60) DEFAULT NULL,
  `liquidacion_con_tasa` int DEFAULT NULL,
  `bg_isclosed` int DEFAULT NULL,
  `bg_have_etiquetas_fiscales` int DEFAULT NULL,
  `tipo_aforo` varchar(50) DEFAULT NULL,
  `estado_senae` varchar(50) DEFAULT NULL,
  `bg_isliquidated` int DEFAULT NULL,
  `bg_have_tasa_control` int DEFAULT NULL,
  `id_user_cierre` smallint unsigned DEFAULT NULL,
  `saldo_mayor` decimal(10,3) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `nro_pedido` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `partials_historicalp_history_user_id_7f2039b0_fk_auth_user` (`history_user_id`),
  KEY `partials_historicalpartial_id_parcial_4c740064` (`id_parcial`),
  KEY `partials_historicalpartial_nro_pedido_01208798` (`nro_pedido`),
  CONSTRAINT `partials_historicalp_history_user_id_7f2039b0_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `partials_historicalpartial`
--

LOCK TABLES `partials_historicalpartial` WRITE;
/*!40000 ALTER TABLE `partials_historicalpartial` DISABLE KEYS */;
/*!40000 ALTER TABLE `partials_historicalpartial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `nro_pedido` varchar(6) NOT NULL,
  `regimen` varchar(2) NOT NULL,
  `flete_aduana` decimal(10,4) NOT NULL,
  `seguro_aduana` decimal(10,4) NOT NULL,
  `incoterm` varchar(4) NOT NULL,
  `pais_origen` varchar(45) DEFAULT NULL,
  `ciudad_origen` varchar(45) DEFAULT NULL,
  `fecha_embarque` date DEFAULT NULL,
  `agente_embarque_forwarder` varchar(70) DEFAULT NULL,
  `tipo_carga` varchar(45) DEFAULT NULL,
  `tipo_flete` varchar(70) DEFAULT NULL,
  `peso_carga` int unsigned DEFAULT NULL,
  `volumen_carga_cbm` int unsigned DEFAULT NULL,
  `nro_seguimiento_formarder` varchar(50) DEFAULT NULL,
  `fecha_arribo` date DEFAULT NULL,
  `dias_libres` int unsigned NOT NULL,
  `fecha_salida_bodega_puerto` date DEFAULT NULL,
  `fecha_ingreso_almacenera` date DEFAULT NULL,
  `fecha_salida_almacenera` date DEFAULT NULL,
  `fecha_liquidacion` date DEFAULT NULL,
  `fecha_llegada_cliente` date DEFAULT NULL,
  `fecha_salida_autorizada_puerto` datetime(6) DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `fecha_salida_origen` date DEFAULT NULL,
  `fecha_declaracion_inicial` date DEFAULT NULL,
  `fecha_ingreso_puerta` date DEFAULT NULL,
  `fecha_movilizacion_contenedor` date DEFAULT NULL,
  `fecha_envio_documentos` date DEFAULT NULL,
  `fecha_entrega_etiquetas_senae` date DEFAULT NULL,
  `fecha_pegado_etiquetas` date DEFAULT NULL,
  `fecha_aforo` date DEFAULT NULL,
  `fecha_envio_de_documentos` date DEFAULT NULL,
  `fecha_aprovacion_compra` date DEFAULT NULL,
  `fecha_llegada_documentos` date DEFAULT NULL,
  `fecha_aprovacion_dai` date DEFAULT NULL,
  `fecha_emision_bl` date DEFAULT NULL,
  `otros` decimal(8,3) DEFAULT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `observaciones` varchar(500) DEFAULT NULL,
  `nro_refrendo` varchar(22) DEFAULT NULL,
  `nro_aplicacion` varchar(8) DEFAULT NULL,
  `nro_poliza` varchar(8) DEFAULT NULL,
  `tipo_cambio_impuestosR10` decimal(14,12) DEFAULT NULL,
  `tipo_cambio_almaceneraR70` decimal(14,12) DEFAULT NULL,
  `exoneracion_arancel` decimal(8,2) DEFAULT NULL,
  `nro_liquidacion` varchar(12) DEFAULT NULL,
  `fodinfa` decimal(10,3) DEFAULT NULL,
  `fodinfa_pagado` decimal(10,3) DEFAULT NULL,
  `ice_advalorem` decimal(10,3) DEFAULT NULL,
  `ice_advalorem_reliquidado` decimal(12,3) DEFAULT NULL,
  `ice_advalorem_pagado` decimal(10,3) DEFAULT NULL,
  `ice_especifico` decimal(10,3) DEFAULT NULL,
  `ice_especifico_pagado` decimal(10,3) DEFAULT NULL,
  `iva` decimal(10,3) DEFAULT NULL,
  `iva_pagado` decimal(10,3) DEFAULT NULL,
  `arancel_especifico_pagar` decimal(16,3) DEFAULT NULL,
  `arancel_especifico_pagar_pagado` decimal(16,3) DEFAULT NULL,
  `arancel_advalorem_pagar` decimal(16,3) DEFAULT NULL,
  `arancel_advalorem_pagar_pagado` decimal(16,0) DEFAULT NULL,
  `liquidacion_con_tasa` int DEFAULT NULL,
  `base_arancel_advalorem` decimal(16,3) DEFAULT NULL,
  `base_arancel_especifico` decimal(16,3) DEFAULT NULL,
  `base_ice_especifico` decimal(16,3) DEFAULT NULL,
  `base_ice_advalorem` decimal(16,3) DEFAULT NULL,
  `porcentaje_ice_advalorem` decimal(16,3) DEFAULT NULL,
  `base_iva` decimal(16,3) DEFAULT NULL,
  `base_fodinfa` decimal(16,3) DEFAULT NULL,
  `base_etiquetas` decimal(16,3) DEFAULT NULL,
  `tipo_cambio_go` decimal(12,2) DEFAULT NULL,
  `id_user_cierre` smallint unsigned DEFAULT NULL,
  `gasto_origen` decimal(16,3) DEFAULT NULL,
  `notas_cierre` varchar(200) DEFAULT NULL,
  `bg_have_close_parcial` int DEFAULT NULL,
  `docentry` int DEFAULT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `url_dai_1` varchar(600) DEFAULT NULL,
  `url_dai_2` varchar(600) DEFAULT NULL,
  `url_dai_3` varchar(600) DEFAULT NULL,
  `path_dai_1` varchar(600) DEFAULT NULL,
  `path_dai_2` varchar(600) DEFAULT NULL,
  `path_dai_3` varchar(600) DEFAULT NULL,
  `url_liquidacion_1` varchar(600) DEFAULT NULL,
  `url_liquidacion_2` varchar(600) DEFAULT NULL,
  `url_liquidacion_3` varchar(600) DEFAULT NULL,
  `tipo_aforo` varchar(50) DEFAULT NULL,
  `estado_senae` varchar(50) DEFAULT NULL,
  `estado_embarque` varchar(70) DEFAULT NULL,
  `nro_proforma` varchar(25) NOT NULL,
  `path_liquidacion_1` varchar(600) DEFAULT NULL,
  `path_liquidacion_2` varchar(600) DEFAULT NULL,
  `path_liquidacion_3` varchar(600) DEFAULT NULL,
  `nro_bl` varchar(70) DEFAULT NULL,
  `nro_hbl_awb` varchar(70) DEFAULT NULL,
  `puerto_destino` varchar(70) DEFAULT NULL,
  `nro_matricula` varchar(11) DEFAULT NULL,
  `numero_de_carga_mrn` varchar(30) DEFAULT NULL,
  `embarcador` varchar(70) DEFAULT NULL,
  `agente_aduana` varchar(100) DEFAULT NULL,
  `ruc_agente_aduana` varchar(13) DEFAULT NULL,
  `punto_lledada` varchar(60) DEFAULT NULL,
  `etiquetas_pegadas` int DEFAULT NULL,
  `bg_have_tasa_control` int DEFAULT NULL,
  `bg_isliquidated` int DEFAULT NULL,
  `bg_isclosed` int DEFAULT NULL,
  `bg_haveExpenses` int DEFAULT NULL,
  `have_etiquetas_fiscales` int DEFAULT NULL,
  `bg_is_tracked` tinyint(1) DEFAULT NULL,
  `bg_is_closed_checked` tinyint(1) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `saldo_mayor` decimal(10,3) DEFAULT NULL,
  `id_pedido` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`nro_pedido`),
  UNIQUE KEY `id_pedido` (`id_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido_factura`
--

DROP TABLE IF EXISTS `pedido_factura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido_factura` (
  `id_pedido_factura` int NOT NULL AUTO_INCREMENT,
  `id_factura_proveedor` varchar(16) NOT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `fecha_emision` date DEFAULT NULL,
  `valor` decimal(20,13) DEFAULT NULL,
  `fob_tasa_trimestral` decimal(20,13) DEFAULT NULL,
  `moneda` varchar(45) NOT NULL,
  `tipo_cambio` decimal(20,13) NOT NULL,
  `vencimiento_pago` date DEFAULT NULL,
  `fecha_pago` date DEFAULT NULL,
  `id_user` smallint DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `bg_isclosed` int DEFAULT NULL,
  `bg_audit` int NOT NULL,
  `bg_isrejected` int NOT NULL,
  `audit_date` datetime(6) DEFAULT NULL,
  `audit_user` smallint DEFAULT NULL,
  `gasto_origen` decimal(20,13) NOT NULL,
  `gasto_origen_tasa_trimestral` decimal(20,13) DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  `nro_pedido` varchar(6) NOT NULL,
  PRIMARY KEY (`id_pedido_factura`),
  UNIQUE KEY `pedido_factura_identificacion_proveedor_e574667f_uniq` (`identificacion_proveedor`,`id_factura_proveedor`),
  KEY `pedido_factura_nro_pedido_f50fb333_fk_pedido_nro_pedido` (`nro_pedido`),
  CONSTRAINT `pedido_factura_identificacion_prove_7a119586_fk_proveedor` FOREIGN KEY (`identificacion_proveedor`) REFERENCES `proveedor` (`identificacion_proveedor`),
  CONSTRAINT `pedido_factura_nro_pedido_f50fb333_fk_pedido_nro_pedido` FOREIGN KEY (`nro_pedido`) REFERENCES `pedido` (`nro_pedido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido_factura`
--

LOCK TABLES `pedido_factura` WRITE;
/*!40000 ALTER TABLE `pedido_factura` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido_factura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `cod_contable` varchar(20) NOT NULL,
  `id_producto` int unsigned NOT NULL,
  `nro_registro_sanitario` varchar(25) NOT NULL,
  `fecha_emision_registro` date DEFAULT NULL,
  `fecha_vencimiento_registro` date DEFAULT NULL,
  `estado_registro` varchar(70) DEFAULT NULL,
  `grado_alcoholico` decimal(12,3) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `nombre_extrangero` varchar(120) DEFAULT NULL,
  `partida_arancelaria` varchar(15) DEFAULT NULL,
  `subpartida_arancelaria` varchar(15) DEFAULT NULL,
  `tnan_codigo` varchar(15) DEFAULT NULL,
  `cod_ice` varchar(39) NOT NULL,
  `capacidad_ml` smallint NOT NULL,
  `cantidad_x_caja` smallint NOT NULL,
  `costo_caja` decimal(16,10) NOT NULL,
  `estado` int NOT NULL,
  `custodia_doble` int NOT NULL,
  `peso` decimal(10,3) DEFAULT NULL,
  `pais_origen` varchar(70) DEFAULT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `registro_sanitario` varchar(100) DEFAULT NULL,
  `id_user` smallint DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  PRIMARY KEY (`cod_contable`),
  UNIQUE KEY `id_producto` (`id_producto`),
  UNIQUE KEY `nombre` (`nombre`),
  KEY `producto_identificacion_prove_db278060_fk_proveedor` (`identificacion_proveedor`),
  CONSTRAINT `producto_identificacion_prove_db278060_fk_proveedor` FOREIGN KEY (`identificacion_proveedor`) REFERENCES `proveedor` (`identificacion_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `producto_en_transito`
--

DROP TABLE IF EXISTS `producto_en_transito`;
/*!50001 DROP VIEW IF EXISTS `producto_en_transito`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `producto_en_transito` AS SELECT 
 1 AS `consecutivo`,
 1 AS `anio`,
 1 AS `nro_pedido`,
 1 AS `nro_refrendo`,
 1 AS `nombre`,
 1 AS `fecha_liquidacion`,
 1 AS `bg_isliquidated`,
 1 AS `bg_isclosed`,
 1 AS `fecha_llegada_cliente`,
 1 AS `nro_cajas`,
 1 AS `cantidad_x_caja`,
 1 AS `Unidades`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `producto_parcial_llegado`
--

DROP TABLE IF EXISTS `producto_parcial_llegado`;
/*!50001 DROP VIEW IF EXISTS `producto_parcial_llegado`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `producto_parcial_llegado` AS SELECT 
 1 AS `id_factura_informativa`,
 1 AS `nro_pedido`,
 1 AS `proveedor`,
 1 AS `nro_factura_informativa`,
 1 AS `nro_refrendo`,
 1 AS `product`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `nro_cajas`,
 1 AS `unidades`,
 1 AS `fecha_llegada_cliente`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `products_historicalproduct`
--

DROP TABLE IF EXISTS `products_historicalproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_historicalproduct` (
  `cod_contable` varchar(20) NOT NULL,
  `id_producto` int unsigned NOT NULL,
  `nro_registro_sanitario` varchar(25) NOT NULL,
  `fecha_emision_registro` date DEFAULT NULL,
  `fecha_vencimiento_registro` date DEFAULT NULL,
  `estado_registro` varchar(70) DEFAULT NULL,
  `grado_alcoholico` decimal(12,3) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `nombre_extrangero` varchar(120) DEFAULT NULL,
  `partida_arancelaria` varchar(15) DEFAULT NULL,
  `subpartida_arancelaria` varchar(15) DEFAULT NULL,
  `tnan_codigo` varchar(15) DEFAULT NULL,
  `cod_ice` varchar(39) NOT NULL,
  `capacidad_ml` smallint NOT NULL,
  `cantidad_x_caja` smallint NOT NULL,
  `costo_caja` decimal(16,10) NOT NULL,
  `estado` int NOT NULL,
  `custodia_doble` int NOT NULL,
  `peso` decimal(10,3) DEFAULT NULL,
  `pais_origen` varchar(70) DEFAULT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `registro_sanitario` longtext,
  `id_user` smallint DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `identificacion_proveedor` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`history_id`),
  KEY `products_historicalp_history_user_id_01ee232f_fk_auth_user` (`history_user_id`),
  KEY `products_historicalproduct_cod_contable_1d274cae` (`cod_contable`),
  KEY `products_historicalproduct_id_producto_cd7f2ecf` (`id_producto`),
  KEY `products_historicalproduct_nombre_e8619743` (`nombre`),
  KEY `products_historicalproduct_identificacion_proveedor_5dab8b8e` (`identificacion_proveedor`),
  CONSTRAINT `products_historicalp_history_user_id_01ee232f_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_historicalproduct`
--

LOCK TABLES `products_historicalproduct` WRITE;
/*!40000 ALTER TABLE `products_historicalproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `products_historicalproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prorrateo`
--

DROP TABLE IF EXISTS `prorrateo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prorrateo` (
  `id_prorrateo` int NOT NULL AUTO_INCREMENT,
  `porcentaje_parcial` decimal(20,13) NOT NULL,
  `fob_parcial_razon_inicial` decimal(20,13) NOT NULL,
  `fob_parcial_razon_saldo` decimal(20,13) NOT NULL,
  `fob_proximo_parcial` decimal(20,13) NOT NULL,
  `fob_inicial` decimal(20,13) NOT NULL,
  `fob_saldo` decimal(20,13) NOT NULL,
  `fob_parcial` decimal(20,13) NOT NULL,
  `almacenaje_parcial` decimal(20,13) NOT NULL,
  `almacenaje_anterior` decimal(20,13) NOT NULL,
  `almacenaje_aplicado` decimal(20,13) NOT NULL,
  `almacenaje_proximo_parcial` decimal(20,13) NOT NULL,
  `prorrateo_flete_aduana` decimal(20,13) NOT NULL,
  `prorrateo_seguro_aduana` decimal(20,13) NOT NULL,
  `gastos_drop_parcial` decimal(20,13) NOT NULL,
  `gastos_drop_parcial_anterior` decimal(20,13) NOT NULL,
  `gastos_drop_parcial_aplicado` decimal(20,13) NOT NULL,
  `gastos_drop_parcial_proximo_parcial` decimal(20,13) NOT NULL,
  `gastos_origen_incial` decimal(20,13) NOT NULL,
  `gastos_origen_anterior_parcial` decimal(20,13) NOT NULL,
  `gastos_origen_aplicado` decimal(20,13) NOT NULL,
  `gastos_origen_proximo_parcial` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_parcial` int NOT NULL,
  PRIMARY KEY (`id_prorrateo`),
  KEY `prorrateo_id_parcial_5734a30e_fk_parcial_id_parcial` (`id_parcial`),
  CONSTRAINT `prorrateo_id_parcial_5734a30e_fk_parcial_id_parcial` FOREIGN KEY (`id_parcial`) REFERENCES `parcial` (`id_parcial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prorrateo`
--

LOCK TABLES `prorrateo` WRITE;
/*!40000 ALTER TABLE `prorrateo` DISABLE KEYS */;
/*!40000 ALTER TABLE `prorrateo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prorrateo_detalle`
--

DROP TABLE IF EXISTS `prorrateo_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prorrateo_detalle` (
  `id_prorrateo_detalle` int NOT NULL AUTO_INCREMENT,
  `id_gastos_nacionalizacion` int unsigned NOT NULL,
  `tipo` varchar(13) NOT NULL,
  `concepto` varchar(90) NOT NULL,
  `valor_prorrateado` decimal(20,13) DEFAULT NULL,
  `valor_provisionado` decimal(20,13) NOT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_prorrateo` int NOT NULL,
  PRIMARY KEY (`id_prorrateo_detalle`),
  UNIQUE KEY `prorrateo_detalle_id_gastos_nacionalizacio_202b6f39_uniq` (`id_gastos_nacionalizacion`,`id_prorrateo`),
  KEY `prorrateo_detalle_id_prorrateo_b7fcd4f5_fk_prorrateo` (`id_prorrateo`),
  CONSTRAINT `prorrateo_detalle_id_prorrateo_b7fcd4f5_fk_prorrateo` FOREIGN KEY (`id_prorrateo`) REFERENCES `prorrateo` (`id_prorrateo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prorrateo_detalle`
--

LOCK TABLES `prorrateo_detalle` WRITE;
/*!40000 ALTER TABLE `prorrateo_detalle` DISABLE KEYS */;
/*!40000 ALTER TABLE `prorrateo_detalle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `identificacion_proveedor` varchar(16) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `tipo_provedor` varchar(13) NOT NULL,
  `moneda_transaccion` varchar(10) NOT NULL,
  `categoria` varchar(250) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `id_user` smallint DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `id_proveedor` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`identificacion_proveedor`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `id_proveedor` (`id_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `provisiones_vs_pagos`
--

DROP TABLE IF EXISTS `provisiones_vs_pagos`;
/*!50001 DROP VIEW IF EXISTS `provisiones_vs_pagos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `provisiones_vs_pagos` AS SELECT 
 1 AS `id_gastos_nacionalizacion`,
 1 AS `concepto`,
 1 AS `tipo`,
 1 AS `fecha`,
 1 AS `nro_pedido1`,
 1 AS `incoterm`,
 1 AS `nro_pedido`,
 1 AS `parcial`,
 1 AS `valor_provisionado`,
 1 AS `pago`,
 1 AS `saldo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `reporte_provisiones_final`
--

DROP TABLE IF EXISTS `reporte_provisiones_final`;
/*!50001 DROP VIEW IF EXISTS `reporte_provisiones_final`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `reporte_provisiones_final` AS SELECT 
 1 AS `id_gastos_nacionalizacion`,
 1 AS `concepto`,
 1 AS `tipo`,
 1 AS `fecha`,
 1 AS `nro_pedido1`,
 1 AS `incoterm`,
 1 AS `nro_pedido`,
 1 AS `parcial`,
 1 AS `valor_provisionado`,
 1 AS `pago`,
 1 AS `saldo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `saldos_provisiones`
--

DROP TABLE IF EXISTS `saldos_provisiones`;
/*!50001 DROP VIEW IF EXISTS `saldos_provisiones`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `saldos_provisiones` AS SELECT 
 1 AS `id_gastos_nacionalizacion`,
 1 AS `concepto`,
 1 AS `tipo`,
 1 AS `fecha`,
 1 AS `nro_pedido1`,
 1 AS `incoterm`,
 1 AS `nro_pedido`,
 1 AS `parcial`,
 1 AS `valor_provisionado`,
 1 AS `pago`,
 1 AS `saldo`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `stockActiveProductsInCustomsView`
--

DROP TABLE IF EXISTS `stockActiveProductsInCustomsView`;
/*!50001 DROP VIEW IF EXISTS `stockActiveProductsInCustomsView`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `stockActiveProductsInCustomsView` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `regimen`,
 1 AS `id_pedido_factura`,
 1 AS `id_factura_proveedor`,
 1 AS `identificacion_proveedor`,
 1 AS `proveedor`,
 1 AS `detalle_pedido_factura`,
 1 AS `producto`,
 1 AS `costo_caja`,
 1 AS `cod_contable`,
 1 AS `grado_alcoholico`,
 1 AS `nro_cajas`,
 1 AS `capacidad_ml`,
 1 AS `cantidad_x_caja`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `suppliers_historicalsupplier`
--

DROP TABLE IF EXISTS `suppliers_historicalsupplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers_historicalsupplier` (
  `identificacion_proveedor` varchar(16) NOT NULL,
  `nombre` varchar(60) NOT NULL,
  `tipo_provedor` varchar(13) NOT NULL,
  `moneda_transaccion` varchar(10) NOT NULL,
  `categoria` varchar(250) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `id_user` smallint DEFAULT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `history_id` int NOT NULL AUTO_INCREMENT,
  `history_date` datetime(6) NOT NULL,
  `history_change_reason` varchar(100) DEFAULT NULL,
  `history_type` varchar(1) NOT NULL,
  `history_user_id` int DEFAULT NULL,
  `id_proveedor` int NOT NULL,
  PRIMARY KEY (`history_id`),
  KEY `suppliers_historical_history_user_id_8de9e5dc_fk_auth_user` (`history_user_id`),
  KEY `suppliers_historicalsupplier_identificacion_proveedor_5580391a` (`identificacion_proveedor`),
  KEY `suppliers_historicalsupplier_nombre_1d2bb7b0` (`nombre`),
  CONSTRAINT `suppliers_historical_history_user_id_8de9e5dc_fk_auth_user` FOREIGN KEY (`history_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers_historicalsupplier`
--

LOCK TABLES `suppliers_historicalsupplier` WRITE;
/*!40000 ALTER TABLE `suppliers_historicalsupplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `suppliers_historicalsupplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarifa_gastos`
--

DROP TABLE IF EXISTS `tarifa_gastos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarifa_gastos` (
  `id_tarifa_gastos` int NOT NULL AUTO_INCREMENT,
  `regimen` varchar(5) NOT NULL,
  `tipo_gasto` varchar(21) NOT NULL,
  `concepto` varchar(120) NOT NULL,
  `valor` decimal(8,4) NOT NULL,
  `estado` int NOT NULL,
  `pais_origen` varchar(45) NOT NULL,
  `porcentaje` decimal(7,4) NOT NULL,
  `comentarios` varchar(550) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `identificacion_proveedor` varchar(16) NOT NULL,
  PRIMARY KEY (`id_tarifa_gastos`),
  UNIQUE KEY `tarifa_gastos_identificacion_proveedor_a801fba5_uniq` (`identificacion_proveedor`,`concepto`,`pais_origen`,`valor`,`tipo_gasto`),
  CONSTRAINT `tarifa_gastos_identificacion_prove_2dc23776_fk_proveedor` FOREIGN KEY (`identificacion_proveedor`) REFERENCES `proveedor` (`identificacion_proveedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarifa_gastos`
--

LOCK TABLES `tarifa_gastos` WRITE;
/*!40000 ALTER TABLE `tarifa_gastos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarifa_gastos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tarifa_incoterm`
--

DROP TABLE IF EXISTS `tarifa_incoterm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tarifa_incoterm` (
  `id_incoterm` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(12) NOT NULL,
  `pais` varchar(45) NOT NULL,
  `incoterms` varchar(4) NOT NULL,
  `ciudad` varchar(45) NOT NULL,
  `tarifa` decimal(8,2) NOT NULL,
  `comentarios` varchar(250) DEFAULT NULL,
  `id_user` smallint NOT NULL,
  `date_create` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id_incoterm`),
  UNIQUE KEY `tarifa_incoterm_pais_ciudad_incoterms_tipo_62fc5ea4_uniq` (`pais`,`ciudad`,`incoterms`,`tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tarifa_incoterm`
--

LOCK TABLES `tarifa_incoterm` WRITE;
/*!40000 ALTER TABLE `tarifa_incoterm` DISABLE KEYS */;
/*!40000 ALTER TABLE `tarifa_incoterm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_user` smallint NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `cargo` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(120) NOT NULL,
  `usertype` enum('L1','L2','L3') NOT NULL COMMENT 'L1 Administrador; L2 Ingreso Data; L3 Visualizacion',
  `last_login` datetime DEFAULT NULL,
  `date_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_update` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='Se registran todos los impuestos que existen en una nacionalizacion, solo impuestos de la SENAE';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (3,'ADRIAN CARDENAS','acardenas@vinesa.com.ec','STAFF','acardenas','','L1','2019-02-14 15:29:44','2017-10-17 19:33:06',NULL),(4,'ALEXANDRA LEON','info6@vinesa.com.ec','STAFF','aleon','n2mO6XIyiy1TTYk1twLHrVjDV+VfZwVZTKZh+aghilM=','L1','2021-09-06 15:58:53','2017-10-17 19:33:06',NULL),(5,'ALEXANDRA VARGAS','info7@vinesa.com.ec','STAFF','avargas','','L1',NULL,'2017-10-17 19:33:06',NULL),(29,'ALEXANDRA YANEZ','ayanez@vinesa.com.ec','STAFF','ayanez','jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=','L1','2021-09-08 14:31:53','2019-04-02 10:00:00',NULL),(6,'CECILIA FELIX','cfelix@vinesa.com.ec','STAFF','cfelix','','L1','2019-12-23 16:08:41','2017-10-17 19:33:06',NULL),(1,'ADMINISTRADOR','usuario@gmail.com','STAFF','cordovez','erdYyo1ERYzIcgXJsjM6bRkmFq5JecqAhJzPmFqMPa8=','L1','2021-09-09 15:14:42','2017-09-07 19:46:27',NULL),(27,'DANIEL MAZA','bodega1@vinesa.com.ec','BODEGA','dmaza','EPGAYnJDjKfRjOLMHuWFpo0y9q6ZOJIKeBT9aBBvfbI=','L3','2021-05-03 15:57:46','2018-11-07 20:08:16',NULL),(7,'DAVID PEREZ','info5@vinesa.com.ec','STAFF','dperez','','L1','2018-01-09 18:01:01','2017-10-17 19:33:06',NULL),(17,'ELIZABETH SALA','info20@vinesa.com','USUARIO ADICIONAL','esala','','L2','2019-03-11 11:26:02','2018-07-06 03:19:28',NULL),(25,'EDUARDO VILLOTA','eduardouio7@gmail.com','STAFF','evillota','erdYyo1ERYzIcgXJsjM6bRkmFq5JecqAhJzPmFqMPa8=','L1','2021-08-16 10:44:59','2017-09-07 19:46:27',NULL),(28,'FELIPE CORDOVEZ','fcordovez@vinesa.com.ec','STAFF','fcordovez','','L1','2018-11-07 12:17:00','2017-09-07 19:46:27',NULL),(8,'GABRIELA ALARCON','galarcon@vinesa.com.ec','STAFF','galarcon','','L1','2021-08-31 08:57:46','2017-10-17 19:33:06',NULL),(9,'JEANNETH CARRILLO','jcarrillo@vinesa.com.ec','STAFF','jcarrillo','','L1','2019-02-07 15:13:07','2017-10-17 19:33:06',NULL),(10,'JORGE CHULDE','jchulde@vinesa.com.ec ','STAFF','jchulde','','L1','2018-06-11 23:22:10','2017-10-17 19:33:06',NULL),(15,'JONATHAN CRUZ','info9@vinesa.com.ec','STAFF','jcruz','jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=','L1','2021-09-09 12:50:43','2017-10-17 19:33:06',NULL),(26,' JEFERSON PACHECO','jpacheco@vinesa.com','STAFF','jpacheco','','L1','2018-11-26 12:14:52','2017-09-07 19:46:27',NULL),(23,'Karla Lema','klema@vinesa.com.ec','STAFF','klema','','L1','2019-02-01 11:01:27','2017-10-17 19:33:06',NULL),(18,'KAROL TOAPANTA','info19@vinesa.com.','Usuario Adicional','ktoapanta','','L2','2020-01-31 11:29:51','2018-07-06 03:19:28',NULL),(33,'LORENA RODRIGUEZ','lrodriguez@vinesa.com.ec','STAFF','lrodriguez','sevQ0S4uFBbNMD6+9xmUyW9kppwqGnmLxrDJI0REFak=','L1','2021-09-09 14:24:28','2017-09-07 19:46:27',NULL),(24,'Lizbeth Santamaria','lsantamaria@vinesa.com.ec','STAFF','lsantamaria','','L1','2018-10-29 19:26:50','2017-10-17 19:33:06',NULL),(11,'MARIA ELENA SANTI','msanti@vinesa.com.ec','STAFF','msanti','','L1','2020-08-28 10:02:07','2017-10-17 19:33:06',NULL),(12,'MARIA ELENA TERAN','mteran@vinesa.com.ec','STAFF','mteran','XnCOFXzvzFGHXS/GZ5kVEZ9PAE2N+oCeqydK87yGuwo=','L1','2021-08-27 16:48:38','2017-10-17 19:33:06',NULL),(31,'PATRICIA RAMOS','pramos@vinesa.com.ec','STAFF','pramos','','L1','2019-12-28 17:46:46','2017-09-07 19:46:27',NULL),(2,'RUTH ANDRADE','Randrade@vinesa.com.ec','STAFF','randrade','','L1','2018-08-16 16:17:47','2017-10-17 19:19:41',NULL),(16,'Rocío Villegas','rvillegas@vinesa.com.ec ','STAFF','rvillegas','','L1','2018-10-15 13:27:50','2017-10-17 19:33:06',NULL),(32,'VERONICA HEREDIA','vheredia@vinesa.com.ec','STAFF','vheredia','RZjDbQo9p8exSPBMe9Pgn2SJ+cL9Njn718JA3oiJ10E=','L1','2021-09-08 15:51:20','2017-10-17 19:33:06',NULL),(30,'MARJORIE OLVERA','mcano@vinlitoral.com.ec','STAFF','vinlitoral','Z0YfSo/3PhAeT480swtFY2GFs8CNzzN9CuSZKAa5kOo=','L1','2021-08-30 13:39:14','2017-09-07 19:46:27',NULL),(13,'VERONICA PONCE','info2@vinesa.com.ec','STAFF','vponce','','L1',NULL,'2017-10-17 19:33:06',NULL),(22,'Yovana Paccha','infoc1@vinesa.com.ec','STAFF','ypaccha','','L1','2020-11-05 11:21:51','2017-10-17 19:33:06',NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_costs_analysis`
--

DROP TABLE IF EXISTS `v_costs_analysis`;
/*!50001 DROP VIEW IF EXISTS `v_costs_analysis`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_costs_analysis` AS SELECT 
 1 AS `producto`,
 1 AS `proveedor`,
 1 AS `cod_contable`,
 1 AS `cod_ice`,
 1 AS `cantidad_x_caja`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `nro_pedido`,
 1 AS `id_parcial`,
 1 AS `fecha_arribo`,
 1 AS `fecha_ingreso_almacenera`,
 1 AS `dias_transito_puerto`,
 1 AS `dias_permanencia_almagro`,
 1 AS `dias_transito`,
 1 AS `fecha_llegada_cliente`,
 1 AS `regimen`,
 1 AS `pais_origen`,
 1 AS `ciudad_origen`,
 1 AS `incoterm`,
 1 AS `unidades`,
 1 AS `costo_unidad`,
 1 AS `moneda`,
 1 AS `tipo_cambio`,
 1 AS `fob`,
 1 AS `cif`,
 1 AS `ex_aduana_unitario`,
 1 AS `base_fodinfa`,
 1 AS `base_iva`,
 1 AS `base_ice_advalorem`,
 1 AS `base_ice_especifico`,
 1 AS `exoneracion_arancel`,
 1 AS `total_ice`,
 1 AS `fodinfa`,
 1 AS `arancel_advalorem`,
 1 AS `arancel_especifico`,
 1 AS `tributos`,
 1 AS `costo_sap`,
 1 AS `indirectos_pe`,
 1 AS `indirectos_pr`,
 1 AS `indirectos`,
 1 AS `costo_botella`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_ice_parciales`
--

DROP TABLE IF EXISTS `v_ice_parciales`;
/*!50001 DROP VIEW IF EXISTS `v_ice_parciales`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_ice_parciales` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `cod_ice`,
 1 AS `fecha_llegada_cliente`,
 1 AS `pais_origen`,
 1 AS `nro_cajas`,
 1 AS `unidades`,
 1 AS `fob_tasa_trimestral`,
 1 AS `Name_exp_9`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `ex_aduana_unitario`,
 1 AS `ice_especifico_unitario`,
 1 AS `ice_advalorem_unitario`,
 1 AS `ice_unitario`,
 1 AS `total_ice`,
 1 AS `costo_total`,
 1 AS `costo_caja_final`,
 1 AS `digitos`,
 1 AS `anio`,
 1 AS `reg`,
 1 AS `cons`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_ice_r10`
--

DROP TABLE IF EXISTS `v_ice_r10`;
/*!50001 DROP VIEW IF EXISTS `v_ice_r10`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_ice_r10` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `cod_ice`,
 1 AS `fecha_llegada_cliente`,
 1 AS `pais_origen`,
 1 AS `nro_cajas`,
 1 AS `unidades`,
 1 AS `fob_tasa_trimestral`,
 1 AS `Name_exp_9`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `ex_aduana_unitario`,
 1 AS `ice_especifico_unitario`,
 1 AS `ice_advalorem_unitario`,
 1 AS `ice_unitario`,
 1 AS `total_ice`,
 1 AS `costo_total`,
 1 AS `costo_caja_final`,
 1 AS `digitos`,
 1 AS `anio`,
 1 AS `reg`,
 1 AS `cons`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_producto_pedidos_R10_llegados`
--

DROP TABLE IF EXISTS `v_producto_pedidos_R10_llegados`;
/*!50001 DROP VIEW IF EXISTS `v_producto_pedidos_R10_llegados`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_producto_pedidos_R10_llegados` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `id_factura_proveedor`,
 1 AS `nro_refrendo`,
 1 AS `producto`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `nro_cajas`,
 1 AS `unidades`,
 1 AS `fecha_llegada_cliente`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_productos_pedidos`
--

DROP TABLE IF EXISTS `v_productos_pedidos`;
/*!50001 DROP VIEW IF EXISTS `v_productos_pedidos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_productos_pedidos` AS SELECT 
 1 AS `nro_pedido`,
 1 AS `nombre`,
 1 AS `id_factura_proveedor`,
 1 AS `nro_refrendo`,
 1 AS `producto`,
 1 AS `capacidad_ml`,
 1 AS `grado_alcoholico`,
 1 AS `nro_cajas`,
 1 AS `unidades`,
 1 AS `fecha_llegada_cliente`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_sgi_provisiones_pagos`
--

DROP TABLE IF EXISTS `v_sgi_provisiones_pagos`;
/*!50001 DROP VIEW IF EXISTS `v_sgi_provisiones_pagos`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_sgi_provisiones_pagos` AS SELECT 
 1 AS `id_gastos_nacionalizacion`,
 1 AS `id_parcial`,
 1 AS `concepto`,
 1 AS `tipo`,
 1 AS `valor_provisionado`,
 1 AS `valor_ajuste`,
 1 AS `fecha`,
 1 AS `fecha_fin`,
 1 AS `comentarios`,
 1 AS `bg_closed`,
 1 AS `bg_is_visible_gi`,
 1 AS `bg_iscontabilizado`,
 1 AS `bg_iscontabilizado_por`,
 1 AS `bg_isdrop`,
 1 AS `id_user`,
 1 AS `date_create`,
 1 AS `last_update`,
 1 AS `identificacion_proveedor`,
 1 AS `nro_pedido`,
 1 AS `pago`,
 1 AS `saldo`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `facturas_proveedor_pendientes`
--

/*!50001 DROP VIEW IF EXISTS `facturas_proveedor_pendientes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `facturas_proveedor_pendientes` AS select `pf`.`nro_pedido` AS `nro_pedido`,`pr`.`nombre` AS `nombre`,`pf`.`id_factura_proveedor` AS `id_factura_proveedor`,`pf`.`valor` AS `valor` from (`cordovezApp`.`pedido_factura` `pf` join `cordovezApp`.`proveedor` `pr` on((`pf`.`identificacion_proveedor` = `pr`.`identificacion_proveedor`))) where (`pf`.`id_factura_proveedor` like 'SF%') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `llegadas_almagro`
--

/*!50001 DROP VIEW IF EXISTS `llegadas_almagro`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `llegadas_almagro` AS select replace(`o`.`nro_pedido`,'-','/') AS `nro_pedido`,`pr`.`nombre` AS `nombre`,`pr`.`cod_ice` AS `cod_ice`,`o`.`fecha_ingreso_almacenera` AS `fecha_ingreso_almacenera`,`o`.`pais_origen` AS `pais_origen`,`dpf`.`nro_cajas` AS `nro_cajas`,`dpf`.`unidades` AS `unidades`,((`dpf`.`costo_caja` * `dpf`.`nro_cajas`) * `pf`.`tipo_cambio`) AS `fob`,'' AS `Name_exp_9`,`pr`.`capacidad_ml` AS `capacidad_ml`,`dpf`.`grado_alcoholico` AS `grado_alcoholico`,`dpf`.`ex_aduana_unitario` AS `ex_aduana_unitario`,`dpf`.`ice_especifico_unitario` AS `ice_especifico_unitario`,`dpf`.`ice_advalorem_unitario` AS `ice_advalorem_unitario`,`dpf`.`ice_unitario` AS `ice_unitario`,`dpf`.`total_ice` AS `total_ice`,`dpf`.`costo_total` AS `costo_total`,`dpf`.`costo_caja_final` AS `costo_caja_final`,substr(`o`.`nro_refrendo`,1,3) AS `digitos`,substr(`o`.`nro_refrendo`,5,4) AS `anio`,substr(`o`.`nro_refrendo`,10,2) AS `reg`,substr(`o`.`nro_refrendo`,13,8) AS `cons` from (((`cordovezApp`.`pedido` `o` left join `cordovezApp`.`pedido_factura` `pf` on((`pf`.`nro_pedido` = `o`.`nro_pedido`))) left join `cordovezApp`.`detalle_pedido_factura` `dpf` on((`pf`.`id_pedido_factura` = `dpf`.`id_pedido_factura`))) left join `cordovezApp`.`producto` `pr` on((`pr`.`cod_contable` = `dpf`.`cod_contable`))) where (`o`.`fecha_ingreso_almacenera` > '2019-10-00') order by `o`.`fecha_ingreso_almacenera`,`o`.`nro_pedido` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `llegadas_pendientes_almagro`
--

/*!50001 DROP VIEW IF EXISTS `llegadas_pendientes_almagro`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `llegadas_pendientes_almagro` AS select `p`.`nro_pedido` AS `nro_pedido`,`s`.`nombre` AS `nombre`,`p`.`fecha_liquidacion` AS `fecha_liquidacion`,`fi`.`nro_factura_informativa` AS `nro_factura_informativa`,`fi`.`nro_refrendo` AS `nro_refrendo`,`p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente` from (((`cordovezApp`.`parcial` `p` left join `cordovezApp`.`factura_informativa` `fi` on((`fi`.`id_parcial` = `p`.`id_parcial`))) left join `cordovezApp`.`pedido_factura` `pf` on((`p`.`nro_pedido` = `pf`.`nro_pedido`))) left join `cordovezApp`.`proveedor` `s` on((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`))) where ((`p`.`bg_isliquidated` = 1) and (`p`.`fecha_llegada_cliente` is null)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `producto_en_transito`
--

/*!50001 DROP VIEW IF EXISTS `producto_en_transito`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `producto_en_transito` AS select cast(substr(`p`.`nro_pedido`,1,3) as unsigned) AS `consecutivo`,cast(substr(`p`.`nro_pedido`,5,2) as unsigned) AS `anio`,`p`.`nro_pedido` AS `nro_pedido`,`fi`.`nro_refrendo` AS `nro_refrendo`,`pro`.`nombre` AS `nombre`,`p`.`fecha_liquidacion` AS `fecha_liquidacion`,`p`.`bg_isliquidated` AS `bg_isliquidated`,`p`.`bg_isclosed` AS `bg_isclosed`,`p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,`fid`.`nro_cajas` AS `nro_cajas`,`pro`.`cantidad_x_caja` AS `cantidad_x_caja`,(`pro`.`cantidad_x_caja` * `fid`.`nro_cajas`) AS `Unidades` from ((((`cordovezApp`.`factura_informativa_detalle` `fid` join `cordovezApp`.`factura_informativa` `fi` on((`fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`))) join `cordovezApp`.`parcial` `p` on((`fi`.`id_parcial` = `p`.`id_parcial`))) join `cordovezApp`.`detalle_pedido_factura` `dpf` on((`fid`.`detalle_pedido_factura` = `dpf`.`detalle_pedido_factura`))) join `cordovezApp`.`producto` `pro` on((`dpf`.`cod_contable` = `pro`.`cod_contable`))) where ((`p`.`bg_isliquidated` = 1) and (`p`.`fecha_llegada_cliente` is null)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `producto_parcial_llegado`
--

/*!50001 DROP VIEW IF EXISTS `producto_parcial_llegado`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `producto_parcial_llegado` AS select `fid`.`id_factura_informativa` AS `id_factura_informativa`,`p`.`nro_pedido` AS `nro_pedido`,`o`.`proveedor` AS `proveedor`,`fi`.`nro_factura_informativa` AS `nro_factura_informativa`,`fi`.`nro_refrendo` AS `nro_refrendo`,`fid`.`product` AS `product`,`fid`.`capacidad_ml` AS `capacidad_ml`,`fid`.`grado_alcoholico` AS `grado_alcoholico`,`fid`.`nro_cajas` AS `nro_cajas`,`fid`.`unidades` AS `unidades`,`p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente` from (((`cordovezApp`.`factura_informativa_detalle` `fid` left join `cordovezApp`.`factura_informativa` `fi` on((`fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`))) left join `cordovezApp`.`parcial` `p` on((`p`.`id_parcial` = `fi`.`id_parcial`))) left join `cordovezApp`.`pedido` `o` on((`p`.`nro_pedido` = `o`.`nro_pedido`))) order by `p`.`fecha_llegada_cliente`,`fi`.`id_factura_informativa` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provisiones_vs_pagos`
--

/*!50001 DROP VIEW IF EXISTS `provisiones_vs_pagos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provisiones_vs_pagos` AS select `gn`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,`gn`.`concepto` AS `concepto`,`gn`.`tipo` AS `tipo`,`gn`.`fecha` AS `fecha`,ifnull(`p`.`nro_pedido`,`gn`.`nro_pedido`) AS `nro_pedido1`,`o`.`incoterm` AS `incoterm`,`o`.`nro_pedido` AS `nro_pedido`,`gn`.`id_parcial` AS `parcial`,`gn`.`valor_provisionado` AS `valor_provisionado`,(select ifnull(sum(`ddp`.`valor`),0) from `cordovezApp`.`detalle_documento_pago` `ddp` where (`ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`)) AS `pago`,(`gn`.`valor_provisionado` - (select ifnull(sum(`ddp`.`valor`),0) from `cordovezApp`.`detalle_documento_pago` `ddp` where (`ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`))) AS `saldo` from ((`cordovezApp`.`gastos_nacionalizacion` `gn` left join `cordovezApp`.`parcial` `p` on(((`p`.`id_parcial` = `gn`.`id_parcial`) and (`gn`.`id_parcial` <> 0)))) left join `cordovezApp`.`pedido` `o` on(((ifnull(`p`.`nro_pedido`,`gn`.`nro_pedido`) = `o`.`nro_pedido`) and (`gn`.`concepto` <> 'ISD') and (`gn`.`concepto` <> 'TRANSPORTE') and (`gn`.`concepto` <> 'MANO DE OBRA ETIQUETADO') and (`gn`.`concepto` <> 'DESCARGA') and (`gn`.`concepto` <> 'ISD') and (`gn`.`fecha` > '2018-12-31')))) order by `gn`.`tipo`,`gn`.`fecha`,`gn`.`concepto` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `reporte_provisiones_final`
--

/*!50001 DROP VIEW IF EXISTS `reporte_provisiones_final`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `reporte_provisiones_final` AS select `cordovezApp`.`provisiones_vs_pagos`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,`cordovezApp`.`provisiones_vs_pagos`.`concepto` AS `concepto`,`cordovezApp`.`provisiones_vs_pagos`.`tipo` AS `tipo`,`cordovezApp`.`provisiones_vs_pagos`.`fecha` AS `fecha`,`cordovezApp`.`provisiones_vs_pagos`.`nro_pedido1` AS `nro_pedido1`,`cordovezApp`.`provisiones_vs_pagos`.`incoterm` AS `incoterm`,`cordovezApp`.`provisiones_vs_pagos`.`nro_pedido` AS `nro_pedido`,`cordovezApp`.`provisiones_vs_pagos`.`parcial` AS `parcial`,`cordovezApp`.`provisiones_vs_pagos`.`valor_provisionado` AS `valor_provisionado`,`cordovezApp`.`provisiones_vs_pagos`.`pago` AS `pago`,`cordovezApp`.`provisiones_vs_pagos`.`saldo` AS `saldo` from `cordovezApp`.`provisiones_vs_pagos` where ((`cordovezApp`.`provisiones_vs_pagos`.`saldo` <> 0) and (`cordovezApp`.`provisiones_vs_pagos`.`concepto` <> 'ISD') and (`cordovezApp`.`provisiones_vs_pagos`.`fecha` > '2020-01-01')) order by `cordovezApp`.`provisiones_vs_pagos`.`concepto` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `saldos_provisiones`
--

/*!50001 DROP VIEW IF EXISTS `saldos_provisiones`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `saldos_provisiones` AS select `cordovezApp`.`provisiones_vs_pagos`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,`cordovezApp`.`provisiones_vs_pagos`.`concepto` AS `concepto`,`cordovezApp`.`provisiones_vs_pagos`.`tipo` AS `tipo`,`cordovezApp`.`provisiones_vs_pagos`.`fecha` AS `fecha`,`cordovezApp`.`provisiones_vs_pagos`.`nro_pedido1` AS `nro_pedido1`,`cordovezApp`.`provisiones_vs_pagos`.`incoterm` AS `incoterm`,`cordovezApp`.`provisiones_vs_pagos`.`nro_pedido` AS `nro_pedido`,`cordovezApp`.`provisiones_vs_pagos`.`parcial` AS `parcial`,`cordovezApp`.`provisiones_vs_pagos`.`valor_provisionado` AS `valor_provisionado`,`cordovezApp`.`provisiones_vs_pagos`.`pago` AS `pago`,`cordovezApp`.`provisiones_vs_pagos`.`saldo` AS `saldo` from `cordovezApp`.`provisiones_vs_pagos` where ((`cordovezApp`.`provisiones_vs_pagos`.`fecha` > '2019-01-00') and (`cordovezApp`.`provisiones_vs_pagos`.`concepto` <> 'ISD') and (`cordovezApp`.`provisiones_vs_pagos`.`saldo` <> 0)) order by `cordovezApp`.`provisiones_vs_pagos`.`concepto` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `stockActiveProductsInCustomsView`
--

/*!50001 DROP VIEW IF EXISTS `stockActiveProductsInCustomsView`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `stockActiveProductsInCustomsView` AS select `pf`.`nro_pedido` AS `nro_pedido`,`ped`.`regimen` AS `regimen`,`dpf`.`id_pedido_factura` AS `id_pedido_factura`,`pf`.`id_factura_proveedor` AS `id_factura_proveedor`,`pf`.`identificacion_proveedor` AS `identificacion_proveedor`,`prov`.`nombre` AS `proveedor`,`dpf`.`detalle_pedido_factura` AS `detalle_pedido_factura`,`pro`.`nombre` AS `producto`,`dpf`.`costo_caja` AS `costo_caja`,`dpf`.`cod_contable` AS `cod_contable`,`dpf`.`grado_alcoholico` AS `grado_alcoholico`,`dpf`.`nro_cajas` AS `nro_cajas`,`pro`.`capacidad_ml` AS `capacidad_ml`,`pro`.`cantidad_x_caja` AS `cantidad_x_caja` from ((((`cordovezApp`.`detalle_pedido_factura` `dpf` left join `cordovezApp`.`producto` `pro` on((`dpf`.`cod_contable` = `pro`.`cod_contable`))) left join `cordovezApp`.`pedido_factura` `pf` on((`dpf`.`id_pedido_factura` = `pf`.`id_pedido_factura`))) left join `cordovezApp`.`pedido` `ped` on((`pf`.`nro_pedido` = `ped`.`nro_pedido`))) left join `cordovezApp`.`proveedor` `prov` on((`pf`.`identificacion_proveedor` = `prov`.`identificacion_proveedor`))) where (`dpf`.`nro_cajas` > 0) order by `pf`.`nro_pedido` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_costs_analysis`
--

/*!50001 DROP VIEW IF EXISTS `v_costs_analysis`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_costs_analysis` AS select `p`.`nombre` AS `producto`,`s`.`nombre` AS `proveedor`,`ddp`.`cod_contable` AS `cod_contable`,`p`.`cod_ice` AS `cod_ice`,`p`.`cantidad_x_caja` AS `cantidad_x_caja`,`p`.`capacidad_ml` AS `capacidad_ml`,`ddp`.`grado_alcoholico` AS `grado_alcoholico`,`pf`.`nro_pedido` AS `nro_pedido`,'0' AS `id_parcial`,`o`.`fecha_arribo` AS `fecha_arribo`,`o`.`fecha_ingreso_almacenera` AS `fecha_ingreso_almacenera`,ifnull((to_days(`o`.`fecha_llegada_cliente`) - to_days(`o`.`fecha_arribo`)),0) AS `dias_transito_puerto`,0 AS `dias_permanencia_almagro`,ifnull((to_days(`o`.`fecha_llegada_cliente`) - to_days(`o`.`fecha_arribo`)),0) AS `dias_transito`,`o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,`o`.`regimen` AS `regimen`,`o`.`pais_origen` AS `pais_origen`,`o`.`ciudad_origen` AS `ciudad_origen`,`o`.`incoterm` AS `incoterm`,(`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`) AS `unidades`,(`ddp`.`costo_caja` / `p`.`cantidad_x_caja`) AS `costo_unidad`,if((`pf`.`tipo_cambio` = 1),'USD','EUR') AS `moneda`,`pf`.`tipo_cambio` AS `tipo_cambio`,(`ddp`.`fob` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `fob`,(`ddp`.`cif` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `cif`,`ddp`.`ex_aduana_unitario` AS `ex_aduana_unitario`,`o`.`base_fodinfa` AS `base_fodinfa`,`o`.`base_iva` AS `base_iva`,`o`.`base_ice_advalorem` AS `base_ice_advalorem`,`o`.`base_ice_especifico` AS `base_ice_especifico`,`o`.`exoneracion_arancel` AS `exoneracion_arancel`,(`ddp`.`total_ice` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `total_ice`,(`ddp`.`fodinfa` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `fodinfa`,(`ddp`.`arancel_advalorem_pagar` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `arancel_advalorem`,(`ddp`.`arancel_especifico_pagar` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `arancel_especifico`,((((`ddp`.`total_ice` + `ddp`.`fodinfa`) + `ddp`.`arancel_advalorem_pagar`) + `ddp`.`arancel_especifico_pagar`) / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `tributos`,((`ddp`.`costo_caja` * `pf`.`tipo_cambio`) / `p`.`cantidad_x_caja`) AS `costo_sap`,(((((`ddp`.`prorrateos_total` - `ddp`.`total_ice`) - `ddp`.`fodinfa`) - `ddp`.`arancel_advalorem_pagar`) - `ddp`.`arancel_especifico_pagar`) / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `indirectos_pe`,(((((`ddp`.`indirectos` - `ddp`.`total_ice`) - `ddp`.`fodinfa`) - `ddp`.`arancel_advalorem_pagar`) - `ddp`.`arancel_especifico_pagar`) / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `indirectos_pr`,(((`ddp`.`costo_total` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) - ((((`ddp`.`total_ice` + `ddp`.`fodinfa`) + `ddp`.`arancel_advalorem_pagar`) + `ddp`.`arancel_especifico_pagar`) / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`))) - ((`ddp`.`costo_caja` * `pf`.`tipo_cambio`) / `p`.`cantidad_x_caja`)) AS `indirectos`,(`ddp`.`costo_total` / (`ddp`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `costo_botella` from ((((`cordovezApp`.`detalle_pedido_factura` `ddp` left join `cordovezApp`.`pedido_factura` `pf` on((`pf`.`id_pedido_factura` = `ddp`.`id_pedido_factura`))) left join `cordovezApp`.`proveedor` `s` on((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`))) left join `cordovezApp`.`producto` `p` on((`p`.`cod_contable` = `ddp`.`cod_contable`))) left join `cordovezApp`.`pedido` `o` on((`pf`.`nro_pedido` = `o`.`nro_pedido`))) where ((`o`.`regimen` = '10') and (`o`.`bg_isclosed` = 1) and (`ddp`.`costo_caja_final` > 0)) union select `p`.`nombre` AS `producto`,`s`.`nombre` AS `proveedor`,`ddp`.`cod_contable` AS `cod_contable`,`p`.`cod_ice` AS `cod_ice`,`p`.`cantidad_x_caja` AS `cantidad_x_caja`,`p`.`capacidad_ml` AS `capacidad_ml`,`fid`.`grado_alcoholico` AS `grado_alcoholico`,`pf`.`nro_pedido` AS `nro_pedido`,`pc`.`id_parcial` AS `id_parcial`,`o`.`fecha_arribo` AS `fecha_arribo`,`o`.`fecha_ingreso_almacenera` AS `fecha_ingreso_almacenera`,ifnull((to_days(`o`.`fecha_ingreso_almacenera`) - to_days(`o`.`fecha_arribo`)),0) AS `dias_transito_puerto`,ifnull((to_days(`pc`.`fecha_llegada_cliente`) - to_days(`o`.`fecha_ingreso_almacenera`)),0) AS `dias_permanencia_almagro`,ifnull((to_days(`pc`.`fecha_llegada_cliente`) - to_days(`o`.`fecha_arribo`)),0) AS `dias_transito`,`pc`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,`o`.`regimen` AS `regimen`,`o`.`pais_origen` AS `pais_origen`,`o`.`ciudad_origen` AS `ciudad_origen`,`o`.`incoterm` AS `incoterm`,(`fid`.`nro_cajas` * `p`.`cantidad_x_caja`) AS `unidades`,(`ddp`.`costo_caja` / `p`.`cantidad_x_caja`) AS `costo_unidad`,if((`pf`.`tipo_cambio` = 1),'USD','EUR') AS `moneda`,`pf`.`tipo_cambio` AS `tipo_cambio`,(`fid`.`fob` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `fob`,(`fid`.`cif` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `cif`,`fid`.`ex_aduana_unitario` AS `ex_aduana_unitario`,`pc`.`base_fodinfa` AS `base_fodinfa`,`pc`.`base_iva` AS `base_iva`,`pc`.`base_ice_advalorem` AS `base_ice_advalorem`,`pc`.`base_ice_especifico` AS `base_ice_especifico`,`pc`.`exoneracion_arancel` AS `exoneracion_arancel`,(`fid`.`total_ice` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `total_ice`,(`fid`.`fodinfa` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `fodinfa`,(`fid`.`arancel_advalorem_pagar` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `arancel_advalorem`,(`fid`.`arancel_especifico_pagar` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `arancel_especifico`,((((`fid`.`total_ice` + `fid`.`fodinfa`) + `fid`.`arancel_advalorem_pagar`) + `fid`.`arancel_especifico_pagar`) / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `tributos`,((`ddp`.`costo_caja` * `pf`.`tipo_cambio`) / `p`.`cantidad_x_caja`) AS `costo_sap`,(((((`fid`.`prorrateos_total` - `fid`.`total_ice`) - `fid`.`fodinfa`) - `fid`.`arancel_advalorem_pagar`) - `fid`.`arancel_especifico_pagar`) / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `indirectos_pe`,(((((`fid`.`indirectos` - `fid`.`total_ice`) - `fid`.`fodinfa`) - `fid`.`arancel_advalorem_pagar`) - `fid`.`arancel_especifico_pagar`) / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `indirectos_pr`,(((`fid`.`costo_total` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) - ((((`fid`.`total_ice` + `fid`.`fodinfa`) + `fid`.`arancel_advalorem_pagar`) + `fid`.`arancel_especifico_pagar`) / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`))) - ((`ddp`.`costo_caja` * `pf`.`tipo_cambio`) / `p`.`cantidad_x_caja`)) AS `indirectos`,(`fid`.`costo_total` / (`fid`.`nro_cajas` * `p`.`cantidad_x_caja`)) AS `costo_botella` from (((((((`cordovezApp`.`factura_informativa_detalle` `fid` left join `cordovezApp`.`factura_informativa` `fi` on((`fi`.`id_factura_informativa` = `fid`.`id_factura_informativa`))) left join `cordovezApp`.`parcial` `pc` on((`pc`.`id_parcial` = `fi`.`id_parcial`))) left join `cordovezApp`.`pedido` `o` on((`o`.`nro_pedido` = `pc`.`nro_pedido`))) left join `cordovezApp`.`detalle_pedido_factura` `ddp` on((`ddp`.`detalle_pedido_factura` = `fid`.`detalle_pedido_factura`))) left join `cordovezApp`.`producto` `p` on((`p`.`cod_contable` = `ddp`.`cod_contable`))) left join `cordovezApp`.`pedido_factura` `pf` on((`pf`.`id_pedido_factura` = `ddp`.`id_pedido_factura`))) left join `cordovezApp`.`proveedor` `s` on((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`))) where (`pc`.`bg_isclosed` = 1) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_ice_parciales`
--

/*!50001 DROP VIEW IF EXISTS `v_ice_parciales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_ice_parciales` AS select replace(`p`.`nro_pedido`,'-','/') AS `nro_pedido`,`pr`.`nombre` AS `nombre`,`pr`.`cod_ice` AS `cod_ice`,`p`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,`o`.`pais_origen` AS `pais_origen`,`fid`.`nro_cajas` AS `nro_cajas`,`fid`.`unidades` AS `unidades`,`fid`.`fob_tasa_trimestral` AS `fob_tasa_trimestral`,'' AS `Name_exp_9`,`pr`.`capacidad_ml` AS `capacidad_ml`,`fid`.`grado_alcoholico` AS `grado_alcoholico`,`fid`.`ex_aduana_unitario` AS `ex_aduana_unitario`,`fid`.`ice_especifico_unitario` AS `ice_especifico_unitario`,`fid`.`ice_advalorem_unitario` AS `ice_advalorem_unitario`,`fid`.`ice_unitario` AS `ice_unitario`,`fid`.`total_ice` AS `total_ice`,`fid`.`costo_total` AS `costo_total`,`fid`.`costo_caja_final` AS `costo_caja_final`,substr(`fi`.`nro_refrendo`,1,3) AS `digitos`,substr(`fi`.`nro_refrendo`,5,4) AS `anio`,substr(`fi`.`nro_refrendo`,10,2) AS `reg`,substr(`fi`.`nro_refrendo`,13,8) AS `cons` from (((((`cordovezApp`.`parcial` `p` left join `cordovezApp`.`pedido` `o` on((`o`.`nro_pedido` = `p`.`nro_pedido`))) left join `cordovezApp`.`factura_informativa` `fi` on((`fi`.`id_parcial` = `p`.`id_parcial`))) left join `cordovezApp`.`factura_informativa_detalle` `fid` on((`fid`.`id_factura_informativa` = `fi`.`id_factura_informativa`))) left join `cordovezApp`.`detalle_pedido_factura` `dpf` on((`fid`.`detalle_pedido_factura` = `dpf`.`detalle_pedido_factura`))) left join `cordovezApp`.`producto` `pr` on((`pr`.`cod_contable` = `dpf`.`cod_contable`))) order by `p`.`fecha_llegada_cliente`,`p`.`nro_pedido` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_ice_r10`
--

/*!50001 DROP VIEW IF EXISTS `v_ice_r10`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_ice_r10` AS select replace(`o`.`nro_pedido`,'-','/') AS `nro_pedido`,`pr`.`nombre` AS `nombre`,`pr`.`cod_ice` AS `cod_ice`,`o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente`,`o`.`pais_origen` AS `pais_origen`,`dpf`.`nro_cajas` AS `nro_cajas`,`dpf`.`unidades` AS `unidades`,`dpf`.`fob_tasa_trimestral` AS `fob_tasa_trimestral`,'' AS `Name_exp_9`,`pr`.`capacidad_ml` AS `capacidad_ml`,`dpf`.`grado_alcoholico` AS `grado_alcoholico`,`dpf`.`ex_aduana_unitario` AS `ex_aduana_unitario`,`dpf`.`ice_especifico_unitario` AS `ice_especifico_unitario`,`dpf`.`ice_advalorem_unitario` AS `ice_advalorem_unitario`,`dpf`.`ice_unitario` AS `ice_unitario`,`dpf`.`total_ice` AS `total_ice`,`dpf`.`costo_total` AS `costo_total`,`dpf`.`costo_caja_final` AS `costo_caja_final`,substr(`o`.`nro_refrendo`,1,3) AS `digitos`,substr(`o`.`nro_refrendo`,5,4) AS `anio`,substr(`o`.`nro_refrendo`,10,2) AS `reg`,substr(`o`.`nro_refrendo`,13,8) AS `cons` from (((`cordovezApp`.`pedido` `o` left join `cordovezApp`.`pedido_factura` `pf` on((`pf`.`nro_pedido` = `o`.`nro_pedido`))) left join `cordovezApp`.`detalle_pedido_factura` `dpf` on((`pf`.`id_pedido_factura` = `dpf`.`id_pedido_factura`))) left join `cordovezApp`.`producto` `pr` on((`pr`.`cod_contable` = `dpf`.`cod_contable`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_producto_pedidos_R10_llegados`
--

/*!50001 DROP VIEW IF EXISTS `v_producto_pedidos_R10_llegados`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_producto_pedidos_R10_llegados` AS select `pf`.`nro_pedido` AS `nro_pedido`,`s`.`nombre` AS `nombre`,`pf`.`id_factura_proveedor` AS `id_factura_proveedor`,`o`.`nro_refrendo` AS `nro_refrendo`,`p`.`nombre` AS `producto`,`dpf`.`capacidad_ml` AS `capacidad_ml`,`dpf`.`grado_alcoholico` AS `grado_alcoholico`,`dpf`.`nro_cajas` AS `nro_cajas`,`dpf`.`unidades` AS `unidades`,`o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente` from ((((`cordovezApp`.`detalle_pedido_factura` `dpf` left join `cordovezApp`.`pedido_factura` `pf` on((`pf`.`id_pedido_factura` = `dpf`.`id_pedido_factura`))) left join `cordovezApp`.`proveedor` `s` on((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`))) left join `cordovezApp`.`pedido` `o` on((`o`.`nro_pedido` = `pf`.`nro_pedido`))) left join `cordovezApp`.`producto` `p` on((`p`.`cod_contable` = `dpf`.`cod_contable`))) where `dpf`.`id_pedido_factura` in (select `cordovezApp`.`pedido_factura`.`id_pedido_factura` from `cordovezApp`.`pedido_factura` where `cordovezApp`.`pedido_factura`.`nro_pedido` in (select `cordovezApp`.`pedido`.`nro_pedido` from `cordovezApp`.`pedido` where (`cordovezApp`.`pedido`.`regimen` = 10))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_productos_pedidos`
--

/*!50001 DROP VIEW IF EXISTS `v_productos_pedidos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_productos_pedidos` AS select `pf`.`nro_pedido` AS `nro_pedido`,`s`.`nombre` AS `nombre`,`pf`.`id_factura_proveedor` AS `id_factura_proveedor`,`o`.`nro_refrendo` AS `nro_refrendo`,`pr`.`nombre` AS `producto`,`dpf`.`capacidad_ml` AS `capacidad_ml`,`dpf`.`grado_alcoholico` AS `grado_alcoholico`,`dpf`.`nro_cajas` AS `nro_cajas`,`dpf`.`unidades` AS `unidades`,`o`.`fecha_llegada_cliente` AS `fecha_llegada_cliente` from ((((`cordovezApp`.`detalle_pedido_factura` `dpf` left join `cordovezApp`.`producto` `pr` on((`pr`.`cod_contable` = `dpf`.`cod_contable`))) left join `cordovezApp`.`pedido_factura` `pf` on((`pf`.`id_factura_proveedor` = `dpf`.`id_pedido_factura`))) left join `cordovezApp`.`proveedor` `s` on((`s`.`identificacion_proveedor` = `pf`.`identificacion_proveedor`))) left join `cordovezApp`.`pedido` `o` on((`pf`.`nro_pedido` = `o`.`nro_pedido`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_sgi_provisiones_pagos`
--

/*!50001 DROP VIEW IF EXISTS `v_sgi_provisiones_pagos`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_sgi_provisiones_pagos` AS select `gn`.`id_gastos_nacionalizacion` AS `id_gastos_nacionalizacion`,`gn`.`id_parcial` AS `id_parcial`,`gn`.`concepto` AS `concepto`,`gn`.`tipo` AS `tipo`,`gn`.`valor_provisionado` AS `valor_provisionado`,`gn`.`valor_ajuste` AS `valor_ajuste`,`gn`.`fecha` AS `fecha`,`gn`.`fecha_fin` AS `fecha_fin`,`gn`.`comentarios` AS `comentarios`,`gn`.`bg_closed` AS `bg_closed`,`gn`.`bg_is_visible_gi` AS `bg_is_visible_gi`,`gn`.`bg_iscontabilizado` AS `bg_iscontabilizado`,`gn`.`bg_iscontabilizado_por` AS `bg_iscontabilizado_por`,`gn`.`bg_isdrop` AS `bg_isdrop`,`gn`.`id_user` AS `id_user`,`gn`.`date_create` AS `date_create`,`gn`.`last_update` AS `last_update`,`gn`.`identificacion_proveedor` AS `identificacion_proveedor`,`gn`.`nro_pedido` AS `nro_pedido`,(select ifnull(sum(`ddp`.`valor`),0) from `cordovezApp`.`detalle_documento_pago` `ddp` where (`ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`)) AS `pago`,(`gn`.`valor_provisionado` - (select ifnull(sum(`ddp`.`valor`),0) from `cordovezApp`.`detalle_documento_pago` `ddp` where (`ddp`.`id_gastos_nacionalizacion` = `gn`.`id_gastos_nacionalizacion`))) AS `saldo` from ((`cordovezApp`.`gastos_nacionalizacion` `gn` left join `cordovezApp`.`parcial` `p` on(((`p`.`id_parcial` = `gn`.`id_parcial`) and (`gn`.`id_parcial` <> 0)))) left join `cordovezApp`.`pedido` `o` on((ifnull(`p`.`nro_pedido`,`gn`.`nro_pedido`) = `o`.`nro_pedido`))) order by `gn`.`tipo`,`gn`.`fecha`,`gn`.`concepto` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-09 18:09:40
