import os
import signal
from flask import Flask, request
from buzz import generator
import pprint

app = Flask(__name__)
webhook = Webhook(app, endpoint='/payload')

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='localhost', port=4567) # port 5000 is the default