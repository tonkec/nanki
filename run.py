#! /usr/bin/env python3
# coding: utf-8

"""
Nan'Ki is a Japanese syllabary quiz written in Python 3

Author: Gareth Sciarrone
"""

"""
This script will run our web app using Flask micro-framework using the settings bellow.
If running on server such as cloud9
import os an run app with following settings :
hots=os.getenv('IP'), port=os.getenv('PORT')
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=int(5000),
            debug=True)
