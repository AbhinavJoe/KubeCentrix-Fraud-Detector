from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from truecallerpy import search_phonenumber
import mysql.connector
import json
from datetime import datetime
import os
import asyncio
import requests
from bs4 import BeautifulSoup
import re
import whois

app = Flask(__name__)
CORS(app)

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/feedback_data.json"
)

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


# Phishing Detection Endpoint
@app.route('/scan', methods=['POST'])
def website_scanning():
    data = request.json
    url = data.get("url")
    word_list = data.get("word_list")
    threshold = 7

    if not url or not word_list:
        return jsonify({"error": "Missing url or word_list"}), 400

    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            all_text = ' '.join([element.get_text(separator=' ') for element in soup.find_all(
                ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'div'])])
            matching_words = [word for word in re.findall(
                r'\b\w+\b', all_text) if word.lower() in map(str.lower, word_list)]

            # Determine if the site is fraudulent based on the number of matching words
            is_fraudulent = len(matching_words) >= threshold

            return jsonify({
                "isFraudulent": is_fraudulent,
                "matching_words": matching_words,
                "count": len(matching_words)
            })
        else:
            return jsonify({"error": "Failed to retrieve the webpage"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# SSL Verification Endpoint
@app.route('/check_ssl', methods=['POST'])
def check_ssl():
    data = request.json
    url = data.get("url")
    try:
        if not url:
            return jsonify({"error": "Missing url"}), 400

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                if response.url.startswith("https://"):
                    return jsonify({"url": url, "ssl": True, "message": "The website uses SSL."})
                else:
                    return jsonify({"url": url, "ssl": False, "message": "The website does not use SSL."})
            else:
                return jsonify({"url": url, "error": f"Failed to retrieve the website. Status code: {response.status_code}"}), response.status_code
        except Exception as e:
            return jsonify({"url": url, "error": f"An error occurred: {e}"}), 500
    except Exception as e:
        app.logger.error(f"Error in check_ssl: {e}")
        return jsonify({"url": url, "error": f"An error occurred: {e}"}), 500


# Domain Authenticity Endpoint
@app.route('/check_domain_authenticity', methods=['POST'])
def get_domain_registration_date():
    data = request.json
    domain_name = data.get("domain_name")

    if not domain_name:
        return jsonify({"error": "Missing domain name"}), 400

    try:
        domain_info = whois.whois(domain_name)
        registration_date = domain_info.creation_date

        if registration_date:
            if isinstance(registration_date, list):
                registration_date = registration_date[0]

            formatted_date = registration_date.strftime('%Y-%m-%d %H:%M:%S')
            time_period = calculate_time_period(registration_date)
            return jsonify({
                "domain_name": domain_name,
                "registration_date": formatted_date,
                "days_registered": time_period
            })
        else:
            return jsonify({
                "domain_name": domain_name,
                "error": "Registration date not available"
            }), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def calculate_time_period(registration_date):
    try:
        registration_date = datetime.strptime(
            str(registration_date), '%Y-%m-%d %H:%M:%S')
        current_date = datetime.now()
        return (current_date - registration_date).days
    except Exception as e:
        return str(e)


@app.route('/blocked', methods=['POST'])
def blocked():
    return render_template('blocked.html')


if __name__ == '__main__':
    app.run(debug=True)
