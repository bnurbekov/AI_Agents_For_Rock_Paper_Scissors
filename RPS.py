#!/usr/bin/python

import sys, getopt
from Players import Moves
from Players import PlayerFactory

def getOpts():
    optlist, args = getopt.getopt(sys.argv[1:],'', ['player1=', 'player2=', 'numberOfGames='])

    if len(optlist) != 3:
        raise Exception("Arguments should be in the following format: [Player1] [Player2] [Number Of Games To Play]")

    player1Name = optlist[0][1]

    if not player1Name.isdigit() and player1Name != 'h':
        raise Exception("Player 1 should either be a number of AI player or h (for human player).")

    player2Name = optlist[0][1]

    if not player2Name.isdigit() and player2Name != 'h':
        raise Exception("Player 1 should either be a number of AI player or h (for human player).")

    if not optlist[2][1].isdigit():
        raise Exception("Number of games should parameter should be a numeric value.")

    return [tuple[1] for tuple in optlist]


if __name__ == "__main__":
    args = getOpts()

    print "Hello!\n" \
          "Welcome to our Rock-Paper-Scissor-Lizard-Spock Game!\n" \
          "For those not familiar with how the game is played, I will explain it now.  R=Rock, P=Paper, S=Scissors, " \
          "L=Lizard, and W=Spock.\n" \
          "S>P, P>R, R>L, L>W, W>S, S>L, L>P, P>W, W>R, R>S. For this trial, you will play 50 games of rock paper " \
          "scissors and our AI will attempt to beat you as much as possible.\n" \
          "Good luck!\n"

    file = open('MainLog', 'w')
    player1 = PlayerFactory.initPlayer(args[0], file)
    player2 = PlayerFactory.initPlayer(args[1], file)
    maxNumGames = int(args[2])

    print "You selected (" + player1.getPlayerName() + ") player one, (" + player2.getPlayerName() + ") player two and number of moves (%d)" % maxNumGames

    player1History = ""
    player2History = ""
    scoreHistory = []
    player1Maximization = -1
    player2Maximization = 1

    while len(scoreHistory) < maxNumGames:
        move1 = player1.getNextMove(player1History, player2History, scoreHistory, player1Maximization)
        move2 = player2.getNextMove(player2History, player1History, scoreHistory, player2Maximization)
        result = Moves.compare(move2, move1)

        player1History += move1
        player2History += move2
        scoreHistory.append(result)

        file.write("Player1: " + move1 + "; Player2: " + move2 + "; Outcome: " + str(result) + "\n")

        player1.processResult(player1History, player2History, scoreHistory, player1Maximization)
        player2.processResult(player2History, player1History, scoreHistory, player2Maximization)

    player1.printStats(player1History, scoreHistory, player1Maximization)
    player2.printStats(player2History, scoreHistory, player2Maximization)

    file.close()