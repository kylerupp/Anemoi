from datetime import datetime
from flask import Flask, jsonify, request
from os import environ

import connector

app = Flask(__name__)

config = {
    "user": environ.get('SQL_USER'),
    "password": environ.get('SQL_PASS'),
    "host": environ.get('SQL_HOST'),
    "database": environ.get('SQL_DB')
}
cnx = connector.create_connection(config)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/config", methods = ['GET'])
def get_config():
    time = datetime.now()
    return jsonify({'date': time})

@app.route('/endpoint', methods= ['POST'])
def post_endpoint():
    endpoint_params = request.json
    lcl_cnx = connector.get_connection()
    cur = lcl_cnx.cursor()
    result = connector.create_endpoint(endpoint_params['mac'], lcl_cnx, cur)
    cnx.close()
    return jsonify({'endpoint': result})

@app.route('/data', methods = ['POST'])
def handle_data():
    endpoint_params = request.json
    print(endpoint_params['id'])
    print(endpoint_params['temp'])
    print(endpoint_params['time'])
    return jsonify({'message': 'OK'})
