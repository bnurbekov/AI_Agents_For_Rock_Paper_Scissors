#!/usr/bin/python

#CHANGE ME, ADD DIFFERENT TYPES OF AI AND DESCRIBE THEM!
def getNextAIMove(History):
	return "Rock"

def result(human, computer):
	print "You tried " + human + " and I tried " + computer
	if human == "Rock":
		if computer == "Lizard" or computer == "Scissors":
			print "You win!"
		elif computer == "Paper" or computer == "Spock":
			print "You lose!"
		else:
			print "You tie!"
	if human == "Paper":
		if computer == "Rock" or computer == "Spock":
			print "You win!"
		elif computer == "Scissors" or computer == "Lizard":
			print "You lose!"
		else:
			print "You tie!"
	if human == "Scissors":
		if computer == "Paper" or computer == "Lizard":
			print "You win!"
		elif computer == "Rock" or computer == "Spock":
			print "You lose!"
		else:
			print "You tie!"
	if human == "Lizard":
		if computer == "Spock" or computer == "Paper":
			print "You win!"
		elif computer == "Scissors" or computer == "Rock":
			print "You lose!"
		else:
			print "You tie!"
	if human == "Spock":
		if computer == "Rock" or computer == "Scissors":
			print "You win!"
		elif computer == "Paper" or computer == "Lizard":
			print "You lose!"
		else:
			print "You tie!"

def getMove(inputString):
	if inputString == 'S' or 'Sci' in inputString or inputString == 's' or 'sci' in inputString:
		return "Scissors"
	elif inputString == 'R' or 'Roc' in inputString or inputString == 'r' or 'roc' in inputString:
		return "Rock"
	elif inputString == 'P' or 'Pap' in inputString or inputString == 'p' or 'pap' in inputString:
		return "Paper"
	elif inputString == 'L' or 'Liz' in inputString or inputString == 'l' or 'liz' in inputString:
		return "Lizard"
	elif inputString == 'W' or 'Spo' in inputString or inputString == 'w' or 'spo' in inputString:
		return "Spock"
	else:
		return "Error"

if __name__ == "__main__":
	print "\nHello! Welcome to our Rock-Paper-Scissor-Lizard-Spock Game! For those not familiar with how the game is played, I will explain it now.  R=Rock, P=Paper, S=Scissors, L=Lizard, and W=Spock. S>P, P>R, R>L, L>W, W>S, S>L, L>P, P>W, W>R, R>S. For this trial, you will play 50 games of rock paper scissors and our AI will attempt to beat you as much as possible. Good luck!"
	numGames = 0
	History = []
	while numGames <50:
		AIMove = getNextAIMove(History)
		move = getMove(raw_input("\nEnter your move for trial %d:  "%numGames))
		if move is not 'Error':
			result(move, AIMove)
			History.append(move)
			numGames+=1
		else:
			print "Sorry, I didn't quite catch that"
	print History
