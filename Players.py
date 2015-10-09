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

class Player0:
    def getPlayerName(self):
        return "Random Player"

    def getNextMove(self, history):
        return random.choice(Moves.getAllMoves())

class Player1:
    def getNextMove(self, history):
        return

class Player2:
    def getNextMove(self, history):
        return

class Player3:
    def getNextMove(self, history):
        return

class Player4:
    def getNextMove(self, history):
        return
