# Nan’Ki

## Overview

Nan’Ki is an online game that challenges your knowledge of Hiragana and Katakana.
It allows you to compete with other top players in both syllabaries.

### Game Rules

First the player chooses the syllabary (Hiragana or Katakana).
He is then asked to guess 20 random characters.
The player scores 1 point for each right answer while error costs 2 points.
He can then compare his final result with other players.
The game keeps a record of the 10 highest scores.

## How it works

It should allow several users to play simultaneously.  
A separate page for the leader-board with the 10 highest scores is accessible anytime without login.   
On landing page the player can login and view the top 3 scores.  
Once the player is logged in, the app prompts the player to choose a syllabary.  
The app selects randomly 20 characters from the chosen syllabary that will be displayed one by one to the player.  
During the challenge, for each right answer 1 point is added to the player’s score. The player can then move to the next guess with his score updated and the number of remaining guesses.  
When guessing wrong it displays the correct answer and removes 2 points. The player can move to the next guess.  
When the player has finished answering, he is taken to his final score with a copy of the leader-board.

## Features

### Features to add

- Leader-board, top 10 scores
- Syllabaries challenge

### Existing features

- Landing / login page

## Tech used

- [Python3](https://docs.python.org/3/)
- [Flask](http://flask.pocoo.org/docs/1.0/)
	- Python’s micoframework to build this web app faster
- [Bootstrap](http://getbootstrap.com/)
	- **Bootstrap v3.3.7** is used to quickly give the project a simple, responsive layout.

## Contributing

### Getting the code up and running

1. Firstly you will need to clone this repository by running
`git clone https://github.com/GarethS3/nanki.git`

2. Make sure you run the code in its own virtual environments by running from project direcory
`source venv/bin/activate`
then :
`which python`

3. To install dependencies you will need pip3
```
sudo apt install python3-pip
pip3 install -r requirements.txt
```
