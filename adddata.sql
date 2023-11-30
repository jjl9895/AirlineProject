--Airlines
INSERT INTO Airline (name) VALUES ("JetBlue");

INSERT INTO Airline (name) VALUES ("Delta");

INSERT INTO Airline (name) VALUES ("American");

INSERT INTO Airline (name) VALUES ("Southwest");

INSERT INTO Airline (name) VALUES ("Air Canada");

INSERT INTO Airline (name) VALUES ("Emirates");

--Airports
INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("RDU", "Raleigh-Durham", "Raleigh", "USA", 2, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("LGA", "Laguardia", "NYC", "USA", 2, "Domestic");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("DEN", "Denver", "Denver", "USA", 1, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("ATL", "Hartsfield-Jackson", "Atlanta", "USA", 2, "Domestic");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("LAX", "Los Angeles", "LA", "USA", 9, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("DXB", "Dubai", "Dubai", "UAE", 3, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("JFK", "John F. Kennedy", "NYC", "USA", 8, "International");

INSERT INTO Airport (code, name, city, country, num_of_terminals, type) VALUES ("PVG", "Shanghai Pudong", "Shanghai", "China", 3, "International");

--Customers
INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) 
VALUES ("danpoker@gmail.com", "Dan", "Zhang", "123abc", "99999999", "2025-05-01", "USA", "2003-05-16", 55, "Clark", 303, "NYC", "NY", 11201);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) 
VALUES ("faithvillar@gmail.com", "Faith", "Villareal", "dance3m0j1", "10101011", "2026-05-12", "USA", "2003-02-03", 6117, "Chatford", 200, "Raleigh", "NC", 27612);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) 
VALUES ("idanl@gmail.com", "Idan", "Lau", "smurf10", "56567654", "2026-06-27", "USA", "2004-04-03", 121, "Deerwood", 919, "Raleigh", "NC", 27610);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) 
VALUES ("rdey@nyu.edu", "Ratan", "Dey", "databses!", "12312314", "2026-07-03", "USA", "1995-01-01", 2, "Metrotech", 900, "NYC", "NY", 11201);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip)
VALUES ("grace@gmail.com", "Grace", "Able", "54321", "12312312", "2025-07-01", "USA", "2004-05-13", 101, "Johnson", 1502, "NYC", "NY", 11201);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip) 
VALUES ("jeff@gmail.com", "Jeff", "Lin", "12345", "12345678", "2026-01-01", "USA", "2004-03-16", 80, "Lafayette", 703, "NYC", "NY", 10013);

INSERT INTO customer (email, first_name, last_name, password, passport_num, passport_expiration, passport_country, date_of_birth, building_num, street, apt_num, city, state, zip)
VALUES ("nikhil@gmail.com", "Nikhil", "Reddy", "password", "11111111", "2027-01-02", "USA", "2004-07-28",101, "Johnson", 1604, "NYC", "NY", 11201);


--Airplanes
INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (758746, 410, "Boeing", 747, "2004-01-23", 19, "Air Canada");

INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (156253, 200, "Boeing", 646, "2004-01-22", 19, "Emirates");

INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (900111, 410, "Boeing", 747, "2022-01-23", 1, "JetBlue");

INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (434343, 240, "Boeing", 878, "2004-04-23", 19, "Air Canada");

INSERT INTO Airplane (id, num_of_seats, manufacturer, model_num, manufacture_date, age, airline_name)
VALUES (22982, 853, "AirBus", 380, "2001-08-07", 22, "Emirates");


--AirlineStaff
INSERT INTO AirlineStaff (username, password, first_name, last_name, date_of_birth, airline_name)
VALUES ("iloveplanes123", "12345678910", "Ishaan", "Poojari", "2004-04-08", "JetBlue");

INSERT INTO airlinestaffemails (staff_username, email) VALUES ("iloveplanes123", "sigma@gmail.com");

INSERT INTO airlinestaffphonenumbers (staff_username, phone_number) VALUES ("iloveplanes123", "9191111918");



ALTER TABLE `customerphonenumbers` CHANGE `phone_number` `phone_number` VARCHAR(11) NOT NULL;

ALTER TABLE `airlinestaffphonenumbers` CHANGE `phone_number` `phone_number` VARCHAR(11) NOT NULL;


--CustomerPhoneNumbers
INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('danpoker@gmail.com', '1342543142');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('faithvillar@gmail.com', '9879879870');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('grace@gmail.com', '9198881049');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('idanl@gmail.com', '6785847563');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('jeff@gmail.com', '9876956804');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('nikhil@gmail.com', '2132453655');

