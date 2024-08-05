-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2024 at 12:18 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `social_network_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customuser`
--

CREATE TABLE `myapp_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `name` varchar(255) NOT NULL,
  `logged_in` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_customuser`
--

INSERT INTO `myapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `email`, `is_active`, `is_staff`, `name`, `logged_in`) VALUES
(1, 'pbkdf2_sha256$720000$HBwFTB8k4n3etUcy8vweAn$y7ANpJEWSU1FaSrcO6wJcv7YPNlZUe+xwDg/YXg4Kos=', NULL, 0, 'shweta@example.com', 1, 0, 'shweta', NULL),
(2, 'pbkdf2_sha256$720000$vYGv73B0oXw79GTezhjf1B$iBtbEDa7JCQXG12bIjx15EL9f6H6cZ3bz+SG9j7VTJQ=', NULL, 0, 'khushboo@example.com', 1, 0, 'khushboo', NULL),
(3, 'pbkdf2_sha256$720000$L3BvG1OHuVuZ2Wjaex5fZg$S/ScZ1zVp0SHrfQw3Uqh2GxoJRQDlw7mb9kPZbasx9U=', NULL, 0, 'smita@example.com', 1, 0, 'smita', NULL),
(4, 'pbkdf2_sha256$720000$jHJiAOMhHnh3EN36S6rWZ0$MwZKs21sTsHQoZk8lHKOolTpagcnx4qI8jGU8xEtnKE=', NULL, 0, 'avika@example.com', 1, 0, 'avika', NULL),
(5, 'pbkdf2_sha256$720000$fOMzr2XcnUfyMC2gzJ27Er$Kl7STGX/pdOl4X+uzR5GWzwysmCNo86HCVEx4VWsGjo=', NULL, 0, 'anjani@example.com', 1, 0, 'anjani', NULL),
(6, 'pbkdf2_sha256$720000$JteNMhiaaMe4g3Osxij1pj$Cq+Fjqe91TajgvDqr1j0SvaKBX2GB7839L9HXwi9Z8Y=', NULL, 0, 'prakriti@example.com', 1, 0, 'prakriti', NULL),
(7, 'pbkdf2_sha256$720000$KMa4ixSVVOgx4U7FU7CxsB$Svm8h99wWntM/an1+Y+BCoqaL17xiiWAWQO4C6JHpb0=', NULL, 0, 'arna@example.com', 1, 0, 'arna', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `myapp_customuser`
--
ALTER TABLE `myapp_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `myapp_customuser`
--
ALTER TABLE `myapp_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
