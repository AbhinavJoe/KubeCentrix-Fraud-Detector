from flask import Flask, request, render_template, jsonify
from truecallerpy import search_phonenumber
import mysql.connector
import json
from datetime import datetime
import os
import asyncio

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/feedback_data.json"
)


app = Flask(__name__)


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rock_Hopper1",
        database="Customer_Services"
    )


id = "a1i04--kE1GeYFb-hPQ7gmvIWvjV8hTQdI74aC1IDKiDcogB0zyFezzT0764fYMQ"


async def check_truecaller(phone_number):
    try:
        result = await search_phonenumber({"phone_number": phone_number}, "IN", id)
        contact_name = result['data']['data'][0]['name']
        return f"{phone_number} is legit. This number belongs to {contact_name}."
    except Exception as e:
        print(f"Error: {e}")
        return f"{phone_number} is suspicious. Unable to verify!"


@app.route('/')
def popup():
    return render_template('popup.html')


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


# @app.route('/submitfeedback', methods=['POST'])
# def submit_feedback():
#     website_url = request.form['website_url']
#     feedback_text = request.form['feedback_text']
#     rating = request.form['rating']
#     print(
#         f'Feedback URL: {website_url}, Feedback Text: {feedback_text}, User Rating: {rating}')
#     return render_template('feedback.html', website_url=website_url, feedback_text=feedback_text, rating=rating)

@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    try:
        db_connection = connect_to_database()
        cursor = db_connection.cursor()

        # Retrieve data from the request
        data = request.json
        customer_name = data.get("customer_name")
        website_url = data.get("website_url")
        feedback_text = data.get("feedback_text")
        rating = data.get("rating")

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

        response = {
            "success": True,
            "message": f"Feedback successfully added to the database with FeedbackID: {feedback_id}."
        }

    except Exception as e:
        response = {
            "success": False,
            "message": f"An error occurred: {str(e)}"
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
