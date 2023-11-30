INSERT INTO Airline (name) VALUES ("JetBlue");

INSERT INTO Airline (name) VALUES ("Delta");

INSERT INTO Airline (name) VALUES ("American");

INSERT INTO Airline (name) VALUES ("Southwest");

INSERT INTO Airline (name) VALUES ("Air Canada");

INSERT INTO Airline (name) VALUES ("Emirates");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("RDU", "Raleigh-Durham", "Raleigh", "USA", 2, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("LGA", "Laguardia", "NYC", "USA", 2, "Domestic");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("DEN", "Denver", "Denver", "USA", 1, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("ATL", "Hartsfield-Jackson", "Atlanta", "USA", 2, "Domestic");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("LAX", "Los Angeles", "LA", "USA", 9, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("DXB", "Dubai", "Dubai", "UAE", 3, "International");

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) VALUES ("danpoker@gmail.com", "Dan", "Zhang", "123abc", "99999999", "2025-05-01", "USA", "2003-05-16", 55, "Clark", 303, "NYC", "NY", 11201);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) VALUES ("faithvillar@gmail.com", "Faith", "Villareal", "dance3m0j1", "10101011", "2026-05-12", "USA", "2003-02-03", 6117, "Chatford", 200, "Raleigh", "NC", 27612);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) VALUES ("idanl@gmail.com", "Idan", "Lau", "smurf10", "56567654", "2026-06-27", "USA", "2004-04-03", 121, "Deerwood", 919, "Raleigh", "NC", 27610);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) VALUES ("rdey@nyu.edu", "Ratan", "Dey", "databses!", "12312314", "2026-07-03", "USA", "1995-01-01", 2, "Metrotech", 900, "NYC", "NY", 11201);

INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (758746, 410, "Boeing", 747, "2004-01-23", 19, "Air Canada");

INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (156253, 200, "Boeing", 646, "2004-01-22", 19, "Emirates");

INSERT INTO airlinestaffemails (staff_username, email) VALUES ("iloveplanes123", "sigma@gmail.com");

ALTER TABLE `customerphonenumbers` CHANGE `phone_number` `phone_number` VARCHAR(11) NOT NULL;

ALTER TABLE `airlinestaffphonenumbers` CHANGE `phone_number` `phone_number` VARCHAR(11) NOT NULL;

INSERT INTO airlinestaffphonenumbers (staff_username, phone_number) VALUES ("iloveplanes123", "9191111918");

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('danpoker@gmail.com', '1342543142');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('faithvillar@gmail.com', '9879879870');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('grace@gmail.com', '9198881049');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('idanl@gmail.com', '6785847563');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('jeff@gmail.com', '9876956804');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('nikhil@gmail.com', '2132453655');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('rdey@nyu.edu', '9847568476');

INSERT INTO `flight` (`num`, `dep_date`, `dep_time`, `arr_time`, `arr_date`, `base_price`, `airplane_id`, `airline_name`, `dep_airport`, `arr_airport`, `status`) VALUES ('4843', '2023-12-04', '12:00:00', '01:54:00', '2023-12-04', '100', '156253', 'Emirates', 'RDU', 'ATL', 'on time');

INSERT INTO `flight` (`num`, `dep_date`, `dep_time`, `arr_time`, `arr_date`, `base_price`, `airplane_id`, `airline_name`, `dep_airport`, `arr_airport`, `status`) VALUES ('5676', '2023-12-12', '12:00:00', '01:54:00', '2023-12-12', '100', '22982', 'JetBlue', 'JFK', 'DEN', 'on time');

INSERT INTO maintenance (start_date, start_time, end_date, end_time, airplane_id) VALUES ("2024-12-08", "12:00:00", "2025-06-01", "01:30:00", 22982);

INSERT INTO `reviews` (`customer_email`, `flight_num`, `rating`, `comment`, `dep_date`, `dep_time`, `airline_name`) VALUES ('danpoker@gmail.com', '1234', '0', 'Awful flight. No one wanted to listen to me talk about my startups.', '2023-11-28', '01:31:00', 'Air Canada'), ('nikhil@gmail.com', '2987', '10', 'Wonderful flight! I met so many lovely ladies on the plane and the service was impeccable. ', '2023-11-21', '10:02:00', 'Emirates'), ('jeff@gmail.com', '5676', '8', 'Could have served more snacks but overall nice flight.', '2023-12-12', '12:00:00', 'JetBlue');

INSERT INTO `purchasehistory` (`customer_email`, `purchase_time`, `card_num`, `exp_date`, `purchase_date`, `first_name`, `last_name`, `name_on_card`, `date_of_birth`, `card_type`, `ticket_id`) VALUES ('danpoker@gmail.com', '12:43:28', '8817176276152987', '2030-11-02', '2023-11-01', 'Daniel', 'Zhang', 'Dan Zhang', '2002-11-16', 'Debit', '123'), ('nikhil@gmail.com', '00:43:28', '7657657657659487', '2032-11-18', '2023-11-16', 'Nikhil', 'Reddy', 'Nikhil Reddy', '2004-11-03', 'Credit', '123');