-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 08, 2023 at 02:39 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectairport`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline`
--

CREATE TABLE `airline` (
  `name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airlinestaff`
--

CREATE TABLE `airlinestaff` (
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `date_of_birth` date NOT NULL,
  `airline_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airlinestaffemails`
--

CREATE TABLE `airlinestaffemails` (
  `staff_username` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airlinestaffphonenumbers`
--

CREATE TABLE `airlinestaffphonenumbers` (
  `staff_username` varchar(225) NOT NULL,
  `phone_number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airplane`
--

CREATE TABLE `airplane` (
  `id` int(11) NOT NULL,
  `num_of_seats` int(11) NOT NULL,
  `manufacturer` varchar(225) NOT NULL,
  `model_num` int(11) NOT NULL,
  `manufacture_date` date NOT NULL,
  `age` int(11) NOT NULL,
  `airline_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

CREATE TABLE `airport` (
  `code` varchar(225) NOT NULL,
  `name` varchar(225) NOT NULL,
  `city` varchar(225) NOT NULL,
  `country` varchar(225) NOT NULL,
  `num_of_terminals` int(11) DEFAULT NULL,
  `type` varchar(225) DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `email` varchar(225) NOT NULL,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `passport_num` int(11) NOT NULL,
  `passport_expiration` date NOT NULL,
  `passport_country` varchar(225) NOT NULL,
  `date_of_birth` date NOT NULL,
  `building_num` int(11) NOT NULL,
  `street` varchar(225) NOT NULL,
  `apt_num` int(11) NOT NULL,
  `city` varchar(225) NOT NULL,
  `state` varchar(225) NOT NULL,
  `zip` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customerphonenumbers`
--

CREATE TABLE `customerphonenumbers` (
  `customer_email` varchar(225) NOT NULL,
  `phone_number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `flight`
--

CREATE TABLE `flight` (
  `num` int(11) NOT NULL,
  `dep_date` date NOT NULL,
  `dep_time` time NOT NULL,
  `arr_time` time NOT NULL,
  `arr_date` date NOT NULL,
  `base_price` float NOT NULL,
  `airplane_id` int(11) NOT NULL,
  `airline_name` varchar(225) NOT NULL,
  `dep_airport` varchar(225) NOT NULL,
  `arr_airport` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `maintenance`
--

CREATE TABLE `maintenance` (
  `start_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_date` date NOT NULL,
  `end_time` time NOT NULL,
  `airplane_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `purchasehistory`
--

CREATE TABLE `purchasehistory` (
  `customer_email` varchar(225) NOT NULL,
  `purchase_time` time NOT NULL,
  `card_num` bigint(255) NOT NULL,
  `exp_date` date NOT NULL,
  `purchase_date` date NOT NULL,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `name_on_card` varchar(225) NOT NULL,
  `date_of_birth` date NOT NULL,
  `card_type` varchar(225) NOT NULL,
  `ticket_id` int(11) NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `customer_email` varchar(225) NOT NULL,
  `flight_num` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` mediumtext NOT NULL,
  `dep_date` date NOT NULL,
  `dep_time` time NOT NULL,
  `airline_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `id` int(11) NOT NULL,
  `price` float NOT NULL,
  `flight_num` int(11) NOT NULL,
  `flight_dep_date` date NOT NULL,
  `flight_dep_time` time NOT NULL,
  `airline_name` varchar(225) NOT NULL,
  `customer_email` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airline`
--
ALTER TABLE `airline`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `airlinestaff`
--
ALTER TABLE `airlinestaff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airlinestaffemails`
--
ALTER TABLE `airlinestaffemails`
  ADD PRIMARY KEY (`staff_username`,`email`);

--
-- Indexes for table `airlinestaffphonenumbers`
--
ALTER TABLE `airlinestaffphonenumbers`
  ADD PRIMARY KEY (`staff_username`,`phone_number`);

--
-- Indexes for table `airplane`
--
ALTER TABLE `airplane`
  ADD PRIMARY KEY (`id`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `airport`
--
ALTER TABLE `airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `customerphonenumbers`
--
ALTER TABLE `customerphonenumbers`
  ADD PRIMARY KEY (`customer_email`,`phone_number`);

--
-- Indexes for table `flight`
--
ALTER TABLE `flight`
  ADD PRIMARY KEY (`num`,`dep_date`,`dep_time`,`airline_name`),
  ADD KEY `airplane_id` (`airplane_id`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `dep_airport` (`dep_airport`),
  ADD KEY `arr_airport` (`arr_airport`);

--
-- Indexes for table `maintenance`
--
ALTER TABLE `maintenance`
  ADD PRIMARY KEY (`start_date`,`start_time`,`end_date`,`end_time`,`airplane_id`),
  ADD KEY `airplane_id` (`airplane_id`);

--
-- Indexes for table `purchasehistory`
--
ALTER TABLE `purchasehistory`
  ADD PRIMARY KEY (`customer_email`,`ticket_id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`customer_email`,`flight_num`,`dep_date`,`dep_time`,`airline_name`),
  ADD KEY `flight_num` (`flight_num`,`dep_date`,`dep_time`),
  ADD KEY `reviews_ibfk_3` (`airline_name`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `flight_num` (`flight_num`,`flight_dep_date`,`flight_dep_time`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airlinestaff`
--
ALTER TABLE `airlinestaff`
  ADD CONSTRAINT `airlinestaff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `airlinestaffemails`
--
ALTER TABLE `airlinestaffemails`
  ADD CONSTRAINT `airlinestaffemails_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `airlinestaff` (`username`);

--
-- Constraints for table `airlinestaffphonenumbers`
--
ALTER TABLE `airlinestaffphonenumbers`
  ADD CONSTRAINT `airlinestaffphonenumbers_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `airlinestaff` (`username`);

--
-- Constraints for table `airplane`
--
ALTER TABLE `airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `customerphonenumbers`
--
ALTER TABLE `customerphonenumbers`
  ADD CONSTRAINT `customerphonenumbers_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`);

--
-- Constraints for table `flight`
--
ALTER TABLE `flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airplane_id`) REFERENCES `airplane` (`id`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`dep_airport`) REFERENCES `airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`arr_airport`) REFERENCES `airport` (`code`);

--
-- Constraints for table `maintenance`
--
ALTER TABLE `maintenance`
  ADD CONSTRAINT `maintenance_ibfk_1` FOREIGN KEY (`airplane_id`) REFERENCES `airplane` (`id`);

--
-- Constraints for table `purchasehistory`
--
ALTER TABLE `purchasehistory`
  ADD CONSTRAINT `purchasehistory_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`),
  ADD CONSTRAINT `purchasehistory_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `ticket` (`id`);

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `customer` (`email`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`flight_num`,`dep_date`,`dep_time`) REFERENCES `flight` (`num`, `dep_date`, `dep_time`),
  ADD CONSTRAINT `reviews_ibfk_3` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`flight_num`,`flight_dep_date`,`flight_dep_time`) REFERENCES `flight` (`num`, `dep_date`, `dep_time`),
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `airline` (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
