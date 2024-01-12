from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import re
import whois
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Phishing Detection Endpoint
@app.route('/scan', methods=['POST'])
def website_scanning():
    data = request.json
    url = data.get("url")
    word_list = data.get("word_list")

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

            return jsonify({
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

# Domain Authenticity Endpoint
@app.route('/check_domain_authenticity', methods=['POST'])
def get_domain_registration_date():
    data = request.json
    domain_name = data.get("domain_name")

    if not domain_name:
        return jsonify({"error": "Missing domain name"}), 400

    try:
        domain_info = whois.whois(domain_name)
        registration_dates = domain_info.creation_date

        if isinstance(registration_dates, list):
            registration_date = registration_dates[0]
        else:
            registration_date = registration_dates

        time_period = calculate_time_period(registration_date)
        return jsonify({
            "domain_name": domain_name,
            "registration_date": registration_date.strftime('%Y-%m-%d %H:%M:%S'),
            "days_registered": time_period
        })
    except whois.parser.PywhoisError as e:
        return jsonify({"error": str(e)}), 500

def calculate_time_period(registration_date):
    try:
        registration_date = datetime.strptime(str(registration_date), '%Y-%m-%d %H:%M:%S')
        current_date = datetime.now()
        return (current_date - registration_date).days
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
