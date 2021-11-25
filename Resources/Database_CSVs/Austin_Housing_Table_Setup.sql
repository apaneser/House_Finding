CREATE TABLE house_info
(
	zpid integer NOT NULL PRIMARY KEY,
	description text,
	propertyTaxRate decimal,
	hasAssociation varchar(10),
	hasCooling varchar(10),
	hasGarage varchar(10),
	hasHeating varchar(10),
	hasSpa varchar(10),
	hasView varchar(10),
	homeType varchar(50),
	yearBuilt int,
	latestPrice decimal,
	latest_saleyear int,
	lotSizeSqFt decimal,
	livingAreaSqFt decimal,
	numOfBathrooms decimal,
	numOfBedrooms decimal,
	numOfStories decimal
);

CREATE TABLE house_location
(
	zpid integer NOT NULL PRIMARY KEY,
	city varchar(50),
	streetAddress varchar(50),
	zipcode int,
	latitude decimal,
	longitude decimal
);

CREATE TABLE house_features
(
	zpid int NOT NULL PRIMARY KEY,
	garageSpaces int,
	parkingSpaces int,
	numOfAccessibilityFeatures int,
	numOfAppliances int,
	numOfParkingFeatures int,
	numOfPatioAndPorchFeatures int,
	numOfSecurityFeatures int,
	numOfWaterfrontFeatures int,
	numOfWindowFeatures int,
	numOfCommunityFeatures int
);

CREATE TABLE house_school
(
	zpid int,
	numOfPrimarySchools int,
	numOfElementarySchools int,
	numOfMiddleSchools int,
	numOfHighSchools int,
	avgSchoolDistance decimal,
	avgSchoolRating decimal,
	avgSchoolSize int,
	MedianStudentsPerTeacher int
);
