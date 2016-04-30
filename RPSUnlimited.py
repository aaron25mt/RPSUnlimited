from enum import Enum
from random import randrange

FILENAME = "moves.txt"

class Result(Enum):
	lose = -1
	tie = 0
	win = 1

def loadMoves(filename):
	try:
		with open(filename, "r") as fileObj:
			moves = [line.strip().split(',') for line in fileObj]
	except IOError:
		print("{} is not a valid file or not in the current working directory".format(FILENAME))
		exit(-1)
	return moves

def createGameName(moves):
	gameName = ""
	for move in moves:
		gameName += move[0]
	return gameName

def printChoices(moves):
	for choiceIndex in range(len(moves)):
		print("({}) {}".format((choiceIndex + 1), moves[choiceIndex][0]))

def doesXBeatY(moves, player1, player2):
	if(player1 == player2):
		return Result.tie
	if(player2 in moves[1:]):
		return Result.win
	else:
		return Result.lose

def main():
	score = 0
	moves = loadMoves(FILENAME)
	print("Welcome to {}!".format(createGameName(moves)))
	while True:
		print("")
		printChoices(moves)
		while True:
			try:
				choice = int(input("Please make a choice: "))
			except ValueError:
				print("Choice must be an integer.")
				continue
			else:
				if(choice < 1 or choice > len(moves)):
					print("Choice must be in between 1 - {}.".format(len(moves)))
					continue
				else:
					break
		player1 = moves[choice - 1][0]
		computer = moves[randrange(0, len(moves) - 1)][0]
		print("\n{} vs. {}...".format(player1, computer))
		result = doesXBeatY(moves[choice - 1], player1, computer)
		if(result == Result.win):
			score += Result.win.value
			print("{} wins!".format(player1))
		elif(result == Result.lose):
			score += Result.lose.value
			print("{} wins!".format(computer))
		else:
			score += Result.tie.value
			print("Tie.")
		print("\nYour score is {}!".format(score))
		playAgain = input("Do you want to play again? (Y/N) ").upper()
		if(playAgain == "N"):
			break

main()