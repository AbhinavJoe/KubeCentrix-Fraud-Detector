# Database Interaction and JSON Export
This Python script interacts with a MySQL database to update a phonebook and exports the data to a JSON file.

## Import Statements
```python
import mysql.connector
import json
```
## Database Connection
```python
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        # Input the password of your own local SQL Workbench database.
        password="",
        database="Customer_Services"
    )
```
## Update Phonebook Function
```python

def update_phonebook():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    contact_name = input("Enter the contact's name: ")
    phone_number = input("Enter the phone number: ")
    contact_detail = input("Enter additional details: ")

    update_query = "INSERT INTO PhoneBook (ContactName, PhoneNumber, Detail) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE PhoneNumber = %s, Detail = %s"
    values = (contact_name, phone_number, contact_detail,
              phone_number, contact_detail)

    cursor.execute(update_query, values)
    db_connection.commit()

    cursor.close()
    db_connection.close()

    print(f"Contact '{contact_name}' with phone number '{phone_number}' and details '{contact_detail}' successfully updated in the PhoneBook.")
```
## Fetch and Store to JSON Function
```python
def fetch_and_store_to_json():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    select_query = "SELECT ContactName, PhoneNumber FROM PhoneBook"
    cursor.execute(select_query)

    phonebook_data = cursor.fetchall()

    data_list = []

    for row in phonebook_data:
        data_list.append({
            'ContactName': row[0],
            'PhoneNumber': row[1]
        })

    cursor.close()
    db_connection.close()

    json_filename = 'phonebook_data.json'
    with open(json_filename, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data successfully stored in {json_filename}.")
```
## Main Script Flow
```python
while True:
    update_phonebook()
    fetch_and_store_to_json()
    user_input = input("Do you want to continue (yes/no)? ").lower()
    if user_input != 'yes':
        break
```
## Usage
Replace the placeholder credentials in the connect_to_database function with your MySQL database information.
Run the script, and it will prompt you to update the phonebook, store the data to a JSON file, and ask if you want to continue.
## License
This project is licensed under the MIT License 
