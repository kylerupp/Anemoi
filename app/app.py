from flask import Flask, jsonify, request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/config", methods =['GET'])
def get_config():
    time = datetime.now()
    return jsonify({'date': time})

@app.route('/data', methods =['POST'])
def handle_data():
    endpoint_params = request.json
    print(endpoint_params['id'])
    print(endpoint_params['temp'])
    print(endpoint_params['time'])
    return jsonify({'message': 'OK'})
