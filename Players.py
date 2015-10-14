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

import random, operator, itertools

class Moves:
    SCISSORS = "S"
    ROCK = "R"
    PAPER = "P"
    LIZARD = "L"
    SPOCK = "W"

    combinations = [''.join(i) for i in itertools.product(['R', 'P', 'S', 'L', 'W'], repeat = 2)]

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
    def convertToFullName(move):
        if move == Moves.PAPER:
            return "Paper"
        elif move == Moves.SCISSORS:
            return "Scissors"
        elif move == Moves.ROCK:
            return "Rock"
        elif move == Moves.SPOCK:
            return "Spock"
        else:
            return "Lizard"

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
        elif move1 == Moves.SPOCK:
            if move2 == Moves.ROCK or move2 == Moves.SCISSORS:
                return 1
            elif move2 == Moves.PAPER or move2 == Moves.LIZARD:
                return -1
            else:
                return 0

        else:
            raise Exception("Unknown move.")

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
    def initPlayer(playerNum, genericLog):
        if (playerNum == '0'):
            return Player0(genericLog)
        elif (playerNum == '1'):
            return Player1(genericLog)
        elif (playerNum == '2'):
            return Player2(genericLog)
        elif (playerNum == '3'):
            return Player3(genericLog)
        elif (playerNum == '4'):
            return Player4(genericLog)
        elif (playerNum == '5'):
            return Player5(genericLog)
        elif (playerNum == '6'):
            return Player6(genericLog)
        elif (playerNum == '7'):
            return Player7(genericLog)
        elif (playerNum == '8'):
            return Player8(genericLog)
        elif (playerNum == 'h'):
            return PlayerHuman(genericLog)
        else:
            return None

class Player:
    def __init__(self, genericLog):
        self.genericLog = genericLog
        self.ownLog = open(self.getPlayerName(), 'w')
        self.ownLog.write("Player: " + self.getPlayerName() + "\n")

    def processResult(self, myHistory, theirHistory, scoreHistory, maximization):
        return

    def getPlayerName(self):
        return "General Player"

    def printStats(self, myHistory, scoreHistory, maximization):
        ties = sum([1 for outcome in scoreHistory if outcome == 0])
        wins = sum([1 for outcome in scoreHistory if outcome == maximization])
        losses = sum([1 for outcome in scoreHistory if outcome == -maximization])

        self.ownLog.write("Ties: " + str(ties) + "\n")
        self.ownLog.write("Wins: " + str(wins) + "\n")
        self.ownLog.write("Losses: " + str(losses) + "\n")


    def calculateScoresForMovesWithLosesSubtracted(self, myHistory, scoreHistory, maximization):
        moveDict = {}
        for move in Moves.getAllMoves():
            #initialize as one to scale the weights properly
            moveDict[move] = 1

        for i in range(len(scoreHistory)):
            if scoreHistory[i] == maximization:
                moveDict[myHistory[i]] += 1
            elif scoreHistory[i] == 0:
                moveDict[myHistory[i]] += 0.5
            else:
                #decrement the count if it is larger than 0 on lose
                if moveDict[myHistory[i]] > 1:
                    moveDict[myHistory[i]] -= 1

        return moveDict

    def calculateScoresForMoves(self, myHistory, scoreHistory, maximization):
        moveDict = {}
        for move in Moves.getAllMoves():
            #initialize as one to scale the weights properly
            moveDict[move] = 0

        for i in range(len(scoreHistory)):
            if scoreHistory[i] == maximization:
                moveDict[myHistory[i]] += 1
            elif scoreHistory[i] == 0:
                moveDict[myHistory[i]] += 0.5

        return moveDict

    # Random weighted choice from dict
    def weighted_choice(self, itemDict):
        total = sum(weight for move, weight in itemDict.iteritems())
        r = random.uniform(0, total)
        upto = 0

        keyValuePairs = list(itemDict.iteritems())
        random.shuffle(keyValuePairs)

        for move, weight in keyValuePairs:
            if upto + weight >= r:
                return move

            upto += weight

        return None

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        return "Rock"

