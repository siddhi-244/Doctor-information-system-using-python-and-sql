-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 24, 2021 at 02:22 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `doctors`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `ID` varchar(10) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Specialisation` varchar(20) NOT NULL,
  `Email` varchar(40) NOT NULL,
  `hospital` varchar(40) NOT NULL,
  `country` varchar(20) NOT NULL,
  `experience` varchar(5) NOT NULL,
  `birth` varchar(10) NOT NULL,
  `city` varchar(20) NOT NULL,
  `Degree` varchar(20) NOT NULL,
  `shift` varchar(20) NOT NULL,
  `gender` varchar(15) NOT NULL,
  `patients_treated` varchar(10) NOT NULL,
  `website` varchar(30) NOT NULL,
  `salary` varchar(10) NOT NULL,
  `age` varchar(5) NOT NULL,
  `available` varchar(2) NOT NULL,
  `number` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`ID`, `Name`, `Specialisation`, `Email`, `hospital`, `country`, `experience`, `birth`, `city`, `Degree`, `shift`, `gender`, `patients_treated`, `website`, `salary`, `age`, `available`, `number`) VALUES
('1', 'dr shah', 'dentist', 'shah21@gmail.com', 'city hospital', 'India', '3', '3/14/90', 'Delhi', 'BDS', 'Morning', 'Male', '12', 'www.jhos.co.in', '340000', '27', '5', '9088828282'),
('2', 'shilpa singh', 'gynecologist', 'shah21@gmail.com', 'city hospital', 'India', '7', '3/1/90', 'Aurangabad', 'PHD', 'Evening', 'Female', '12', 'www.cityhos.com', '340033', '31', '5', '9088828222'),
('3', 'Diya Sharma', 'pediatrician', 'diya32@gmail.com', 'krishna hospital', 'India', '4', '10/23/1993', 'Hyderabad', 'MBBS', 'Evening', 'Female', '12', 'www.krushnahospital.co.in', '67000', '27', '5', '9190909090'),
('4', 'Diya Bhanushali', 'dermatologist', 'diya32@gmail.com', 'ved hospital', 'India', '4', '10/04/1990', 'Hyderabad', 'PHD', 'Evening', 'Female', '50', 'www.vedhospital.co.in', '67000', '31', '7', '9190909099'),
('5', 'Diya Batra', 'dermatologist', 'diya4444@gmail.com', 'ved hospital', 'India', '8', '10/04/1990', 'Hyderabad', 'PHD', 'Morning', 'Female', '40', 'www.vedhospital.co.in', '67008', '33', '6', '8888888888');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
