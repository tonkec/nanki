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


from flask import Flask, render_template, request, redirect
from datetime import datetime
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            now = datetime.now().strftime("%Y.%m.%d : %H:%M:%S")
            user_list.writelines(now + " - " + request.form["username"] + " - logged in\n")
        return redirect(request.form["username"])
    return render_template('index.html')


@app.route('/<username>')
def user_page(username):
    return render_template("quiz-sel.html", user=username)


@app.route('/<username>/<kana>')
def quiz(username, kana):
    with open('data/syllabary.json', 'r') as kanji_data:
        kanjis = json.load(kanji_data)
        guess = kanjis[0]

    return render_template('quiz.html', user=username, guess=guess, kana=kana)


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=int(5000),
            debug=True)