class Player0(Player):
    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def getPlayerName(self):
        return "Constant Player"
        
    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        return Moves.SPOCK

class Player1(Player):
    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def getPlayerName(self):
        return "Random Player"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        return Moves.getRandomMove()

class Player2(Player):
    """More likely to pick successful in the past moves."""

    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def getPlayerName(self):
        return "Weighted Random"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        moveDict = self.calculateScoresForMovesWithLosesSubtracted(myHistory, scoreHistory, maximization)
        return self.weighted_choice(moveDict)

class Player3(Player):
    """Counters Player2."""

    def __init__(self, genericLog):
        Player.__init__(self, genericLog)
        self.opponentPlayer = Player2(genericLog)

    def getPlayerName(self):
        return "MLE_MAP"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        return random.choice(Moves.getMovesThatCounter(self.opponentPlayer.getNextMove(theirHistory, myHistory, scoreHistory, -maximization)))

class Player4(Player):
    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def getPlayerName(self):
        return "Bayes Average"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        moveDict = self.calculateScoresForMoves(theirHistory, scoreHistory, -maximization)
        moveUtilityDict = {}

        for move in Moves.getAllMoves():
            moveUtilityDict[move] = 0

        for move in moveUtilityDict:
            for m in moveDict:
                if (move == m):
                    moveUtilityDict[move] += 0.1*moveDict[m]
                elif (move not in Moves.getMovesThatCounter(m)):
                    moveUtilityDict[move] -= moveDict[m]
                else:
                    moveUtilityDict[move] += moveDict[m]

        minScore = min(moveUtilityDict.itervalues())

        if minScore < 0:
            for move in moveUtilityDict.iterkeys():
                moveUtilityDict[move] += -minScore

        return self.weighted_choice(moveUtilityDict)

class Player5(Player):
    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def getPlayerName(self):
        return "Rotation"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        """Tries to counter the rotation after opponent's loss."""

        #If it's the first move or the opponent has won previously, then select random move
        if (len(myHistory) <= 0 or scoreHistory[-1] != maximization):
            return Moves.getRandomMove()

        return random.choice(Moves.getMovesThatCounter(random.choice(Moves.getMovesThatCounter(myHistory[-1]))))

    
class Player6(Player):
    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

        self.combine = {Moves.combinations[i] : chr(ord('a') + i) for i in range(0, len(Moves.combinations))}
        self.split = {chr(ord('a') + i) : Moves.combinations[i] for i in range(0, len(Moves.combinations))}

    def getPlayerName(self):
        return "Pattern Detection"

    def convertHistoriesIntoDna(self, myHistory, theirHistory):
        dna = ""

        if myHistory == "":
            return dna

        for i in range(0, len(myHistory)):
            dna += self.combine[myHistory[i]+theirHistory[i]]

        return dna

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        dna = self.convertHistoriesIntoDna(myHistory, theirHistory)

        if dna == "":
            return Moves.getRandomMove()

        patternDict = {}

        for patternLength in range(min(5, len(dna)-1), 0, -1):
            pattern = dna[-patternLength:]
            searchStart = 0

            while True:
                patternIndex = dna.find(pattern, searchStart, -1)

                if patternIndex == -1:
                    break

                searchStart = patternIndex + 1

                nextMoveAfterPattern = dna[patternIndex + patternLength]
                expectedOpponentMove = self.split[nextMoveAfterPattern][1]
                if pattern in patternDict.iterkeys():
                    patternDict[pattern].append(expectedOpponentMove)
                else:
                    patternDict[pattern] = [expectedOpponentMove]

        if len(patternDict)>1:
            patternUtilDict = {}

            #weighted choice of a pattern based on length and frequency
            for pattern, listOfNextMoves in patternDict.iteritems():
                patternUtilDict[pattern] = len(listOfNextMoves)/4.0 + len(pattern)/4.0*3

            selectedPattern = self.weighted_choice(patternUtilDict)
        elif patternDict:
            selectedPattern = patternDict.keys()[0]
        else:
            return Moves.getRandomMove()

        #weighted choice of next move of an opponent
        opponentMoves = patternDict[selectedPattern]
        nextOpponentMove = self.weighted_choice(dict( [(i, opponentMoves.count(i)) for i in set(opponentMoves)]))

        #weighted choice of move that would counter the next move of an opponent
        return random.choice(Moves.getMovesThatCounter(nextOpponentMove))
    
