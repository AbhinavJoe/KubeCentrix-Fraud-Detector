import mysql.connector
import json


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="J@itely54$",
        database="Customer_Services"
    )


def update_database_from_json():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    # Load data from the JSON file
    json_filename = 'phonebook_data.json'
    with open(json_filename, 'r') as json_file:
        phonebook_data = json.load(json_file)

    # Iterate through the data and update the database
    for entry in phonebook_data:
        contact_name = entry['ContactName']
        phone_number = entry['PhoneNumber']

        # Update the PhoneBook table
        update_query = "INSERT INTO PhoneBook (ContactName, PhoneNumber) VALUES (%s, %s) ON DUPLICATE KEY UPDATE ContactName = %s"
        values = (contact_name, phone_number, contact_name)

        cursor.execute(update_query, values)
        db_connection.commit()

        print(f"Contact '{contact_name}' with phone number '{
              phone_number}' successfully updated in the PhoneBook.")

    # Close the cursor and connection
    cursor.close()
    db_connection.close()


# Main script flow
update_database_from_json()