INSERT INTO `customerphonenumbers` (`customer_email`, `phone_number`) VALUES ('rdey@nyu.edu', '9847568476');

--Flights
INSERT INTO Flight (`num`, `dep_date`, `dep_time`, `arr_time`, `arr_date`, `base_price`, `airplane_id`, `airline_name`, `dep_airport`, `arr_airport`, `status`) 
VALUES (4843, '2023-12-04', '12:00:00', '01:54:00', '2023-12-04', '100', '156253', 'Emirates', 'RDU', 'ATL', 'on time');

INSERT INTO Flight (`num`, `dep_date`, `dep_time`, `arr_time`, `arr_date`, `base_price`, `airplane_id`, `airline_name`, `dep_airport`, `arr_airport`, `status`) 
VALUES (5676, '2023-12-12', '12:00:00', '01:54:00', '2023-12-12', '100', '22982', 'JetBlue', 'JFK', 'DEN', 'on time');

INSERT INTO Flight (num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, airline_name, dep_airport, arr_airport, status)
VALUES (2987, "2023-11-21", "10:02:00", "11:50:00", "2023-11-21", 100.00, 22982, "Emirates", "JFK", "PVG", "delayed");

INSERT INTO Flight (num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, airline_name, dep_airport, arr_airport, status)
VALUES (4842, "2023-11-26", "12:00:00", "01:54:00", "2023-11-26", 100.00, 434343, "Air Canada", "PVG", "JFK", "on time");

INSERT INTO Flight (num, dep_date, dep_time, arr_time, arr_date, base_price, airplane_id, airline_name, dep_airport, arr_airport, status)
VALUES (1234, "2023-11-28", "01:31:00", "03:28:00", "2023-11-28", 200.00, 434343, "Air Canada", "JFK", "PVG", "canceled");

INSERT INTO maintenance (start_date, start_time, end_date, end_time, airplane_id) VALUES ("2024-12-08", "12:00:00", "2025-06-01", "01:30:00", 22982);

INSERT INTO `reviews` (`customer_email`, `flight_num`, `rating`, `comment`, `dep_date`, `dep_time`, `airline_name`) 
VALUES ('danpoker@gmail.com', '1234', '0', 'Awful flight. No one wanted to listen to me talk about my startups.', '2023-11-28', '01:31:00', 'Air Canada'), 
('nikhil@gmail.com', '2987', '10', 'Wonderful flight! I met so many lovely ladies on the plane and the service was impeccable. ', '2023-11-21', '10:02:00', 'Emirates'), 
('jeff@gmail.com', '5676', '8', 'Could have served more snacks but overall nice flight.', '2023-12-12', '12:00:00', 'JetBlue');

--Tickets
INSERT INTO Ticket (id, price, flight_num, flight_dep_date, flight_dep_time, airline_name, customer_email)
VALUES (123, 100.00, 1234, "2023-11-28", "01:31:00", "Air Canada", "jeff@gmail.com");

INSERT INTO Ticket (id, price, flight_num, flight_dep_date, flight_dep_time, airline_name, customer_email)
VALUES (246, 100.00, 4842, "2023-11-26", "12:00:00", "Emirates", "grace@gmail.com");


--PurchaseHistory
INSERT INTO Purchasehistory (`customer_email`, `purchase_time`, `card_num`, `exp_date`, `purchase_date`, `first_name`, `last_name`, `name_on_card`, `date_of_birth`, `card_type`, `ticket_id`) 
VALUES ('danpoker@gmail.com', '12:43:28', '8817176276152987', '2030-11-02', '2023-11-01', 'Daniel', 'Zhang', 'Dan Zhang', '2002-11-16', 'Debit', '123'), ('nikhil@gmail.com', '00:43:28', '7657657657659487', '2032-11-18', '2023-11-16', 'Nikhil', 'Reddy', 'Nikhil Reddy', '2004-11-03', 'Credit', '123');

INSERT INTO PurchaseHistory (customer_email, purchase_time, card_num, exp_date, purchase_date, first_name, last_name, name_on_card, date_of_birth, card_type, ticket_id)
VALUES ("jeff@gmail.com", "01:00:00", 1234123412341234, "2026-11-06", "2023-11-07", "Jeff", "Lin", "Jeffrey Lin", "2004-03-16", "Credit", 123);

INSERT INTO PurchaseHistory (customer_email, purchase_time, card_num, exp_date, purchase_date, first_name, last_name, name_on_card, date_of_birth, card_type, ticket_id)
VALUES ("grace@gmail.com", "02:03:40", 2345234523452345, "2026-12-30", "2023-11-07", "Grace", "Able", "Grace Ableidinger", "2004-05-13", "Debit", 246);




