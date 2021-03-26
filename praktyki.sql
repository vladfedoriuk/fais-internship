-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 26, 2021 at 04:49 PM
-- Server version: 10.5.9-MariaDB
-- PHP Version: 8.0.3

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
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$tbT4KB5bLfxF$xOHe+tangRidcfkrRZ1iByVzt3q4XpR5bIcwwvxPFO8=', '2021-03-25 08:31:55.467186', 1, 'admin', '', '', 'vlad.fedoriuk2000@gmail.com', 1, 1, '2021-03-25 08:30:43.089657');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'core', 'sfibersstackcalibratorpar'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-03-25 08:29:55.245733'),
(2, 'auth', '0001_initial', '2021-03-25 08:29:55.576392'),
(3, 'admin', '0001_initial', '2021-03-25 08:29:56.613746'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-03-25 08:29:56.885725'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-03-25 08:29:56.896804'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-03-25 08:29:57.025450'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-03-25 08:29:57.139458'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-03-25 08:29:57.178595'),
(9, 'auth', '0004_alter_user_username_opts', '2021-03-25 08:29:57.202593'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-03-25 08:29:57.308788'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-03-25 08:29:57.314605'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-03-25 08:29:57.340270'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-03-25 08:29:57.375611'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-03-25 08:29:57.402489'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-03-25 08:29:57.431240'),
(16, 'auth', '0011_update_proxy_permissions', '2021-03-25 08:29:57.447314'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-03-25 08:29:57.475156'),
(18, 'sessions', '0001_initial', '2021-03-25 08:29:57.521481');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('33nvt1kpzl29joeaf54axgs4g0tvzp1u', '.eJxVjEEOwiAQRe_C2pAODJS6dO8ZCDCDVA0kpV0Z765NutDtf-_9l_BhW4vfOi9-JnEWIE6_WwzpwXUHdA_11mRqdV3mKHdFHrTLayN-Xg7376CEXr61sg4AWNvs0GiFOiS2lsakNaQJdLSIpFyIA9IInJlRwZCyo8kYBCveH7sLNws:1lPLPH:S-4Hj4gaEoWqq_eIpvxKPF--psvEBsIpq6xiVHQwhjA', '2021-04-08 08:31:55.471593');

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `start_time` datetime NOT NULL DEFAULT current_timestamp(),
  `stop_time` datetime NOT NULL,
  `remarks` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `run_id` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='A table for saving information about output files';

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `file_name`, `start_time`, `stop_time`, `remarks`, `run_id`) VALUES
(1, 'test-file', '2021-03-16 14:05:00', '2021-03-16 14:15:00', NULL, 1),
(2, 'some-other-test-file', '2021-03-22 13:20:29', '2021-03-22 14:19:48', NULL, 2);

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
(10, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(11, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 1, NULL),
(12, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, '# m  l  f  s        adc_g   adc_o   time_o\n  0  0  0  l        1.0     0.0     0\n  0  0  0  r        1.0     0.0     0\n  0  0  1  l        1.0     0.0     0\n  0  0  1  r        1.0     0.0     0\n  0  0  2  l        1.0     0.0     0\n  0  0  2  r        1.0     0.0     0\n  0  0  3  l        1.0     0.0     0\n  0  0  3  r        1.0     0.0     0', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

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
(10, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(11, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 1, NULL),
(12, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, '#   FTAB id channel         mod     layer   fiber   side l/r\n0x1000      0               0       0       0       l\n0x1000      1               0       0       0       r\n0x1000      2               0       0       1       l\n0x1000      3               0       0       1       r\n0x1000      4               0       0       2       l\n0x1000      5               0       0       2       r\n0x1000      6               0       0       3       l\n0x1000      7               0       0       3       r', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

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
(10, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(11, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 1, NULL),
(12, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, 'fThreshold: Float_t \\\n-4 -4 -4 -4 -4 -4 -4 -4 \\\n-4 -4 -4 -4 -4 -4 -4 -4\nnPolarity: Int_t 0\nnAnaMode: Int_t 0\nnIntMode: Int_t 150\nnDeadTime: Int_t 400\nfVetoThreshold: Float_t \\\n15 15 15 15 15 15 15 15 \\\n15 15 15 15 15 15 15 15\nfBLMode: Int_t \\\n0 0 0 0 0 0 0 0 \\\n0 0 0 0 0 0 0 0', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

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
(10, '', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(11, '', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 1, NULL),
(12, '', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, '', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

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
(10, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(11, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 1, NULL),
(12, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, 'nModules: Int_t 2\nnLayers: Int_t 10 30\nnFibers: Int_t \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76 \\\n76 76 76 76 76 76 76 76 76 76\nfLayerRotation: Float_t \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90 \\\n0 90 0 90 0 90 0 90 0 90\nfFiberOffsetX: Float_t \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 \\\n-37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5 -37.5\nfFiberOffsetY: Float_t \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5 \\\n10.5 11.5 12.5 13.5 14.5 15.5 16.5 17.5 18.5 19.5 \\\n20.5 21.5 22.5 23.5 24.5 25.5 26.5 27.5 28.5 29.5\nfFibersPitch: Float_t \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1 \\\n1 1 1 1 1 1 1 1 1 1', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

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
(10, '', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(11, '', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 1, NULL),
(12, '', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, '', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

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
(10, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-22 11:14:00', '2021-03-22 12:14:00', 2, NULL),
(12, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 7, NULL),
(13, 'fA0: Float_t -0.000540944\nfLambda: Float_t 118.809', '2021-03-16 14:05:00', '2021-03-22 13:20:29', 13, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `configuration`
--
ALTER TABLE `configuration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

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
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `SFibersStackDDLookupTable`
--
ALTER TABLE `SFibersStackDDLookupTable`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `SFibersStackDDUnpackerPar`
--
ALTER TABLE `SFibersStackDDUnpackerPar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `SFibersStackDigitizerPar`
--
ALTER TABLE `SFibersStackDigitizerPar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `SFibersStackGeomPar`
--
ALTER TABLE `SFibersStackGeomPar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `SFibersStackHitFinderFiberPar`
--
ALTER TABLE `SFibersStackHitFinderFiberPar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- Indexes for table `SFibersStackHitFinderPar`
--
ALTER TABLE `SFibersStackHitFinderPar`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_version_date` (`valid_from`,`version`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `configuration`
--
ALTER TABLE `configuration`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `SFibersStackCalibratorPar`
--
ALTER TABLE `SFibersStackCalibratorPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `SFibersStackDDLookupTable`
--
ALTER TABLE `SFibersStackDDLookupTable`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `SFibersStackDDUnpackerPar`
--
ALTER TABLE `SFibersStackDDUnpackerPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `SFibersStackDigitizerPar`
--
ALTER TABLE `SFibersStackDigitizerPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `SFibersStackGeomPar`
--
ALTER TABLE `SFibersStackGeomPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `SFibersStackHitFinderFiberPar`
--
ALTER TABLE `SFibersStackHitFinderFiberPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `SFibersStackHitFinderPar`
--
ALTER TABLE `SFibersStackHitFinderPar`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
