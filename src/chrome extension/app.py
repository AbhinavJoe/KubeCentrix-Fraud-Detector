from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('popup.html')


@app.route('/submitnumber', methods=['POST'])
def submit_number():
    number = request.form['number']

    # Process the form data as needed
    # For example, you can print the data
    print(f'Number: {number}')

    # Redirect or render another template as needed
    return render_template('result.html', number=number)


@app.route('/submitfeedback', methods=['POST'])
def submit_feedback():
    feedbackurl = request.form['feedbackurl']
    feedbacktext = request.form['feedbacktext']

    # Process the form data as needed
    # For example, you can print the data
    print(f'Feedback URL: {feedbackurl}, Feedback Text: {feedbacktext}')

    # Redirect or render another template as needed
    return render_template('result.html', feedbackurl=feedbackurl, feedbacktext=feedbacktext)


if __name__ == '__main__':
    app.run(debug=True)
