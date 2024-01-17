# Importing libraries
from flask import Flask, request, render_template, jsonify
import requests
from flask_cors import CORS
from truecallerpy import search_phonenumber
import pickle
import re
from urllib.parse import urlparse
import pandas as pd
import mysql.connector
import json
from datetime import datetime
import os
import asyncio


app = Flask(__name__)
CORS(app)

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/feedback_data.json")

model_path = os.path.join(current_directory, "../../models/model.pkl")

id = "a1i0G--kQ_JjlkNktMTu0VpvpCIecw2f_31zk1iirNejrrOvLRLS2EB7l76rrjgJ"


''' This asynchronous function 'check_truecaller' is designed to verify phone numbers using the Truecaller API. It takes a phone number as input and checks its legitimacy and spam status. The function returns different messages based on the information retrieved from the API. It handles both successful data retrieval and exceptions that might occur during the process.'''


async def check_truecaller(phone_number):
    try:
        result = await search_phonenumber({"phone_number": phone_number}, "IN", id)
        if result['status_code'] == 200 and result['data']['data']:
            phone_data = result['data']['data'][0]

            if 'spamInfo' in phone_data:
                spam_info = phone_data['spamInfo']
                spam_score = spam_info.get('spamScore', 0)
                spam_type = spam_info.get('spamType', '')

                if spam_score > 0 and spam_type:
                    return f"{phone_number} is likely spam. Type: {spam_type}, Score: {spam_score}."

            contact_name = phone_data.get('name', 'Unknown')

            if contact_name == 'Unknown':
                return f"{phone_number} does not have enough information available. May be suspicious."

            return f"{phone_number} is legit. This number belongs to {contact_name}."
        else:
            return f"{phone_number} does not have enough information available. May be suspicious."

    except Exception as e:
        print(f"Error: {e}")
        return f"{phone_number} is not a valid number. Unable to verify!"


'''This function 'connect_to_database' establishes a connection to a MySQL database.It uses the mysql.connector.connect method to create this connection.The database connection parameters such as host, user, password, and the specific database name are provided.
The function returns a connection object which can be used to interact with the database.'''


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rock_Hopper1",
        database="Customer_Services"
    )


''' This function 'insert_user_feedback' is designed to insert customer feedback into a database.It takes customer name, website URL, feedback text, and rating as inputs.The function establishes a database connection, inserts the feedback data into the UserFeedback table,
and then returns the auto-generated feedback ID. '''


def insert_user_feedback(customer_name, website_url, feedback_text, rating):
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

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

    cursor.close()
    db_connection.close()

    return feedback_id


'''Render the 'index.html' template when accessing the root URL '/' '''


@app.route('/')
def popup():
    return render_template('index.html')


'''Render the 'verification.html' template when accessing '/verification' route when the verify number button is clicked in the popup '''


@app.route('/verification')
def verification():
    return render_template('verification.html')


'''Render the 'feeback.html' template when accessing '/feedback' route when then user feedback is clicked  '''


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


'''This route '/submitnumber' is defined to handle POST requests in a web application. When a POST request is received, it extracts a phone number from the request form,runs an asynchronous function 'check_truecaller' to verify the phone number,and then renders a template with the verification result.'''


@app.route('/submitnumber', methods=['POST'])
def submit_number():
    phone_number = request.form['phone_number']
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(check_truecaller(phone_number))
    loop.close()

    return render_template('verification.html', result=result)


'''This route '/submitfeedback' is defined to handle POST requests for submitting feedback in a web application.It retrieves feedback data from the request form, inserts the data into a database, and may perform additional operations like storing data to a JSON file.The function returns a response to the user by rendering an HTML template with a success or error message.'''


@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.form
        customer_name = data.get("customer_name")
        website_url = data.get("website_url")
        feedback_text = data.get("feedback_text")
        rating = data.get("rating")

        feedback_id = insert_user_feedback(
            customer_name, website_url, feedback_text, rating)

        fetch_and_store_to_json()

        response = "Your feedback has been recorded. Thank You."

    except Exception as e:
        response = f"An error occurred: {str(e)}. Please try again later."

    return render_template('feedback.html', response=response)


'''This function 'fetch_and_store_to_json' connects to a database, retrieves feedback data from the UserFeedback table, and then stores this data in a JSON file.It fetches data, formats it into a list of dictionaries, and writes this list to a JSON file.The function ensures proper closure of database connections and hand'''


def fetch_and_store_to_json():
    db_connection = connect_to_database()
    cursor = db_connection.cursor()

    select_query = "SELECT Website_URL, FeedbackText FROM UserFeedback"
    cursor.execute(select_query)

    feedback_data = cursor.fetchall()

    data_list = []

    for row in feedback_data:
        data_list.append({
            'Website_URL': row[0],
            'FeedbackText': row[1]
        })

    cursor.close()
    db_connection.close()

    with open(json_file_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data successfully stored in feedback_data.json.")


'''# This Flask route '/ml_check' is used to check if a given URL is legitimate or suspicious using a machine learning model. The route handles POST requests with a URL in the JSON payload. It uses an 'extract_features' function to convert the URL into a feature set, and then applies a pre-trained machine learning model to predict the '''


def extract_features(url):
    special_chars = [';', '?', '=', '&']
    features = {'length': len(url),
                'has_ip': int(bool(re.match(r'\d+\.\d+\.\d+\.\d+', url))),
                'count_special': sum(map(url.count, special_chars)),
                'https': url.startswith('https')
                }
    return features


'''This Flask route '/ml_check' is used to check if a given URL is legitimate or suspicious using a machine learning model. The route handles POST requests with a URL in the JSON payload. It uses an 'extract_features' function to convert the URL into a feature set, and then applies a pre-trained machine learning model to predict the URL's class (legitimate or suspicious).'''


@app.route('/ml_check', methods=['POST'])
def ml_check():
    data = request.json
    url = data.get("url")

    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    if not url:
        return jsonify({"error": "Missing URL"}), 400

    features = extract_features(url)
    features_df = pd.DataFrame([features])

    predicted_class = model.predict(features_df)[0]

    if predicted_class == 0:
        result = 'Legitimate'
    else:
        result = 'Suspicious'
        try:
            # Send URL to the secondary Flask server
            # Replace with actual URL
            secondary_server_url = 'http://127.0.0.1:5001/receive_data'
            response = requests.post(secondary_server_url, json={
                                     'fraudulent_url': url})

            if response.status_code == 200:
                print("Data successfully sent to secondary server.")
            else:
                print("Failed to send data to secondary server.")
        except requests.exceptions.RequestException as e:
            print(f"Error sending data to secondary server: {e}")

    return jsonify({"result": result})


@app.route('/blocked')
def blocked():
    return render_template('blocked.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
