#!/usr/bin/python

import random
from collections import defaultdict

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
    def compare(move1, move2):
        """
        Returns 1 if move1 beats move2
        Returns 0 if move1 is equal to move2 (tie)
        Returns -1 if move2 beats move1
        """

        if move1 == Moves.ROCK:
            if move2 == Moves.LIZARD or move2 == Moves.SCISSORS:
                return 1
            elif move2 == Moves.PAPER or move2 == Moves.SPOCK:
                return -1
            else:
                return 0
        elif move1 == Moves.PAPER:
            if move2 == Moves.ROCK or move2 == Moves.SPOCK:
                return 1
            elif move2 == Moves.SCISSORS or move2 == Moves.LIZARD:
                return -1
            else:
                return 0
        elif move1 == Moves.SCISSORS:
            if move2 == Moves.PAPER or move2 == Moves.LIZARD:
                return 1
            elif move2 == Moves.ROCK or move2 == Moves.SPOCK:
                return -1
            else:
                return 0
        elif move1 == Moves.LIZARD:
            if move2 == Moves.SPOCK or move2 == Moves.PAPER:
                return 1
            elif move2 == Moves.SCISSORS or move2 == Moves.ROCK:
                return -1
            else:
                return 0
        else: #Moves.SPOCK
            if move2 == Moves.ROCK or move2 == Moves.SCISSORS:
                return 1
            elif move2 == Moves.PAPER or move2 == Moves.LIZARD:
                return -1
            else:
                return 0

    @staticmethod
    def getRandomMove():
        return random.choice(Moves.getAllMoves())

    @staticmethod
    def getMovesThatCounter(move):
        counterMoves = []

        if move == Moves.ROCK:
            counterMoves.append(Moves.PAPER)
            counterMoves.append(Moves.SPOCK)
        elif move == Moves.PAPER:
            counterMoves.append(Moves.SCISSORS)
            counterMoves.append(Moves.LIZARD)
        elif move == Moves.SCISSORS:
            counterMoves.append(Moves.ROCK)
            counterMoves.append(Moves.SPOCK)
        elif move == Moves.LIZARD:
            counterMoves.append(Moves.SCISSORS)
            counterMoves.append(Moves.ROCK)
        else:
            counterMoves.append(Moves.PAPER)
            counterMoves.append(Moves.LIZARD)

        return counterMoves

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

    def getLeastUsedMoves(self, history):
        moveCountDict = dict()

        for move in Moves.getAllMoves():
            moveCountDict[move] = 0

        for move in history:
            moveCountDict[move] += 1

        leastUsedMoves = []
        smallestCount = 1000000
        for key, value in moveCountDict.iteritems():
            if smallestCount > value:
                smallestCount = value
                leastUsedMoves.append(key)
            elif smallestCount == value:
                leastUsedMoves.append(key)

        return  leastUsedMoves

    def getNextMove(self, history):
        return "Rock"

class Player0(Player):
    def getPlayerName(self):
        return "Random Player"

    def getNextMove(self, history):
        return Moves.getRandomMove()

class Player1(Player):
    def getPlayerName(self):
        return "Least used move beating Player"

    def getNextMove(self, history):
        moveHistory = [outcome[0] for outcome in history]

        if len(history) <= 0:
            return Moves.getRandomMove()

        leastUsedMove = random.choice(self.getLeastUsedMoves(moveHistory))
        moveBeatingLeastUsedMove = random.choice(Moves.getMovesThatCounter(leastUsedMove))

        return moveBeatingLeastUsedMove

class Player2(Player):
    def getPlayerName(self):
        return "Pattern matching Player"

    def getNextMove(self, history):
        return

class Player3(Player):
    def getPlayerName(self):
        return "Advanced versatile Player"

    def getNextMove(self, history):
        return

class Player4(Player):
    def getPlayerName(self):
        return "Advanced group matching Player"

    def getNextMove(self, history):
        return
