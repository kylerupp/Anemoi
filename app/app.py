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

@app.route('/endpoint', methods = ['POST'])
def post_endpoint():
    endpoint_info = request.json
    lcl_cnx = connector.get_connection()
    cur = lcl_cnx.cursor()
    result = connector.create_endpoint(
        endpoint_info['mac'],
        lcl_cnx,
        cur)
    lcl_cnx.close()
    return jsonify({'endpoint': result})

@app.route('/temp', methods = ['POST'])
def post_temp():
    temp_info = request.json
    lcl_cnx = connector.get_connection()
    cur = lcl_cnx.cursor()
    result = connector.create_temp(
        temp_info['mac'],
        temp_info['temp'],
        temp_info['log'],
        lcl_cnx,
        cur)
    lcl_cnx.close()
    return jsonify({'temp': result})
