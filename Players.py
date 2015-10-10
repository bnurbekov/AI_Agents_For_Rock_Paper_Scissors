#!/usr/bin/python
#AI for RPSLW game.  Methods implimented include:

#0: constant Spock: always throws spock
#1: random: picks a purely random throw
#2: weighted random: weights each choice based on previous history, but still random
#3: average (MAP): checks the average move of the player, and beats it
#4: Bayes Average: combines the average move that beats a player, and uses it
#5: N rotation: determines the average rotation of the player, and counters it
#6: pattern detection: looks in the history for the longest string of the pattern detected, and attempts to beat the next move
#7: Bayes pattern detection: weights multiple patterns found and computes the best move
#8: category player: determines what category of person you are, and uses algorithms 1-7 to beat you

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
        elif (playerNum == 5):
            return Player5()
        elif (playerNum == 6):
            return Player6()
        elif (playerNum == 7):
            return Player7()
        elif (playerNum == 8):
            return Player8()
        else:
            return None

class Player:
    def getPlayerName(self):
        return "General Player"
        
#not used in all players, consider moving
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
        return "Constant Player"
        
    def getNextMove(self, history):
        return Moves.SPOCK

class Player1(Player):
    def getPlayerName(self):
        return "Random Player"

    def getNextMove(self, history):
        return Moves.getRandomMove()

class Player2(Player):
    def getPlayerName(self):
        return "Weighted Random"

    def getNextMove(self, history):
	rockScore    = 0
	paperScore   = 0
	scissorsScore = 0
	lizardScore  = 0
	spockScore   = 0
        for move_human_opponent_outcome in history:
		move = move_human_opponent_outcome[0]
		if move == Moves.ROCK:
			rockScore+=.5
			paperScore+=1
			spockScore+=1
		elif move == Moves.PAPER:
			paperScore+=.5
			scissorsScore+=1
			lizardScore+=1
		elif move == Moves.SCISSORS:
			scissorsScore+=.5
			rockScore+=1
			spockScore+=1
		elif move == Moves.LIZARD:
			lizardScore+=.5
			scissorsScore+=1
			rockScore+=1
		elif move == Moves.SPOCK:
			spockScore+=.5
			paperScore+=1
			lizardScore+=1
	nextMove = random.uniform(0,rockScore+paperScore+scissorsScore+lizardScore+spockScore)
	if nextMove <= rockScore:
		return Moves.ROCK
	nextMove-=rockScore
	if nextMove <= paperScore:
		return Moves.PAPER
	nextMove-=paperScore
	if nextMove <= scissorsScore:
		return Moves.SCISSORS
	nextMove-=scissorsScore
	if nextMove <= lizardScore:
		return Moves.LIZARD
	nextMove-=lizardScore
	if nextMove <= spockScore:
		return Moves.SPOCK
	else:
		print "ERROR"
		return

class Player3(Player):
    def getPlayerName(self):
        return "MLE/MAP"

    def getNextMove(self, history):
        rockScore    = 0
	paperScore   = 0
	scissorsScore = 0
	lizardScore  = 0
	spockScore   = 0
        for move_human_opponent_outcome in history:
		move = move_human_opponent_outcome[0]
		if move == Moves.ROCK:
			rockScore+=1
		elif move == Moves.PAPER:
			paperScore+=1
		elif move == Moves.SCISSORS:
			scissorsScore+=1
		elif move == Moves.LIZARD:
			lizardScore+=1
		elif move == Moves.SPOCK:
			spockScore+=1

	if rockScore is max(rockScore,paperScore,scissorsScore,lizardScore,spockScore):
		return Moves.PAPER
	elif paperScore is max(rockScore,paperScore,scissorsScore,lizardScore,spockScore):
		return Moves.SCISSORS
	elif scissorsScore is max(rockScore,paperScore,scissorsScore,lizardScore,spockScore):
		return Moves.SPOCK
	elif lizardScore is max(rockScore,paperScore,scissorsScore,lizardScore,spockScore):
		return Moves.ROCK
	elif spockScore is max(rockScore,paperScore,scissorsScore,lizardScore,spockScore):
		return Moves.LIZARD

class Player4(Player):
    def getPlayerName(self):
        return "Bayes Average"

    def getNextMove(self, history):
        return

class Player5(Player):
    def getPlayerName(self):
        return "N Rotation w/l"

    def getNextMove(self, history):
        return
    
class Player6(Player):
    def getPlayerName(self):
        return "Pattern Detection"

    def getNextMove(self, history):
        return
    
class Player7(Player):
    def getPlayerName(self):
        return "Bayes Pattern Detection"

    def getNextMove(self, history):
        return
    
class Player8(Player):
    def getPlayerName(self):
        return "Best Category"

    def getNextMove(self, history):
        return
