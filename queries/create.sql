CREATE TABLE bus_characteristics (
    model_id BIGINT NOT NULL,
    name VARCHAR(24) NOT NULL,
    size INTEGER NOT NULL,
    description MEDIUMTEXT NOT NULL,
    FULLTEXT key description(description),
    PRIMARY KEY (model_id)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
CREATE TABLE buses (
	licensePlate VARCHAR(8) NOT NULL,
	characteristics_model_id BIGINT NOT NULL,
	working BOOLEAN NOT NULL,
	PRIMARY KEY (licensePlate)
);
CREATE TABLE drivers (
	licenseID VARCHAR(24) NOT NULL,
	name_firstName VARCHAR(240) NOT NULL,
	name_lastName VARCHAR(240) NOT NULL,
	PRIMARY KEY (licenseID)
);
CREATE TABLE passengers (
	passengerID INT NOT NULL,
	name_firstName VARCHAR(240) NOT NULL,
	name_lastName VARCHAR(240) NOT NULL,
	PRIMARY KEY (passengerID)
);
CREATE TABLE onetimetickets (
	ticketID INT NOT NULL,
	issueDate TIMESTAMP NOT NULL,
	passengerID INT NOT NULL,
	PRIMARY KEY (ticketID),
	FOREIGN KEY(passengerID) REFERENCES passengers (passengerID)
);
CREATE TABLE routes (
	routeNo INT NOT NULL,
	PRIMARY KEY (routeNo)
);
CREATE TABLE stops (
	stopID INT NOT NULL,
	stopName VARCHAR(240) NOT NULL,
	stopCoordinates VARCHAR(128) NOT NULL,
	PRIMARY KEY (stopID)
);
CREATE TABLE stops_en_route (
	stopID INT NOT NULL,
	routeID INT NOT NULL,
	stopOrder INT NOT NULL,
	PRIMARY KEY (stopID, routeID),
	FOREIGN KEY(stopID) REFERENCES stops (stopID),
	FOREIGN KEY(routeID) REFERENCES routes (routeNo)
);
CREATE TABLE rides (
	rideID BIGINT NOT NULL,
	licensePlate VARCHAR(8) NOT NULL,
	routeNo INT NOT NULL,
	licenseID VARCHAR(24) NOT NULL,
	startTime DATETIME NOT NULL,
	PRIMARY KEY (rideID),
	FOREIGN KEY(licensePlate) REFERENCES buses (licensePlate),
	FOREIGN KEY(routeNo) REFERENCES routes (routeNo),
	FOREIGN KEY(licenseID) REFERENCES drivers (licenseID)
);
CREATE TABLE weeklytickets (
	ticketID INT NOT NULL,
	issueDate TIMESTAMP NOT NULL,
	passengerID INT NOT NULL,
	PRIMARY KEY (ticketID),
	FOREIGN KEY(passengerID) REFERENCES passengers (passengerID)
);
CREATE TABLE ticket_uses (
	useID INT NOT NULL,
	rideID BIGINT NOT NULL,
	w_ticketID INT,
	o_ticketID INT,
	PRIMARY KEY (useID)
);
