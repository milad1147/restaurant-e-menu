-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 28, 2014 at 10:58 PM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `tablet_choise`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
  `id_category` int(3) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` tinytext,
  `image_url` varchar(300) DEFAULT NULL,
  `parent_category` int(3) unsigned DEFAULT NULL,
  PRIMARY KEY (`id_category`),
  KEY `name` (`name`),
  KEY `parent_category` (`parent_category`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id_category`, `name`, `description`, `image_url`, `parent_category`) VALUES
(1, 'Предястия', 'Салати, мезета и други', NULL, NULL),
(2, 'Салати', 'Пресни салати', NULL, 1);

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

CREATE TABLE IF NOT EXISTS `item` (
  `id_item` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `price` decimal(3,2) NOT NULL,
  `short_description` tinytext NOT NULL,
  `description` text,
  `image_url` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id_item`),
  KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`id_item`, `name`, `price`, `short_description`, `description`, `image_url`) VALUES
(1, 'Шопска салата', 4.20, 'Краставици, домати, сирене', NULL, NULL),
(2, 'Овчарска салата', 5.80, 'с месо', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `item_category`
--

CREATE TABLE IF NOT EXISTS `item_category` (
  `id_item` int(4) unsigned NOT NULL,
  `id_category` int(3) unsigned NOT NULL,
  PRIMARY KEY (`id_item`,`id_category`),
  KEY `id_category` (`id_category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `item_category`
--

INSERT INTO `item_category` (`id_item`, `id_category`) VALUES
(1, 2),
(2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `item_status`
--

CREATE TABLE IF NOT EXISTS `item_status` (
  `id_status` int(1) unsigned NOT NULL AUTO_INCREMENT,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`id_status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `item_status`
--

INSERT INTO `item_status` (`id_status`, `status`) VALUES
(1, 'Not Ordered'),
(2, 'Ordered'),
(3, 'Delivered');

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE IF NOT EXISTS `order` (
  `id_order` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `table` int(3) unsigned NOT NULL,
  `is_finished` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_order`),
  KEY `table` (`table`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `order`
--

INSERT INTO `order` (`id_order`, `table`, `is_finished`) VALUES
(1, 15, 1),
(2, 2, 0);

-- --------------------------------------------------------

--
-- Table structure for table `order_item`
--

CREATE TABLE IF NOT EXISTS `order_item` (
  `id_order_item` int(14) unsigned NOT NULL AUTO_INCREMENT,
  `id_order` int(10) unsigned NOT NULL,
  `id_item` int(4) unsigned NOT NULL,
  `time_ordered` timestamp NULL DEFAULT NULL,
  `status` int(1) unsigned NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_order_item`),
  KEY `status` (`status`),
  KEY `id_order` (`id_order`),
  KEY `id_item` (`id_item`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `order_item`
--

INSERT INTO `order_item` (`id_order_item`, `id_order`, `id_item`, `time_ordered`, `status`) VALUES
(1, 1, 2, '2014-05-28 20:57:04', 3),
(2, 1, 2, '2014-05-28 20:57:04', 3),
(3, 2, 1, '2014-05-28 20:57:42', 2),
(4, 2, 2, '2014-05-28 20:57:42', 3);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE IF NOT EXISTS `roles` (
  `id_role` int(2) NOT NULL AUTO_INCREMENT,
  `role` varchar(10) NOT NULL,
  PRIMARY KEY (`id_role`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id_role`, `role`) VALUES
(1, 'Admin'),
(2, 'Waiter');

-- --------------------------------------------------------

--
-- Table structure for table `uers`
--

CREATE TABLE IF NOT EXISTS `uers` (
  `id_user` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `password` varchar(40) NOT NULL,
  PRIMARY KEY (`id_user`),
  KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `uers`
--

INSERT INTO `uers` (`id_user`, `username`, `name`, `password`) VALUES
(1, 'vankata', 'Ivan Ivanov', '40bd001563085fc35165329ea1ff5c5ecbdbbeef'),
(2, 'mari', 'Мария', '40bd001563085fc35165329ea1ff5c5ecbdbbeef');

-- --------------------------------------------------------

--
-- Table structure for table `user_roles`
--

CREATE TABLE IF NOT EXISTS `user_roles` (
  `id_user` int(10) unsigned NOT NULL,
  `id_role` int(2) NOT NULL,
  PRIMARY KEY (`id_user`,`id_role`),
  KEY `id_role` (`id_role`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user_roles`
--

INSERT INTO `user_roles` (`id_user`, `id_role`) VALUES
(1, 1),
(1, 2),
(2, 2);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `category`
--
ALTER TABLE `category`
  ADD CONSTRAINT `category_ibfk_1` FOREIGN KEY (`parent_category`) REFERENCES `category` (`id_category`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `item_category`
--
ALTER TABLE `item_category`
  ADD CONSTRAINT `item_category_ibfk_2` FOREIGN KEY (`id_item`) REFERENCES `item` (`id_item`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `item_category_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `category` (`id_category`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order_item`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `order_item_ibfk_3` FOREIGN KEY (`id_order`) REFERENCES `order` (`id_order`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_item_ibfk_1` FOREIGN KEY (`status`) REFERENCES `item_status` (`id_status`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_item_ibfk_2` FOREIGN KEY (`id_item`) REFERENCES `item` (`id_item`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_roles`
--
ALTER TABLE `user_roles`
  ADD CONSTRAINT `user_roles_ibfk_2` FOREIGN KEY (`id_role`) REFERENCES `roles` (`id_role`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `user_roles_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `uers` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
