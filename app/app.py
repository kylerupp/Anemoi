from flask import Flask, jsonify
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/config", methods =['GET'])
def get_config():
    time = datetime.now()
    return jsonify({'date': time})