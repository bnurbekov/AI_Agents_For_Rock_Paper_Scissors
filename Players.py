#!/usr/bin/python

import random

class Moves:
    SCISSORS = "Scissors"
    ROCK = "Rock"
    PAPER = "Paper"
    LIZARD = "Lizard"
    SPOCK = "Spock"

    @staticmethod
    def getAllMoves():
        return [Moves.SCISSORS, Moves.ROCK, Moves.PAPER, Moves.LIZARD, Moves.SPOCK]

    @staticmethod
    def parseMove(inputString):
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

        raise Exception("Unrecognized move string was provided.")

    @staticmethod
    def result(human, computer):
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

    @staticmethod
    def getRandomMove():
        return random.choice(Moves.getAllMoves())


    @staticmethod
    def getMovesThatCounter(move):
        return


class PlayerFactory:
    @staticmethod
    def initPlayer(playerNum):
        if (playerNum == 0):
            return Player0()
        elif (playerNum == 1):
            return Player1()
        elif (playerNum == 2):
            return Player2()
        elif (playerNum == 3):
            return Player3()
        elif (playerNum == 4):
            return Player4()
        else:
            return None

class Player:
    def getPlayerName(self):
        return "General Player"

    def getNextMove(self, history):
        return "Rock"

class Player0(Player):
    def getPlayerName(self):
        return "Random Player"

    def getNextMove(self, history):
        return Moves.getRandomMove()

class Player1(Player):
    def getNextMove(self, history):
        return

class Player2(Player):
    def getNextMove(self, history):
        return

class Player3(Player):
    def getNextMove(self, history):
        return

class Player4(Player):
    def getNextMove(self, history):
        return
