-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 22, 2021 at 10:20 AM
-- Server version: 10.5.9-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `praktyki`
--

-- --------------------------------------------------------

--
-- Table structure for table `configuration`
--

CREATE TABLE `configuration` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `start_time` datetime NOT NULL DEFAULT current_timestamp(),
  `stop_time` datetime NOT NULL,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `run_id` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='A table for saving information about output files';

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `file_name`, `start_time`, `stop_time`, `remarks`, `run_id`) VALUES
(1, 'test-file', '2021-03-16 14:05:00', '2021-03-16 14:15:00', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackCalibratorPar`
--

CREATE TABLE `SFibersStackCalibratorPar` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackCalibratorPar`
--

INSERT INTO `SFibersStackCalibratorPar` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-16 13:42:09', '2021-03-16 14:17:09', 2, NULL),
(3, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackDDLookupTable`
--

CREATE TABLE `SFibersStackDDLookupTable` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackDDLookupTable`
--

INSERT INTO `SFibersStackDDLookupTable` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-16 13:42:09', '2021-03-16 14:17:09', 2, NULL),
(3, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackDDUnpackerPar`
--

CREATE TABLE `SFibersStackDDUnpackerPar` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackDDUnpackerPar`
--

INSERT INTO `SFibersStackDDUnpackerPar` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-16 13:42:09', '2021-03-16 14:02:09', 2, NULL),
(3, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackDigitizerPar`
--

CREATE TABLE `SFibersStackDigitizerPar` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackDigitizerPar`
--

INSERT INTO `SFibersStackDigitizerPar` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, '', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, '', '2021-03-16 13:42:09', '2021-03-16 14:02:09', 2, NULL),
(3, '', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, '', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, '', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, '', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, '', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, '', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, '', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackGeomPar`
--

CREATE TABLE `SFibersStackGeomPar` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackGeomPar`
--

INSERT INTO `SFibersStackGeomPar` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-16 13:42:09', '2021-03-16 14:02:09', 2, NULL),
(3, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackHitFinderFiberPar`
--

CREATE TABLE `SFibersStackHitFinderFiberPar` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackHitFinderFiberPar`
--

INSERT INTO `SFibersStackHitFinderFiberPar` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, '', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, '', '2021-03-16 13:42:09', '2021-03-16 14:02:09', 2, NULL),
(3, '', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, '', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, '', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, '', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, '', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, '', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, '', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `SFibersStackHitFinderPar`
--

CREATE TABLE `SFibersStackHitFinderPar` (
  `id` int(10) UNSIGNED NOT NULL,
  `parameters` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `valid_from` datetime NOT NULL DEFAULT current_timestamp(),
  `valid_to` datetime NOT NULL,
  `version` int(11) NOT NULL DEFAULT 1,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='An abstract base table which reflects the structure of a single configuration.';

--
-- Dumping data for table `SFibersStackHitFinderPar`
--

INSERT INTO `SFibersStackHitFinderPar` (`id`, `parameters`, `valid_from`, `valid_to`, `version`, `remarks`) VALUES
(1, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-16 11:27:59', '2021-03-16 11:47:59', 1, NULL),
(2, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-16 13:42:09', '2021-03-16 14:02:09', 2, NULL),
(3, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-16 14:00:40', '2021-03-16 14:20:40', 3, NULL),
(4, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-17 09:24:31', '2021-03-17 09:44:31', 4, NULL),
(5, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-17 19:01:39', '2021-03-17 19:21:39', 1, NULL),
(6, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-19 12:13:23', '2021-03-19 12:33:23', 1, NULL),
(7, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-21 22:00:00', '2021-03-21 23:00:00', 1, NULL),
(8, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 1, 'Some testing conf with remarks'),
(10, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `configuration`
--
ALTER TABLE `configuration`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_run` (`run_id`,`start_time`,`stop_time`);

--
-- Indexes for table `SFibersStackCalibratorPar`
--
ALTER TABLE `SFibersStackCalibratorPar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SFibersStackDDLookupTable`
--
ALTER TABLE `SFibersStackDDLookupTable`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SFibersStackDDUnpackerPar`
--
ALTER TABLE `SFibersStackDDUnpackerPar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SFibersStackDigitizerPar`
--
ALTER TABLE `SFibersStackDigitizerPar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SFibersStackGeomPar`
--
ALTER TABLE `SFibersStackGeomPar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SFibersStackHitFinderFiberPar`
--
ALTER TABLE `SFibersStackHitFinderFiberPar`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `SFibersStackHitFinderPar`
--
ALTER TABLE `SFibersStackHitFinderPar`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `configuration`
--
ALTER TABLE `configuration`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `SFibersStackCalibratorPar`
--
ALTER TABLE `SFibersStackCalibratorPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SFibersStackDDLookupTable`
--
ALTER TABLE `SFibersStackDDLookupTable`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SFibersStackDDUnpackerPar`
--
ALTER TABLE `SFibersStackDDUnpackerPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SFibersStackDigitizerPar`
--
ALTER TABLE `SFibersStackDigitizerPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SFibersStackGeomPar`
--
ALTER TABLE `SFibersStackGeomPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SFibersStackHitFinderFiberPar`
--
ALTER TABLE `SFibersStackHitFinderFiberPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `SFibersStackHitFinderPar`
--
ALTER TABLE `SFibersStackHitFinderPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
