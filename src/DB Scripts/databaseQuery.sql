CREATE DATABASE DataBase_Customer_Services;
USE DataBase_Customer_Services;

CREATE TABLE UserFeedback (
    FeedbackID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    SiteURL TEXT,
    FeedbackText TEXT,
    Rating INT,
    Timestamp TIMESTAMP
);

CREATE TABLE PhoneBook (
    ContactID INT PRIMARY KEY,
    ContactName VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Detail TEXT
);
CREATE TABLE FraudulentDataWebsite (
    WebsiteID INT PRIMARY KEY,
    WebsiteName VARCHAR(100),
    Description TEXT,
    ReportDate TIMESTAMP
);

-- ALTER TABLE PhoneBook
-- DROP COLUMN Detail;

SELECT * FROM UserFeedback;

-- DROP TABLE UserFeedback;
