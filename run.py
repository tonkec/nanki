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
import random
import json


app = Flask(__name__)


class Player:
    """Creates player profile for each new user logged"""
    def __init__(self, username):
        self.name = username
        self.score = 0


def get_random_kana():
    """Selects the character to guess"""
    with open('data/syllabary.json', 'r') as json_data:
        kanas = json.load(json_data)
    print("kanas : ", kanas)
    return kanas


def check_answer(answer, guess, score):
    """Compare answer and selected character"""
    if answer == guess['name']:
        print('Right answer')
        score += 1
        print(score)
    if answer != guess['name']:
        print('Wrong answer')
        score -= 2
        print(score)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        with open("data/users.txt", "a") as user_list:
            now = datetime.now().strftime("%Y.%m.%d : %H:%M:%S")
            user_list.writelines(now + " - " + request.form["username"] + " - logged in\n")
        return redirect("log/" + request.form["username"])
    return render_template('index.html')


@app.route('/log/<username>')
def user_page(username):
    """
    Quiz selection page, with logic to select 20 random characters from selected syllabary
    """
    player = Player(username)

    print(player.name + "'s score : " + str(player.score))

    return render_template("quiz-sel.html", player=player)


@app.route('/log/<username>/<kana>', methods=["GET", "POST"])
def quiz(username, kana):
    """
    Quiz main page
    """
    selection = get_random_kana()
    guess = selection[0]
    score = 0

    if request.method == "POST":
        answer = request.form["answer"]
        check_answer(answer, guess, score)
        return render_template('quiz.html', user=username, guess=guess, kana=kana)

    return render_template('quiz.html', user=username, guess=guess, kana=kana)


@app.route('/leader-board')
def leader_board():
    """route to leaderboard with top 10 scores"""
    return render_template('leader-board.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=int(5000),
            debug=True)
