import mysql.connector
import json


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="J@itely54$",
        database="Customer_Services"
    )


def update_phonebook():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    # Take user input for contact details
    contact_name = input("Enter the contact's name: ")
    phone_number = input("Enter the phone number: ")
    contact_detail = input("Enter additional details: ")

    # Update the PhoneBook table
    update_query = "INSERT INTO PhoneBook (ContactName, PhoneNumber, Detail) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE PhoneNumber = %s, Detail = %s"
    values = (contact_name, phone_number, contact_detail,
              phone_number, contact_detail)

    cursor.execute(update_query, values)
    db_connection.commit()

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

    print(f"Contact '{contact_name}' with phone number '{phone_number}' and details '{
          contact_detail}' successfully updated in the PhoneBook.")


def fetch_and_store_to_json():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    # Fetch data from the PhoneBook table
    select_query = "SELECT ContactName, PhoneNumber FROM PhoneBook"
    cursor.execute(select_query)

    # Fetch all the rows
    phonebook_data = cursor.fetchall()

    # Create a list to store the data
    data_list = []

    # Convert the data to a list of dictionaries
    for row in phonebook_data:
        data_list.append({
            'ContactName': row[0],
            'PhoneNumber': row[1]
        })

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

    # Save the data to a JSON file
    json_filename = 'phonebook_data.json'
    with open(json_filename, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data successfully stored in {json_filename}.")


# Main script flow
while True:
    update_phonebook()
    fetch_and_store_to_json()
    user_input = input("Do you want to continue (yes/no)? ").lower()
    if user_input != 'yes':
        break
