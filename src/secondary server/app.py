from flask import Flask, request

app = Flask(__name__)


@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json
    fraudulent_url = data.get('fraudulent_url')

    # Logic to handle the received fraudulent URL
    print(f"Received fraudulent URL: {fraudulent_url}")

    return "URL Received", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
