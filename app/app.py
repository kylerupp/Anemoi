from datetime import datetime
from flask import abort, Flask, jsonify, request
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

@app.route("/time", methods = ['GET'])
def get_config():
    time = datetime.now()
    return jsonify({'date': time})

@app.route('/endpoint/<mac>', methods = ['GET', 'POST', 'PATCH'])
def get_endpoint(mac):
    lcl_cnx = connector.get_connection()
    cur = lcl_cnx.cursor()
    if request.method == 'GET':
        result = connector.get_endpoint(mac, cur)
        if(result == None):
            lcl_cnx.close()
            abort(404)
    if request.method == 'POST':
        result = connector.create_endpoint(mac, lcl_cnx, cur)
    if request.method == 'PATCH':
        result = connector.update_endpoint(mac, lcl_cnx, cur)
    lcl_cnx.close()
    return jsonify({'endpoint': result})

@app.route('/endpoint/<mac>/firmware', methods = ['GET', 'POST', 'PATCH'])
def get_endpoint_firmware(mac):
    lcl_cnx = connector.get_connection()
    cur = lcl_cnx.cursor()
    params = None
    if request.method == 'GET':
        result = connector.get_endpoint_firmware(mac, cur)
        if(result == None):
            lcl_cnx.close()
            abort(404)
    else:
        params = request.json
    if request.method == 'POST':
        result = connector.create_endpoint_firmware(mac, params['firmware'], lcl_cnx, cur)
    if request.method == 'PATCH':
        result = connector.update_endpoint_firmware(mac, params['firmware'], lcl_cnx, cur)
    lcl_cnx.close()
    return jsonify({'endpoint': result})


@app.route('/data', methods = ['POST'])
def post_data():
    data_info = request.json
    lcl_cnx = connector.get_connection()
    cur = lcl_cnx.cursor()
    result = connector.create_data(
        data_info['mac'],
        data_info['temp'],
        lcl_cnx,
        cur)
    lcl_cnx.close()
    return jsonify({'data': result})     
