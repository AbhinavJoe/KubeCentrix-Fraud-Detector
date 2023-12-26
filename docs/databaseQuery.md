# MySQL Database Setup
This set of SQL statements creates a MySQL database named DCustomer_Services with three tables: UserFeedback, PhoneBook, and FraudulentDataWebsite. It also includes some commented-out statements for potential alterations.

## Database Creation and Usage
```sql

CREATE DATABASE Customer_Services;
USE DataBase_Customer_Services;
```
## UserFeedback Table

```sql

CREATE TABLE UserFeedback (
    FeedbackID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    SiteURL TEXT,
    FeedbackText TEXT,
    Rating INT,
    Timestamp TIMESTAMP
);
```
## PhoneBook Table
```sql

CREATE TABLE PhoneBook (
    ContactID INT PRIMARY KEY,
    ContactName VARCHAR(50),
    PhoneNumber VARCHAR(15),
    Detail TEXT
);
```
Commented-out statement to potentially drop the Detail column:

```sql

-- ALTER TABLE PhoneBook
-- DROP COLUMN Detail;

```
## FraudulentDataWebsite Table

```sql
   CREATE TABLE FraudulentDataWebsite (
    WebsiteID INT PRIMARY KEY,
    WebsiteName VARCHAR(100),
    Description TEXT,
    ReportDate TIMESTAMP
);
```
Select All Records from UserFeedback
```sql
SELECT * FROM UserFeedback;
```

Commented Out Drop Table Statement
```sql
-- DROP TABLE UserFeedback;
```

## License
This MySQL database setup script is provided under the MIT License.
