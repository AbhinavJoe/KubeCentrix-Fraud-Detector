from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from truecallerpy import search_phonenumber
import mysql.connector
import json
from datetime import datetime
import os
import asyncio
import requests
import whois


app = Flask(__name__)
CORS(app)

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/feedback_data.json")

words_file_path = os.path.join(current_directory, "word_list.json")

id = "a1i04--kE1GeYFb-hPQ7gmvIWvjV8hTQdI74aC1IDKiDcogB0zyFezzT0764fYMQ"


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
                return f"{phone_number} does not have enough information available."

            return f"{phone_number} is legit. This number belongs to {contact_name}."
        else:
            return f"{phone_number} does not have enough information available."

    except Exception as e:
        print(f"Error: {e}")
        return f"{phone_number} is suspicious. Unable to verify!"


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rock_Hopper1",
        database="Customer_Services"
    )


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

    # Close the cursor and connection
    cursor.close()
    db_connection.close()

    return feedback_id


@app.route('/')
def popup():
    return render_template('index.html')


@app.route('/verification')
def verification():
    return render_template('verification.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')


@app.route('/submitnumber', methods=['POST'])
def submit_number():
    phone_number = request.form['phone_number']
    # Run the asynchronous coroutine using an event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(check_truecaller(phone_number))
    loop.close()

    return render_template('verification.html', result=result)


@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    try:
        # Retrieve data from the request
        data = request.form
        customer_name = data.get("customer_name")
        website_url = data.get("website_url")
        feedback_text = data.get("feedback_text")
        rating = data.get("rating")

        # Insert feedback into the database
        feedback_id = insert_user_feedback(
            customer_name, website_url, feedback_text, rating)

        # Fetch and store data to JSON file
        fetch_and_store_to_json()

        response = "Your feedback has been recorded. Thank You."

    except Exception as e:
        response = f"An error occurred: {str(e)}. Please try again later."

    return render_template('feedback.html', response=response)


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
    with open(json_file_path, 'w') as json_file:
        json.dump(data_list, json_file, indent=2)

    print(f"Data successfully stored in feedback_data.json.")


with open(words_file_path) as f:
    suspicious_words = json.load(f)


def check_ssl(url):
    try:
        response = requests.get(url)
        return response.url.startswith('https://')
    except:
        return False


def check_suspicious_words(content, word_list):
    return any(word in content for word in word_list)


def get_website_age(domain):
    try:
        whois_info = whois.whois(domain)
        return (datetime.datetime.now() - whois_info.creation_date).days
    except:
        return None


@app.route('/check_website', methods=['POST'])
def check_website():
    data = request.json
    url = data['url']

    # Check SSL Verification
    ssl_verified = check_ssl(url)

    # Check for Suspicious Words
    response = requests.get(url)
    contains_suspicious_words = check_suspicious_words(
        response.text, suspicious_words)

    # Check Website Registration Date
    website_age = get_website_age(url)

    # Calculate Trust Score (this is a simplistic scoring system)
    trust_score = 10
    if not ssl_verified:
        trust_score -= 3
    if contains_suspicious_words:
        trust_score -= 4
    if website_age is not None and website_age < 30:  # less than 30 days
        trust_score -= 3

    # Determine if the website is potentially fraudulent
    is_fraudulent = trust_score < 5

    return jsonify({
        'trust_score': trust_score,
        'is_fraudulent': is_fraudulent
    })


@app.route('/blocked')
def blocked():
    return render_template('blocked.html')


if __name__ == '__main__':
    app.run(debug=True)