class Player7(Player):
    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

        self.strategiesUsed = []
        self.strategyScores = []
        self.strategies = []
        for i in range(0, 7):
            self.strategies.append(PlayerFactory.initPlayer(str(i), genericLog))
            self.strategyScores.append(0)
            self.strategiesUsed.append(0)

    def printStats(self, myHistory, scoreHistory, maximization):
        Player.printStats(self, myHistory, scoreHistory, maximization)
        self.ownLog.write("Strategies used:\n" + '\n'.join([str(i)+" " + str(self.strategiesUsed[i]) for i in range(len(self.strategiesUsed))]) + "\n")

    def getPlayerName(self):
        return "Best Category"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        """Implements Random Drop Switch strategy for player selection."""

        if len(scoreHistory) > 0:
             if scoreHistory[-1] == maximization:
                 self.strategyScores[self.lastStrategyIndex] += 1
             elif scoreHistory[-1] == -maximization:
                 if random.randint(0, 1):
                     self.strategyScores[self.lastStrategyIndex] = 0

        self.ownLog.write("Strategy scores:\n" + '\n'.join([str(i)+" " + str(self.strategyScores[i]) for i in range(len(self.strategyScores))]) + "\n")

        #find the position of the maximum element in array
        maxScore = max(enumerate(self.strategyScores), key=(lambda x: x[1]))[1]
        maxScoringStrategies = [i for i in range(len(self.strategyScores)) if self.strategyScores[i] == maxScore]
        self.lastStrategyIndex = random.choice(maxScoringStrategies)
        self.strategiesUsed[self.lastStrategyIndex] += 1

        self.ownLog.write("Strategy selected: " + str(self.lastStrategyIndex) + "\n")

        return self.strategies[self.lastStrategyIndex].getNextMove(myHistory, theirHistory, scoreHistory, maximization)

class Player8(Player):
    """Reinforcement learning player"""

    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def printStats(self, myHistory, scoreHistory, maximization):
        Player.printStats(self, myHistory, scoreHistory, maximization)
        return

    def getPlayerName(self):
        return "Bonus Reinforcement Learning"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        return


class PlayerHuman(Player):
    """Reinforcement learning player"""

    def __init__(self, genericLog):
        Player.__init__(self, genericLog)

    def printStats(self, myHistory, scoreHistory, maximization):
        Player.printStats(self, myHistory, scoreHistory, maximization)

        scoreSum = sum([outcome for outcome in scoreHistory])

        if scoreSum >= 1:
            print "Overall you win!"
        elif scoreSum <= -1:
            print "Overall you lose!"
        else:
            print "Overall you tie!"

    def getPlayerName(self):
        return "Human"

    def getNextMove(self, myHistory, theirHistory, scoreHistory, maximization):
        playerMadeValidMove = False
        move = None

        while not playerMadeValidMove:
            try:
                userInput = raw_input("\nEnter your move for trial %d:  " % (len(myHistory) + 1))
                move = Moves.parseMove(userInput)
            except Exception, e:
                print "Sorry, I didn't quite catch that. Please enter Rock | Paper | Scissors | Lizard | Spock. Error: " + str(e)
            else:
                playerMadeValidMove = True

        return move

    def processResult(self, myHistory, theirHistory, scoreHistory, maximization):
        print "You tried (" + Moves.convertToFullName(myHistory[-1]) + ") and I tried (" + Moves.convertToFullName(theirHistory[-1]) + ")"

        if scoreHistory[-1] is maximization:
            print "You win!"
        elif scoreHistory[-1] is 0:
            print "You tie!"
        else:
            print "You lose!"
        
