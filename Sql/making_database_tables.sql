CREATE DATABASE Horizion_travles_database;
USE Horizion_travles_database;
CREATE TABLE user_info (
	user_id int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    email varchar(255) NOT NULL,
    hashed_password char(60) NOT NULL,
    PRIMARY KEY (user_id)
    );

CREATE TABLE flight_info (
	flight_id int NOT NULL,
    departure_location varchar(255) NOT NULL,
    departure_time time,
    destination_location varchar(255) NOT NULL,
    arival_time time,
	PRIMARY KEY (flight_id)
);

CREATE TABLE flight_orders (
	order_id int NOT NULL,
	user_id int NOT NULL,
    flight_id int NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (user_id) REFERENCES user_info(user_id),
    FOREIGN KEY (flight_id) REFERENCES flight_info(flight_id)
)