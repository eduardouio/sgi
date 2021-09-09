-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 02, 2021 at 03:27 PM
-- Server version: 5.7.21
-- PHP Version: 7.0.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cordovezApp`
--

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id_user` smallint(6) NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `cargo` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(120) NOT NULL,
  `usertype` enum('L1','L2','L3') NOT NULL COMMENT 'L1 Administrador; L2 Ingreso Data; L3 Visualizacion',
  `last_login` datetime DEFAULT NULL,
  `date_create` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_update` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Se registran todos los impuestos que existen en una nacionalizacion, solo impuestos de la SENAE';

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id_user`, `nombres`, `email`, `cargo`, `username`, `password`, `usertype`, `last_login`, `date_create`, `last_update`) VALUES
(3, 'ADRIAN CARDENAS', 'acardenas@vinesa.com.ec', 'STAFF', 'acardenas', 'RZjDbQo9p8exSPBMe9Pgn2SJ+cL9Njn718JA3oiJ10E=', 'L1', '2019-02-14 15:29:44', '2017-10-17 14:33:06', NULL),
(4, 'ALEXANDRA LEON', 'info6@vinesa.com.ec', 'STAFF', 'aleon', 'n2mO6XIyiy1TTYk1twLHrVjDV+VfZwVZTKZh+aghilM=', 'L1', '2021-05-31 12:39:14', '2017-10-17 14:33:06', NULL),
(5, 'ALEXANDRA VARGAS', 'info7@vinesa.com.ec', 'STAFF', 'avargas', 'wahlp6v48H/KWHQd+pNhcC2qSf3b3OfJ867fRjtD61M=', 'L1', NULL, '2017-10-17 14:33:06', NULL),
(29, 'ALEXANDRA YANEZ', 'ayanez@vinesa.com.ec', 'STAFF', 'ayanez', 'jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=', 'L1', '2021-06-02 09:44:28', '2019-04-02 05:00:00', NULL),
(6, 'CECILIA FELIX', 'cfelix@vinesa.com.ec', 'STAFF', 'cfelix', 'au6/iMXeSD+6ordxivCvPvqaKp4B3Wy2HcCv1Y7wFYk=', 'L1', '2019-12-23 16:08:41', '2017-10-17 14:33:06', NULL),
(1, 'ADMINISTRADOR', 'usuario@gmail.com', 'STAFF', 'cordovez', 'erdYyo1ERYzIcgXJsjM6bRkmFq5JecqAhJzPmFqMPa8=', 'L1', '2021-05-28 12:50:02', '2017-09-07 14:46:27', NULL),
(27, 'DANIEL MAZA', 'bodega1@vinesa.com.ec', 'BODEGA', 'dmaza', 'EPGAYnJDjKfRjOLMHuWFpo0y9q6ZOJIKeBT9aBBvfbI=', 'L3', '2021-05-03 15:57:46', '2018-11-07 15:08:16', NULL),
(7, 'DAVID PEREZ', 'info5@vinesa.com.ec', 'STAFF', 'dperez', '', 'L1', '2018-01-09 18:01:01', '2017-10-17 14:33:06', NULL),
(17, 'ELIZABETH SALA', 'info20@vinesa.com', 'USUARIO ADICIONAL', 'esala', 'wahlp6v48H/KWHQd+pNhcC2qSf3b3OfJ867fRjtD61M=', 'L2', '2019-03-11 11:26:02', '2018-07-05 22:19:28', NULL),
(25, 'EDUARDO VILLOTA', 'eduardouio7@gmail.com', 'STAFF', 'evillota', 'erdYyo1ERYzIcgXJsjM6bRkmFq5JecqAhJzPmFqMPa8=', 'L1', '2020-11-16 09:29:34', '2017-09-07 14:46:27', NULL),
(28, 'FELIPE CORDOVEZ', 'fcordovez@vinesa.com.ec', 'STAFF', 'fcordovez', 'jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=', 'L1', '2018-11-07 12:17:00', '2017-09-07 14:46:27', NULL),
(8, 'GABRIELA ALARCON', 'galarcon@vinesa.com.ec', 'STAFF', 'galarcon', '6NO8JgF7HM+5oD5KYJKDafc21rRcTPVMLr1Jojb9W6s=', 'L1', '2021-03-18 10:27:40', '2017-10-17 14:33:06', NULL),
(9, 'JEANNETH CARRILLO', 'jcarrillo@vinesa.com.ec', 'STAFF', 'jcarrillo', '6rbBEcnvv/xN7lufGVHMhcJOWcWrU7GUE8m0A6ag0vc=', 'L1', '2019-02-07 15:13:07', '2017-10-17 14:33:06', NULL),
(10, 'JORGE CHULDE', 'jchulde@vinesa.com.ec ', 'STAFF', 'jchulde', '', 'L1', '2018-06-11 23:22:10', '2017-10-17 14:33:06', NULL),
(15, 'JONATHAN CRUZ', 'info9@vinesa.com.ec', 'STAFF', 'jcruz', 'jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=', 'L1', '2021-06-01 09:38:00', '2017-10-17 14:33:06', NULL),
(26, ' JEFERSON PACHECO', 'jpacheco@vinesa.com', 'STAFF', 'jpacheco', 'LmRXfBDXxb5XWDeH5LVME1hS+H7/4TE3r2gxkTusu7Q=', 'L1', '2018-11-26 12:14:52', '2017-09-07 14:46:27', NULL),
(23, 'Karla Lema', 'klema@vinesa.com.ec', 'STAFF', 'klema', 'Sc3ELMirM33H/ouxVOD5xdGh6pgEF4itVqlGog5KgTg=', 'L1', '2019-02-01 11:01:27', '2017-10-17 14:33:06', NULL),
(18, 'KAROL TOAPANTA', 'info19@vinesa.com.', 'Usuario Adicional', 'ktoapanta', 'jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=', 'L2', '2020-01-31 11:29:51', '2018-07-05 22:19:28', NULL),
(33, 'LORENA RODRIGUEZ', 'lrodriguez@vinesa.com.ec', 'STAFF', 'lrodriguez', 'sevQ0S4uFBbNMD6+9xmUyW9kppwqGnmLxrDJI0REFak=', 'L1', '2021-05-31 13:50:01', '2017-09-07 14:46:27', NULL),
(24, 'Lizbeth Santamaria', 'lsantamaria@vinesa.com.ec', 'STAFF', 'lsantamaria', 'AETc2dmhOCNF3MeooOTkMo4cmaA2T816DpOOkGHW8g0=', 'L1', '2018-10-29 19:26:50', '2017-10-17 14:33:06', NULL),
(30, 'MARJORIE CANO', 'mcano@vinlitoral.com.ec', 'STAFF', 'mcano', 'jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=', 'L1', '2020-06-11 12:18:09', '2017-09-07 14:46:27', NULL),
(11, 'MARIA ELENA SANTI', 'msanti@vinesa.com.ec', 'STAFF', 'msanti', 'fUWznJaK7g10gvB21c3gh3BIUgnm+amBB1wYRhwKGL0=', 'L1', '2020-08-28 10:02:07', '2017-10-17 14:33:06', NULL),
(12, 'MARIA ELENA TERAN', 'mteran@vinesa.com.ec', 'STAFF', 'mteran', 'XnCOFXzvzFGHXS/GZ5kVEZ9PAE2N+oCeqydK87yGuwo=', 'L1', '2021-05-26 11:14:09', '2017-10-17 14:33:06', NULL),
(31, 'PATRICIA RAMOS', 'pramos@vinesa.com.ec', 'STAFF', 'pramos', 'jR0TWnF/TS81Xr7h9LASq4yRY/sLR9dAUwC+EwI9mE0=', 'L1', '2019-12-28 17:46:46', '2017-09-07 14:46:27', NULL),
(2, 'RUTH ANDRADE', 'Randrade@vinesa.com.ec', 'STAFF', 'randrade', 'YIcCKnZT3wfhFSyG0KfXB0PlaEbXuvKsckOxD8/Ct9E=', 'L1', '2018-08-16 16:17:47', '2017-10-17 14:19:41', NULL),
(16, 'Rocío Villegas', 'rvillegas@vinesa.com.ec ', 'STAFF', 'rvillegas', '', 'L1', '2018-10-15 13:27:50', '2017-10-17 14:33:06', NULL),
(32, 'VERONICA HEREDIA', 'vheredia@vinesa.com.ec', 'STAFF', 'vheredia', 'RZjDbQo9p8exSPBMe9Pgn2SJ+cL9Njn718JA3oiJ10E=', 'L1', '2021-06-01 17:22:18', '2017-10-17 14:33:06', NULL),
(13, 'VERONICA PONCE', 'info2@vinesa.com.ec', 'STAFF', 'vponce', 'wahlp6v48H/KWHQd+pNhcC2qSf3b3OfJ867fRjtD61M=', 'L1', NULL, '2017-10-17 14:33:06', NULL),
(22, 'Yovana Paccha', 'infoc1@vinesa.com.ec', 'STAFF', 'ypaccha', 'OYxePHUJpAuO+RWU798iZB3ujwzxbqDxBF0N8pC8lok=', 'L1', '2020-11-05 11:21:51', '2017-10-17 14:33:06', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`username`),
  ADD UNIQUE KEY `id_user` (`id_user`),
  ADD UNIQUE KEY `nombres` (`nombres`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_user` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;