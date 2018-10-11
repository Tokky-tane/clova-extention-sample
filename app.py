# coding:utf-8
from flask import Flask, request, jsonify
import os
from cek import Clova
import datetime

app = Flask(__name__)

application_id = os.environ.get("APPLICATION_ID")
clova = Clova(application_id, debug_mode=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/app', methods=['POST'])
def my_service():
    resp = clova.route(request.data, request.headers)
    resp = jsonify(resp)
    resp.headers['Content-Type'] = 'application/json;charset-UTF-8'
    return resp


@clova.handle.launch
def launch_request_handler(clova_request):
    return clova.response("こんにちは世界。スキルを起動します")


@clova.handle.default
def default_handler(clova_request):
    return clova.response("もう一度お願いします")


if __name__ == '__main__':
    app.run()
