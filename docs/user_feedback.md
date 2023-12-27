# User Feedback Database Interaction

## Overview

This Python script interacts with a MySQL database to collect and manage user feedback for a customer service application. The script performs the following tasks:

1. **Insert User Feedback:**

   - Collects user information such as name, website URL, feedback text, and rating.
   - Inserts this feedback into the "UserFeedback" table in the MySQL database.

2. **Fetch and Store to JSON:**
   - Retrieves feedback data (Website URL and Feedback Text) from the "UserFeedback" table.
   - Converts the data into a list of dictionaries.
   - Stores the data in a JSON file named "feedback_data.json".

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

1. Run the script in a Python environment.

2. Enter the required information when prompted:

   - Customer Name
   - Website URL
   - Feedback Text
   - Rating (1-5)

3. The script will insert the feedback into the database and print the auto-generated FeedbackID.

4. The script will then fetch feedback data from the database, convert it into a JSON format, and save it to a file named "feedback_data.json".

## Note

- Ensure that the MySQL server is running and accessible.
- Replace the placeholder database connection details with your actual database credentials.

## Dependencies

1. Python 3.12
2. json module
3. os module

## File Structure

```
project_directory/
│
├──src/
│     └── user_feedback.py
└── data/
        └── UserFeedback.json
```

## License

This script is provided under the MIT License.
