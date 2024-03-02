-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Oct 08, 2023 at 11:25 AM
-- Server version: 5.7.39
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lofartapp_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(11) NOT NULL,
  `admin_username` varchar(20) DEFAULT NULL,
  `admin_pwd` varchar(200) DEFAULT NULL,
  `admin_email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_username`, `admin_pwd`, `admin_email`) VALUES
(1, 'admin123', 'pbkdf2:sha256:600000$Wbq58ufF8dKQ8Spb$af62e17e015a7b40a1c303362cd390226fdf3ec97f6b0ad1042495a0dc748a5a', 'admin@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `adminreg`
--

CREATE TABLE `adminreg` (
  `admin_id` int(11) NOT NULL,
  `admin_username` varchar(10) NOT NULL,
  `admin_pwd` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `adminreg`
--

INSERT INTO `adminreg` (`admin_id`, `admin_username`, `admin_pwd`) VALUES
(1, 'admin123', 'pbkdf2:sha256:600000$p9VugZ2OPEHnc1ii$0278d50ba9b4e5eb3389809e932f1a2b2af615d3b94314397b9f86056412192a');

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('bf1e54f26db5');

-- --------------------------------------------------------

--
-- Table structure for table `lga`
--

CREATE TABLE `lga` (
  `lga_id` int(11) NOT NULL,
  `lga_name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL,
  `order_amt` int(11) NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `order_user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `orderdetails`
--

CREATE TABLE `orderdetails` (
  `details_id` int(11) NOT NULL,
  `details_qty` int(11) NOT NULL,
  `details_amt` int(11) NOT NULL,
  `details_order_id` int(11) DEFAULT NULL,
  `details_upload_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `payment_status` varchar(10) NOT NULL,
  `payment_amt` int(11) NOT NULL,
  `payment_date` datetime DEFAULT NULL,
  `payment_user_id` int(11) DEFAULT NULL,
  `payment_order_id` int(11) DEFAULT NULL,
  `refno` varchar(12) NOT NULL,
  `ptupload` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `payment_status`, `payment_amt`, `payment_date`, `payment_user_id`, `payment_order_id`, `refno`, `ptupload`) VALUES
(47, 'pending', 9900000, '2023-10-08 11:23:59', 15, NULL, 'LF6428709351', 13);

-- --------------------------------------------------------

--
-- Table structure for table `state`
--

CREATE TABLE `state` (
  `state_id` int(11) NOT NULL,
  `state_name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `state`
--

INSERT INTO `state` (`state_id`, `state_name`) VALUES
(1, 'lagos\r\n');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `user_fname` varchar(64) NOT NULL,
  `user_lname` varchar(64) NOT NULL,
  `user_add` varchar(200) NOT NULL,
  `user_city` varchar(64) NOT NULL,
  `user_reg` datetime DEFAULT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_profile` varchar(300) DEFAULT NULL,
  `user_pix` varchar(120) DEFAULT NULL,
  `user_username` varchar(100) NOT NULL,
  `user_password` varchar(225) NOT NULL,
  `user_usertype` varchar(100) NOT NULL,
  `user_state_id` int(11) DEFAULT NULL,
  `user_lga_id` int(11) DEFAULT NULL,
  `user_state` varchar(10) NOT NULL,
  `user_lga` varchar(50) NOT NULL,
  `user_phone` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_fname`, `user_lname`, `user_add`, `user_city`, `user_reg`, `user_email`, `user_profile`, `user_pix`, `user_username`, `user_password`, `user_usertype`, `user_state_id`, `user_lga_id`, `user_state`, `user_lga`, `user_phone`) VALUES
(15, 'Precious', 'Awe', '24 ,james street , off powerline ,Lagos', 'lagos', '2023-10-06 10:08:00', 'chukuwamazon@gmail.com', 'None', 'mdo.jpg', 'chukuwamazon@gmail.com', 'pbkdf2:sha256:600000$i6C1wcPjLdJT95R7$79f1fd2fda05b75f7ef28335a8ff08488cd1938fd3254222f131579850c2cf83', 'Fashion_Designer', NULL, NULL, '', '', ''),
(16, 'mazi', 'buko', '24 ,james street , off powerline ,Lagos', 'lagos', '2023-10-06 10:40:49', 'librallaw@yahoo.com', 'this is all about me and what i want', 'mdo.jpg', 'librallaw@yahoo.com', 'pbkdf2:sha256:600000$1yvjYGoXnV7UDRwZ$0d27ac3e64923670d6bc765b5ed6966719e309ca56979a26f7415453b8682dde', 'Fashion_Designer', NULL, NULL, '', '', ''),
(17, 'leve', 'ovie', '24 ,james street , off powerline ,Lagos', 'lagos', '2023-10-06 14:34:33', 'mazibuko@gmail.com', 'None', 'b3.png', 'mazibuko@gmail.com', 'pbkdf2:sha256:600000$UvS3v2oDEk4XDYcD$94fdd68582c91b2e864dd58434d9135b410fe6b9ebb3b71a0e593405dd68ee6d', 'Fashion_Designer', NULL, NULL, 'lagos', 'ojodu', '09022837445');

-- --------------------------------------------------------

--
-- Table structure for table `usercomment`
--

CREATE TABLE `usercomment` (
  `usercomment_id` int(11) NOT NULL,
  `user_comment` varchar(300) DEFAULT NULL,
  `comment_date` datetime DEFAULT NULL,
  `comment_user_id` int(11) DEFAULT NULL,
  `comment_upload_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `usercomment`
--

INSERT INTO `usercomment` (`usercomment_id`, `user_comment`, `comment_date`, `comment_user_id`, `comment_upload_id`) VALUES
(15, 'this is one of the most beautifl thing i have seen ', '2023-10-06 13:23:36', 16, 12),
(16, 'i lopve this website and i this is one of the best artwork ', '2023-10-06 20:47:45', 17, 12),
(17, 'this is best art work. have ever had to come across', '2023-10-08 11:23:36', 15, 13);

-- --------------------------------------------------------

--
-- Table structure for table `userupload`
--

CREATE TABLE `userupload` (
  `upload_id` int(11) NOT NULL,
  `upload_filename` varchar(200) NOT NULL,
  `upload_amt` int(11) NOT NULL,
  `upload_date` datetime DEFAULT NULL,
  `upload_user_id` int(11) DEFAULT NULL,
  `upload_desc` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `userupload`
--

INSERT INTO `userupload` (`upload_id`, `upload_filename`, `upload_amt`, `upload_date`, `upload_user_id`, `upload_desc`) VALUES
(12, '6090653b4.jpg', 90000, '2023-10-06 10:11:41', 15, 'the name of my school and the name of my other school is something most people would not understand the name of my school and the name of my other school is something most people would not understand '),
(13, '3959629b2.jpg', 99000, '2023-10-06 10:47:16', 16, 'there is more to life than we see it this is why we all havee to be good there is more to life than we see it this is why we all havee to be good there is more to life than we see it this is why we all havee to be good ');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `adminreg`
--
ALTER TABLE `adminreg`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `lga`
--
ALTER TABLE `lga`
  ADD PRIMARY KEY (`lga_id`),
  ADD KEY `ix_lga_lga_name` (`lga_name`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `order_user_id` (`order_user_id`);

--
-- Indexes for table `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD PRIMARY KEY (`details_id`),
  ADD KEY `details_order_id` (`details_order_id`),
  ADD KEY `details_upload_id` (`details_upload_id`),
  ADD KEY `ix_orderdetails_details_amt` (`details_amt`),
  ADD KEY `ix_orderdetails_details_qty` (`details_qty`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`),
  ADD KEY `payment_user_id` (`payment_user_id`),
  ADD KEY `payment_order_id` (`payment_order_id`),
  ADD KEY `ix_payment_payment_amt` (`payment_amt`),
  ADD KEY `ix_payment_payment_status` (`payment_status`),
  ADD KEY `ix_payment_refno` (`refno`),
  ADD KEY `ptupload` (`ptupload`);

--
-- Indexes for table `state`
--
ALTER TABLE `state`
  ADD PRIMARY KEY (`state_id`),
  ADD KEY `ix_state_state_name` (`state_name`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_state_id` (`user_state_id`),
  ADD KEY `user_lga_id` (`user_lga_id`),
  ADD KEY `ix_user_user_lname` (`user_lname`),
  ADD KEY `ix_user_user_add` (`user_add`),
  ADD KEY `ix_user_user_city` (`user_city`),
  ADD KEY `ix_user_user_profile` (`user_profile`),
  ADD KEY `ix_user_user_username` (`user_username`),
  ADD KEY `ix_user_user_usertype` (`user_usertype`),
  ADD KEY `ix_user_user_password` (`user_password`),
  ADD KEY `ix_user_user_email` (`user_email`),
  ADD KEY `ix_user_user_fname` (`user_fname`);

--
-- Indexes for table `usercomment`
--
ALTER TABLE `usercomment`
  ADD PRIMARY KEY (`usercomment_id`),
  ADD KEY `comment_user_id` (`comment_user_id`),
  ADD KEY `comment_upload_id` (`comment_upload_id`),
  ADD KEY `ix_usercomment_user_comment` (`user_comment`);

--
-- Indexes for table `userupload`
--
ALTER TABLE `userupload`
  ADD PRIMARY KEY (`upload_id`),
  ADD KEY `upload_user_id` (`upload_user_id`),
  ADD KEY `ix_userupload_upload_amt` (`upload_amt`),
  ADD KEY `ix_userupload_upload_filename` (`upload_filename`),
  ADD KEY `ix_userupload_upload_desc` (`upload_desc`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `adminreg`
--
ALTER TABLE `adminreg`
  MODIFY `admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `lga`
--
ALTER TABLE `lga`
  MODIFY `lga_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `orderdetails`
--
ALTER TABLE `orderdetails`
  MODIFY `details_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `state`
--
ALTER TABLE `state`
  MODIFY `state_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `usercomment`
--
ALTER TABLE `usercomment`
  MODIFY `usercomment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `userupload`
--
ALTER TABLE `userupload`
  MODIFY `upload_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`order_user_id`) REFERENCES `user` (`user_id`);

--
-- Constraints for table `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD CONSTRAINT `orderdetails_ibfk_1` FOREIGN KEY (`details_order_id`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `orderdetails_ibfk_2` FOREIGN KEY (`details_upload_id`) REFERENCES `userupload` (`upload_id`);

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`payment_user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `payment_ibfk_2` FOREIGN KEY (`payment_order_id`) REFERENCES `order` (`order_id`),
  ADD CONSTRAINT `payment_ibfk_3` FOREIGN KEY (`ptupload`) REFERENCES `userupload` (`upload_id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`user_state_id`) REFERENCES `state` (`state_id`),
  ADD CONSTRAINT `user_ibfk_2` FOREIGN KEY (`user_lga_id`) REFERENCES `lga` (`lga_id`);

--
-- Constraints for table `usercomment`
--
ALTER TABLE `usercomment`
  ADD CONSTRAINT `usercomment_ibfk_1` FOREIGN KEY (`comment_user_id`) REFERENCES `user` (`user_id`),
  ADD CONSTRAINT `usercomment_ibfk_2` FOREIGN KEY (`comment_upload_id`) REFERENCES `userupload` (`upload_id`);

--
-- Constraints for table `userupload`
--
ALTER TABLE `userupload`
  ADD CONSTRAINT `userupload_ibfk_1` FOREIGN KEY (`upload_user_id`) REFERENCES `user` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
