import datetime
import random
import string

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"


@app.route("/now")
def now():  # view function
    return str(datetime.datetime.now())


@app.route('/random')
def get_random():  # view function
    length = int(request.args['length'])
    result = ''
    for i in range(length):
        result += random.choice(string.ascii_lowercase)
    return result


app.run()
