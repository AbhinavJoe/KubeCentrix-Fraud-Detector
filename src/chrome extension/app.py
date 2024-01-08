from flask import Flask, render_template, request
from truecallerpy import search_phonenumber

app = Flask(__name__)

id = "a1i04--kE1GeYFb-hPQ7gmvIWvjV8hTQdI74aC1IDKiDcogB0zyFezzT0764fYMQ"

async def check_truecaller(phone_number):
    try:
        result = await search_phonenumber({"phone_number": phone_number}, "IN", id)
        contact_name = result['data']['data'][0]['name']
        return f"{phone_number} is legit. This number belongs to {contact_name}."
    except Exception as e:
        print(f"Error: {e}")
        return f"{phone_number} is suspicious. Unable to verify with Truecaller."

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/submitnumber', methods=['POST'])
def submit_number():
    phone_number = request.form['phone_number']
    result = check_truecaller(phone_number)
    return render_template('templates/verification.html', result=result)

@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    website_url = request.form['website_url']
    feedback_text = request.form['feedback_text']
    print(f'Feedback URL: {website_url}, Feedback Text: {feedback_text}')
    return render_template('templates/feedback.html', feedbackurl=website_url, feedbacktext=feedback_text)

if __name__ == '__main__':
    app.run(debug=True)
