# from flask import Flask, request
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)


# @app.route('/receive_data', methods=['POST'])
# def receive_data():
#     data = request.json
#     fraudulent_url = data.get('fraudulent_url')

#     # Path to your JSON file where URLs will be stored
#     json_file_path = 'fraudulent_urls.json'

#     # Read existing data
#     try:
#         with open(json_file_path, 'r') as file:
#             urls = json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         urls = []

#     # Append new URL
#     urls.append(fraudulent_url)

#     # Write updated data back to file
#     with open(json_file_path, 'w') as file:
#         json.dump(urls, file, indent=4)

#     return "URL Received and Stored", 200


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)


from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Hardcoded admin credentials (replace with a secure authentication system)
admin_username = "admin1"
admin_password = "Pass1"


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == admin_username and password == admin_password:
        return "Login Successful", 200
    else:
        return "Invalid Credentials", 401


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    fraudulent_url = data.get('fraudulent_url')

    # Path to your JSON file where URLs will be stored
    json_file_path = 'fraudulent_urls.json'

    # Read existing data
    try:
        with open(json_file_path, 'r') as file:
            urls = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        urls = []

    # Append new URL
    urls.append(fraudulent_url)

    # Write updated data back to file
    with open(json_file_path, 'w') as file:
        json.dump(urls, file, indent=4)

    return "URL Received and Stored", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
