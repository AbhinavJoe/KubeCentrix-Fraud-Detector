# PhoneBook Data Update Script

## Overview

This Python script updates a MySQL database with phonebook data from a JSON file. The script performs the following tasks:

1. **Connect to Database:**

   - Establishes a connection to the MySQL database named "Customer_Services" with the provided credentials.

2. **Update Database from JSON:**
   - Loads phonebook data from a JSON file named "phonebook_data.json".
   - Iterates through the data and updates the "PhoneBook" table in the database.
   - Uses the `INSERT INTO ... ON DUPLICATE KEY UPDATE` MySQL syntax to insert a new record or update an existing record based on the unique key.
   - Prints a message for each successfully updated contact.

## Requirements

Before running the script, ensure you have the following:

- MySQL server installed and running.
- Python interpreter installed.
- `mysql-connector-python` library installed (`pip install mysql-connector-python`).

## Configuration

In the script, there is a `connect_to_database` function that establishes a connection to the MySQL database. You need to configure the connection parameters such as `host`, `user`, `password`, and `database`. Replace the placeholder values with your actual database credentials.

```python
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Customer_Services"
    )
```

## Usage

1. Ensure that the MySQL server is running and accessible.
2. Run the script in a Python environment.
3. The script will load data from the "phonebook_data.json" file and update the "PhoneBook" table in the database.
4. The script will print a message for each successfully updated contact.

## Note

- Replace the placeholder database connection details with your actual database credentials.
- The script assumes that the "PhoneBook" table has a unique key constraint on the "ContactName" column.

## License

This script is licensed under the MIT License.
