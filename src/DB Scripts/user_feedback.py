import mysql.connector
import json
from datetime import datetime

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="J@itely54$",       # need to repalce 
        database="Customer_Services"
    )

def insert_user_feedback():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    # Take user feedback input
    customer_name = input("Enter your name: ")
    website_url = input("Enter the website URL: ")
    feedback_text = input("Enter your feedback: ")
    rating = float(input("Enter your rating (1-5): "))

    # Get the current timestamp
    timestamp = datetime.now()

    # Insert the feedback into the UserFeedback table
    insert_query = "INSERT INTO UserFeedback (CustomerName, Website_URL, FeedbackText, Rating, Timestamp) VALUES (%s, %s, %s, %s, %s)"
    values = (customer_name, website_url, feedback_text, rating, timestamp)

    cursor.execute(insert_query, values)
    db_connection.commit()

    # Fetch the auto-generated FeedbackID
    cursor.execute("SELECT LAST_INSERT_ID()")
    feedback_id = cursor.fetchone()[0]

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

    print(f"Feedback successfully added to the database with FeedbackID: {feedback_id}.")

def fetch_and_store_to_json():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    # Fetch data from the UserFeedback table
    select_query = "SELECT Website_URL, FeedbackText FROM UserFeedback"
    cursor.execute(select_query)

    # Fetch all the rows
    feedback_data = cursor.fetchall()

    # Create a list to store the data
    data_list = []

    # Convert the data to a list of dictionaries
    for row in feedback_data:
        data_list.append({
            'Website_URL': row[0],
            'FeedbackText': row[1]
        })

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

    # Save the data to a JSON file
    json_filename = 'feedback_data.json'
    with open(json_filename, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data successfully stored in {json_filename}.")

# Main script flow
insert_user_feedback()
fetch_and_store_to_json()
