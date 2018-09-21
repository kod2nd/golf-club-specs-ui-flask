from flask import render_template, request
import requests
import json


from golf_spec_ui import app

def displayHello(name):
    if request.method == 'GET':
        response = requests.get('https://golf-specs-api.herokuapp.com/')
        data = response.json()
        # indexDict = json.loads(data)
        print("STATUS CODEEEE", data["message"])
        return render_template('index.html', name=name)
    else:
        return render_template('index.html', name="no one")

@app.route('/', methods=['GET'])
@app.route('/<name>')
def index(name=" "):
    return displayHello(name)
