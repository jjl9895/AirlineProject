-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 30, 2023 at 11:32 PM
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
-- Database: `AirportProject`
--

-- --------------------------------------------------------

--
-- Table structure for table `Airline`
--

CREATE TABLE `Airline` (
  `name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Airline`
--

INSERT INTO `Airline` (`name`) VALUES
('Air Canada'),
('American'),
('Delta'),
('Emirates'),
('JetBlue'),
('Southwest');

-- --------------------------------------------------------

--
-- Table structure for table `AirlineStaff`
--

CREATE TABLE `AirlineStaff` (
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `first_name` varchar(225) NOT NULL,
  `last_name` varchar(225) NOT NULL,
  `date_of_birth` date NOT NULL,
  `airline_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `AirlineStaff`
--

INSERT INTO `AirlineStaff` (`username`, `password`, `first_name`, `last_name`, `date_of_birth`, `airline_name`) VALUES
('iloveplanes123', '12345678910', 'Ishaan', 'Poojari', '2004-04-08', 'JetBlue');

-- --------------------------------------------------------

--
-- Table structure for table `AirlineStaffEmails`
--

CREATE TABLE `AirlineStaffEmails` (
  `staff_username` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `AirlineStaffEmails`
--

INSERT INTO `AirlineStaffEmails` (`staff_username`, `email`) VALUES
('iloveplanes123', 'sigma@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `airlinestaffphonenumbers`
--

CREATE TABLE `airlinestaffphonenumbers` (
  `staff_username` varchar(225) NOT NULL,
  `phone_number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `airlinestaffphonenumbers`
--

INSERT INTO `airlinestaffphonenumbers` (`staff_username`, `phone_number`) VALUES
('iloveplanes123', '9191111918');

-- --------------------------------------------------------

--
-- Table structure for table `Airplane`
--

CREATE TABLE `Airplane` (
  `id` int(11) NOT NULL,
  `num_of_seats` int(11) NOT NULL,
  `manufacturer` varchar(225) NOT NULL,
  `model_num` int(11) NOT NULL,
  `manufacture_date` date NOT NULL,
  `age` int(11) NOT NULL,
  `airline_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Airplane`
--

INSERT INTO `Airplane` (`id`, `num_of_seats`, `manufacturer`, `model_num`, `manufacture_date`, `age`, `airline_name`) VALUES
(22982, 853, 'AirBus', 380, '2001-08-07', 22, 'Emirates'),
(156253, 200, 'Boeing', 646, '2004-01-22', 19, 'Emirates'),
(434343, 240, 'Boeing', 878, '2004-04-23', 19, 'Air Canada'),
(758746, 410, 'Boeing', 747, '2004-01-23', 19, 'Air Canada'),
(900111, 410, 'Boeing', 747, '2022-01-23', 1, 'JetBlue');

-- --------------------------------------------------------

--
-- Table structure for table `Airport`
--

CREATE TABLE `Airport` (
  `code` varchar(225) NOT NULL,
  `name` varchar(225) NOT NULL,
  `city` varchar(225) NOT NULL,
  `country` varchar(225) NOT NULL,
  `num_of_terminals` int(11) NOT NULL,
  `type` varchar(225) NOT NULL
) ;

--
-- Dumping data for table `Airport`
--

INSERT INTO `Airport` (`code`, `name`, `city`, `country`, `num_of_terminals`, `type`) VALUES
('ATL', 'Hartsfield-Jackson', 'Atlanta', 'USA', 2, 'Domestic'),
('DEN', 'Denver', 'Denver', 'USA', 1, 'International'),
('DXB', 'Dubai', 'Dubai', 'UAE', 3, 'International'),
('JFK', 'John F. Kennedy', 'NYC', 'USA', 8, 'International'),
('LAX', 'Los Angeles', 'LA', 'USA', 9, 'International'),
('LGA', 'Laguardia', 'NYC', 'USA', 2, 'Domestic'),
('PVG', 'Shanghai Pudong', 'Shanghai', 'China', 3, 'International'),
('RDU', 'Raleigh-Durham', 'Raleigh', 'USA', 2, 'International');

-- --------------------------------------------------------

--
-- Table structure for table `Customer`
--

CREATE TABLE `Customer` (
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

--
-- Dumping data for table `Customer`
--

INSERT INTO `Customer` (`email`, `first_name`, `last_name`, `password`, `passport_num`, `passport_expiration`, `passport_country`, `date_of_birth`, `building_num`, `street`, `apt_num`, `city`, `state`, `zip`) VALUES
('danpoker@gmail.com', 'Dan', 'Zhang', '123abc', 99999999, '2025-05-01', 'USA', '2003-05-16', 55, 'Clark', 303, 'NYC', 'NY', 11201),
('faithvillar@gmail.com', 'Faith', 'Villareal', 'dance3m0j1', 10101011, '2026-05-12', 'USA', '2003-02-03', 6117, 'Chatford', 200, 'Raleigh', 'NC', 27612),
('grace@gmail.com', 'Grace', 'Able', '54321', 12312312, '2025-07-01', 'USA', '2004-05-13', 101, 'Johnson', 1502, 'NYC', 'NY', 11201),
('idanl@gmail.com', 'Idan', 'Lau', 'smurf10', 56567654, '2026-06-27', 'USA', '2004-04-03', 121, 'Deerwood', 919, 'Raleigh', 'NC', 27610),
('jeff@gmail.com', 'Jeff', 'Lin', '12345', 12345678, '2026-01-01', 'USA', '2004-03-16', 80, 'Lafayette', 703, 'NYC', 'NY', 10013),
('nikhil@gmail.com', 'Nikhil', 'Reddy', 'password', 11111111, '2027-01-02', 'USA', '2004-07-28', 101, 'Johnson', 1604, 'NYC', 'NY', 11201),
('rdey@nyu.edu', 'Ratan', 'Dey', 'databses!', 12312314, '2026-07-03', 'USA', '1995-01-01', 2, 'Metrotech', 900, 'NYC', 'NY', 11201);

-- --------------------------------------------------------

--
-- Table structure for table `customerphonenumbers`
--

CREATE TABLE `customerphonenumbers` (
  `customer_email` varchar(225) NOT NULL,
  `phone_number` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customerphonenumbers`
--

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES
('danpoker@gmail.com', '1342543142'),
('faithvillar@gmail.com', '9879879870'),
('grace@gmail.com', '9198881049'),
('idanl@gmail.com', '6785847563'),
('jeff@gmail.com', '9876956804'),
('nikhil@gmail.com', '2132453655'),
('rdey@nyu.edu', '9847568476');

-- --------------------------------------------------------

--
-- Table structure for table `Flight`
--

CREATE TABLE `Flight` (
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

--
-- Dumping data for table `Flight`
--

INSERT INTO `Flight` (`num`, `dep_date`, `dep_time`, `arr_time`, `arr_date`, `base_price`, `airplane_id`, `airline_name`, `dep_airport`, `arr_airport`, `status`) VALUES
(1234, '2023-11-28', '01:31:00', '03:28:00', '2023-11-28', 200, 434343, 'Air Canada', 'JFK', 'PVG', 'canceled'),
(2987, '2023-11-21', '10:02:00', '11:50:00', '2023-11-21', 100, 22982, 'Emirates', 'JFK', 'PVG', 'delayed'),
(4842, '2023-11-26', '12:00:00', '01:54:00', '2023-11-26', 100, 434343, 'Air Canada', 'PVG', 'JFK', 'on time'),
(4843, '2023-12-04', '12:00:00', '01:54:00', '2023-12-04', 100, 156253, 'Emirates', 'RDU', 'ATL', 'on time'),
(5676, '2023-12-12', '12:00:00', '01:54:00', '2023-12-12', 100, 22982, 'JetBlue', 'JFK', 'DEN', 'on time');

-- --------------------------------------------------------

--
-- Table structure for table `Maintenance`
--

CREATE TABLE `Maintenance` (
  `start_date` date NOT NULL,
  `start_time` time NOT NULL,
  `end_date` date NOT NULL,
  `end_time` time NOT NULL,
  `airplane_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Maintenance`
--

INSERT INTO `Maintenance` (`start_date`, `start_time`, `end_date`, `end_time`, `airplane_id`) VALUES
('2024-12-08', '12:00:00', '2025-06-01', '01:30:00', 22982);

-- --------------------------------------------------------

--
-- Table structure for table `PurchaseHistory`
--

CREATE TABLE `PurchaseHistory` (
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

--
-- Dumping data for table `PurchaseHistory`
--

INSERT INTO `PurchaseHistory` (`customer_email`, `purchase_time`, `card_num`, `exp_date`, `purchase_date`, `first_name`, `last_name`, `name_on_card`, `date_of_birth`, `card_type`, `ticket_id`) VALUES
('grace@gmail.com', '02:03:40', 2345234523452345, '2026-12-30', '2023-11-07', 'Grace', 'Able', 'Grace Ableidinger', '2004-05-13', 'Debit', 246),
('jeff@gmail.com', '01:00:00', 1234123412341234, '2026-11-06', '2023-11-07', 'Jeff', 'Lin', 'Jeffrey Lin', '2004-03-16', 'Credit', 123)
('danpoker@gmail.com', '03:05:34', 9867887687688678, '2026-12-06', '2023-11-07', 'Dan', 'Zhang', 'Dan Zhang', '2003-05-16', 'Credit', 589);

-- --------------------------------------------------------

--
-- Table structure for table `Reviews`
--

CREATE TABLE `Reviews` (
  `customer_email` varchar(225) NOT NULL,
  `flight_num` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `comment` mediumtext NOT NULL,
  `dep_date` date NOT NULL,
  `dep_time` time NOT NULL,
  `airline_name` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Reviews`
--

INSERT INTO `Reviews` (`customer_email`, `flight_num`, `rating`, `comment`, `dep_date`, `dep_time`, `airline_name`) VALUES
('danpoker@gmail.com', 1234, 0, 'Awful flight. No one wanted to listen to me talk about my startups.', '2023-11-28', '01:31:00', 'Air Canada'),
('jeff@gmail.com', 5676, 8, 'Could have served more snacks but overall nice flight.', '2023-12-12', '12:00:00', 'JetBlue'),
('nikhil@gmail.com', 2987, 10, 'Wonderful flight! I met so many lovely ladies on the plane and the service was impeccable. ', '2023-11-21', '10:02:00', 'Emirates');

-- --------------------------------------------------------

--
-- Table structure for table `Ticket`
--

CREATE TABLE `Ticket` (
  `id` int(11) NOT NULL,
  `price` float NOT NULL,
  `flight_num` int(11) NOT NULL,
  `flight_dep_date` date NOT NULL,
  `flight_dep_time` time NOT NULL,
  `airline_name` varchar(225) NOT NULL,
  `customer_email` varchar(225)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Ticket`
--

INSERT INTO `Ticket` (`id`, `price`, `flight_num`, `flight_dep_date`, `flight_dep_time`, `airline_name`, `customer_email`) VALUES
(123, 100, 1234, '2023-11-28', '01:31:00', 'Air Canada', 'jeff@gmail.com'),
(246, 100, 4842, '2023-11-26', '12:00:00', 'Emirates', 'grace@gmail.com')
(589, 100, 5676, '2023-12-12', '12:00:00', 'JetBlue', 'danpoker@gmail.com')

INSERT INTO `Ticket` (`id`, `price`, `flight_num`, `flight_dep_date`, `flight_dep_time`, `airline_name`) VALUES
(577, 100, 5676, '2023-12-12', '12:00:00', 'JetBlue')
(573, 100, 5676, '2023-12-12', '12:00:00', 'JetBlue')
(574, 100, 5676, '2023-12-12', '12:00:00', 'JetBlue');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Airline`
--
ALTER TABLE `Airline`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `AirlineStaff`
--
ALTER TABLE `AirlineStaff`
  ADD PRIMARY KEY (`username`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `AirlineStaffEmails`
--
ALTER TABLE `AirlineStaffEmails`
  ADD PRIMARY KEY (`staff_username`,`email`);

--
-- Indexes for table `airlinestaffphonenumbers`
--
ALTER TABLE `airlinestaffphonenumbers`
  ADD PRIMARY KEY (`staff_username`,`phone_number`);

--
-- Indexes for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD PRIMARY KEY (`id`,`airline_name`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `Airport`
--
ALTER TABLE `Airport`
  ADD PRIMARY KEY (`code`);

--
-- Indexes for table `Customer`
--
ALTER TABLE `Customer`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `customerphonenumbers`
--
ALTER TABLE `customerphonenumbers`
  ADD PRIMARY KEY (`customer_email`,`phone_number`);

--
-- Indexes for table `Flight`
--
ALTER TABLE `Flight`
  ADD PRIMARY KEY (`num`,`dep_date`,`dep_time`,`airline_name`),
  ADD KEY `airplane_id` (`airplane_id`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `dep_airport` (`dep_airport`),
  ADD KEY `arr_airport` (`arr_airport`);

--
-- Indexes for table `Maintenance`
--
ALTER TABLE `Maintenance`
  ADD PRIMARY KEY (`start_date`,`start_time`,`end_date`,`end_time`,`airplane_id`),
  ADD KEY `airplane_id` (`airplane_id`);

--
-- Indexes for table `PurchaseHistory`
--
ALTER TABLE `PurchaseHistory`
  ADD PRIMARY KEY (`customer_email`,`ticket_id`),
  ADD KEY `ticket_id` (`ticket_id`);

--
-- Indexes for table `Reviews`
--
ALTER TABLE `Reviews`
  ADD PRIMARY KEY (`customer_email`,`flight_num`,`dep_date`,`dep_time`,`airline_name`),
  ADD KEY `flight_num` (`flight_num`,`dep_date`,`dep_time`),
  ADD KEY `airline_name` (`airline_name`);

--
-- Indexes for table `Ticket`
--
ALTER TABLE `Ticket`
  ADD PRIMARY KEY (`id`),
  ADD KEY `flight_num` (`flight_num`,`flight_dep_date`,`flight_dep_time`),
  ADD KEY `airline_name` (`airline_name`),
  ADD KEY `customer_email` (`customer_email`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `AirlineStaff`
--
ALTER TABLE `AirlineStaff`
  ADD CONSTRAINT `airlinestaff_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`);

--
-- Constraints for table `AirlineStaffEmails`
--
ALTER TABLE `AirlineStaffEmails`
  ADD CONSTRAINT `airlinestaffemails_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `AirlineStaff` (`username`);

--
-- Constraints for table `airlinestaffphonenumbers`
--
ALTER TABLE `airlinestaffphonenumbers`
  ADD CONSTRAINT `airlinestaffphonenumbers_ibfk_1` FOREIGN KEY (`staff_username`) REFERENCES `AirlineStaff` (`username`);

--
-- Constraints for table `Airplane`
--
ALTER TABLE `Airplane`
  ADD CONSTRAINT `airplane_ibfk_1` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`);

--
-- Constraints for table `customerphonenumbers`
--
ALTER TABLE `customerphonenumbers`
  ADD CONSTRAINT `customerphonenumbers_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `Customer` (`email`);

--
-- Constraints for table `Flight`
--
ALTER TABLE `Flight`
  ADD CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`airplane_id`) REFERENCES `Airplane` (`id`),
  ADD CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`),
  ADD CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`dep_airport`) REFERENCES `Airport` (`code`),
  ADD CONSTRAINT `flight_ibfk_4` FOREIGN KEY (`arr_airport`) REFERENCES `Airport` (`code`);

--
-- Constraints for table `Maintenance`
--
ALTER TABLE `Maintenance`
  ADD CONSTRAINT `maintenance_ibfk_1` FOREIGN KEY (`airplane_id`) REFERENCES `Airplane` (`id`);

--
-- Constraints for table `PurchaseHistory`
--
ALTER TABLE `PurchaseHistory`
  ADD CONSTRAINT `purchasehistory_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `Customer` (`email`),
  ADD CONSTRAINT `purchasehistory_ibfk_2` FOREIGN KEY (`ticket_id`) REFERENCES `Ticket` (`id`);

--
-- Constraints for table `Reviews`
--
ALTER TABLE `Reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`customer_email`) REFERENCES `Customer` (`email`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`flight_num`,`dep_date`,`dep_time`) REFERENCES `Flight` (`num`, `dep_date`, `dep_time`),
  ADD CONSTRAINT `reviews_ibfk_3` FOREIGN KEY (`airline_name`) REFERENCES `Flight` (`airline_name`);

--
-- Constraints for table `Ticket`
--
ALTER TABLE `Ticket`
  ADD CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`flight_num`,`flight_dep_date`,`flight_dep_time`) REFERENCES `Flight` (`num`, `dep_date`, `dep_time`),
  ADD CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`airline_name`) REFERENCES `Airline` (`name`),
  ADD CONSTRAINT `ticket_ibfk_3` FOREIGN KEY (`customer_email`) REFERENCES `Customer` (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
