from checkno import check_phone_number
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

current_directory = os.path.dirname(os.path.realpath(__file__))
json_file_path = os.path.join(
    current_directory, "../../data/phonebook_data.json"
)


@app.route('/')
def index():
    return render_template('popup.html')


@app.route('/submitnumber', methods=['POST'])
def submit_number():
    phone_number = request.form['phone_number']

    # # Process the form data as needed
    # # For example, you can print the data
    # print(f'Number: {phone_number}')

    # # Redirect or render another template as needed
    # return render_template('result.html', number=phone_number)

    result = check_phone_number(phone_number)
    return render_template('verification.html', result=result)


@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    website_url = request.form['website_url']
    feedback_text = request.form['feedback_text']

    # Process the form data as needed
    # For example, you can print the data
    print(f'Feedback URL: {website_url}, Feedback Text: {feedback_text}')

    # Redirect or render another template as needed
    return render_template('result.html', feedbackurl=website_url, feedbacktext=feedback_text)


if __name__ == '__main__':
    app.run(debug=True)
