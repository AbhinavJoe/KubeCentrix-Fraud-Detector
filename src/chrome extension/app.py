from flask import Flask, render_template, request
from truecallerpy import search_phonenumber
import asyncio

app = Flask(__name__)

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


@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    website_url = request.form['website_url']
    feedback_text = request.form['feedback_text']
    rating = request.form['rating']
    print(
        f'Feedback URL: {website_url}, Feedback Text: {feedback_text}, User Rating: {rating}')
    return render_template('feedback.html', website_url=website_url, feedback_text=feedback_text, rating=rating)


if __name__ == '__main__':
    app.run(debug=True)
