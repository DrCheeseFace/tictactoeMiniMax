#tictactoe ai
import math

def printBoard(board):
	print("   0    1    2")
	row = 0
	for i in board:
		print(str(row)+str(i))
		row +=1

def humanMove(board):
	while True:
		printBoard(board)
		x = int(input("column: "))
		y = int(input("row: "))
		if board[y][x] != " ":
			print("Pick an empty slot")
		else:
			board[y][x] = "x"
			printBoard(board)
			return board

def checkStatus(board):
	for i in board:
		for j in i:
			if j ==" ":
				if winner(board) == "x" or winner(board) =="o":
					return winner(board)
				else:
					return "ongoing"
	else:
		if winner(board) == "x" or winner(board) =="o":
			return winner(board)
		else:
			return "draw"


def winner(board):
	for i in range(3):
		if board[0][i] == board[1][i] == board[2][i]:
			winner = board[0][i]
			return winner
			break
		if board[i][0] == board[i][1] == board[i][2]:
			winner = board[i][0]
			return winner
			break
		if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board [1][1] == board[2][0]:
			winner = board[1][1]
			return winner # i realize this "if" is run 3 times for no reason, i dont care                                                     
			break
	return None

def machineMove(board):
	bestScore = -math.inf
	for i in range (3):
		for j in range(3):
			if board[i][j] == " ":
				board[i][j] = "o"
				score = minimax(board,False)
				board[i][j] = " "
				if score > bestScore:
					bestScore = score
					bestMove = [i,j]

	board[bestMove[0]][bestMove[1]] = "o"
	return board

scores = {
  "x": -10,
  "o": 10,
  "draw": 0
}

def minimax(board,isMaximizing):
	check = checkStatus(board)
	
	if checkStatus(board) != "ongoing":
		return scores[check]	

	if isMaximizing:
		bestScore = -math.inf
		for i in range (3):
			for j in range(3):
				if board[i][j] == " ":
					board[i][j] = "o"
					score = minimax(board,False)
					board[i][j] = " "
					bestScore = max(score, bestScore)
					
		return bestScore
	else: #minimizing
		bestScore = math.inf
		for i in range (3):
			for j in range(3):
				if board[i][j] == " ":
					board[i][j] = "x"
					score = minimax(board,True)
					board[i][j] = " "
					bestScore = min(score, bestScore)
		return bestScore


humanToMove = True
board = [[" "," "," "],
		 [" "," "," "],
		 [" "," "," "]]


while checkStatus(board) == "ongoing":
	if humanToMove: #x
		board = humanMove(board)
		humanToMove = False
	else: #o
		board = machineMove(board)
		humanToMove = True
	
print(checkStatus(board))
		

