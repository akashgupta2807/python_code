#! /usr/bin/env python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def message():
    return 'Python is cool!'

app.run()
