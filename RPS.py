#!/usr/bin/python

import sys, Players
from Players import Moves
from Players import PlayerFactory


def result(human, computer):
    print "You tried " + human + " and I tried " + computer
    if human == Moves.ROCK:
        if computer == "Lizard" or computer == "Scissors":
            print "You win!"
        elif computer == "Paper" or computer == "Spock":
            print "You lose!"
        else:
            print "You tie!"
    if human == Moves.PAPER:
        if computer == "Rock" or computer == "Spock":
            print "You win!"
        elif computer == "Scissors" or computer == "Lizard":
            print "You lose!"
        else:
            print "You tie!"
    if human == Moves.SCISSORS:
        if computer == "Paper" or computer == "Lizard":
            print "You win!"
        elif computer == "Rock" or computer == "Spock":
            print "You lose!"
        else:
            print "You tie!"
    if human == Moves.LIZARD:
        if computer == "Spock" or computer == "Paper":
            print "You win!"
        elif computer == "Scissors" or computer == "Rock":
            print "You lose!"
        else:
            print "You tie!"
    if human == Moves.SPOCK:
        if computer == "Rock" or computer == "Scissors":
            print "You win!"
        elif computer == "Paper" or computer == "Lizard":
            print "You lose!"
        else:
            print "You tie!"


def getMove(inputString):
    lowerInputString = inputString.lower()

    if lowerInputString == 's' or 'sci' in lowerInputString:
        return Moves.SCISSORS
    elif lowerInputString == 'r' or 'roc' in lowerInputString:
        return Moves.ROCK
    elif lowerInputString == 'p' or 'pap' in lowerInputString:
        return Moves.PAPER
    elif lowerInputString == 'l' or 'liz' in lowerInputString:
        return Moves.LIZARD
    elif lowerInputString == 'w' or 'spo' in lowerInputString:
        return Moves.SPOCK

    raise Exception("Invalid input from user.")


def checkArgs():
    validArgNum = len(sys.argv) == 3

    if not validArgNum:
        raise Exception("Arguments should be in the following format: [AI Difficulty] [Number Of Games To Play]")


if __name__ == "__main__":
    checkArgs()

    print "Hello!\n" \
		  "Welcome to our Rock-Paper-Scissor-Lizard-Spock Game!\n" \
		  "For those not familiar with how the game is played, I will explain it now.  R=Rock, P=Paper, S=Scissors, " \
          "L=Lizard, and W=Spock.\n" \
		  "S>P, P>R, R>L, L>W, W>S, S>L, L>P, P>W, W>R, R>S. For this trial, you will play 50 games of rock paper " \
          "scissors and our AI will attempt to beat you as much as possible.\n" \
		  "Good luck!\n"

    player = PlayerFactory.initPlayer(int(sys.argv[1]))
    maxNumGames = int(sys.argv[2])

    print "You selected player (" + player.getPlayerName() + ") and number of moves (%d)" % maxNumGames

    history = []
    numGames = 0
    while numGames < maxNumGames:
        AIMove = player.getNextMove(history)
        try:
            move = getMove(raw_input("\nEnter your move for trial %d:  " % numGames))
        except:
            print "Sorry, I didn't quite catch that. Please enter Rock | Paper | Scissors | Lizard | Spock."
        else:
			print move
			result(move, AIMove)
			history.append(move)
			numGames += 1

    print history
