from tkinter import *

def button(frame):          
    b=Button(frame,padx=1,bg="white",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b



ai = 0
human = 1
turn = human



def copy(board):

	copy_board = []

	for i in board:
		copy_row = []
		for j in i:
			copy_row.append(j)
		copy_board.append(copy_row)
	
	return copy_board


def myBestMove(best_board):
	best_score = float('-inf')
	best_move = []; 
	width = len(best_board)
	
	for i in range(width):
		for j in range(width):
			if best_board[i][j] == " ":
				new_board = copy(best_board)
				new_board[i][j] = ai
				score = max_value(new_board)
				if score > best_score:
					best_score = score
					best_move = [i,j]

	print(best_board)
	return best_move



def max_value(board):
	print(board)
	if terminal_case(board,ai):
		print("Never came here")
		if win_case(board,ai):
			return 1
		elif draw_case(board):
			return 0
	val = float("-inf")
	
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == " ":
				new_board = copy(board)
				new_board[i][j] = ai
				val = max(val,min_value(new_board))

	return val



def min_value(board):
	if terminal_case(board,human):
		if win_case(board,human):
			return -1
		elif draw_case(board):
			return 0

	val = float("inf")
	
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == " ":
				new_board = copy(board)
				new_board[i][j] = human
				val = min(val,max_value(new_board))

	return val;


def terminal_case(board,plyaer):
	return win_case(board,plyaer) or draw_case(board)



def win_case(board, player):

	if board[0][0] == player and board[0][1] == player and board[0][2] == player:
		return True

	elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
		return True

	elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
		return True
	
	elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
		return True

	elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
		return True

	elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
		return True

	elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
		return True

	elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
		return True

	return False


def click(row,col,turn):
	a = "X"
	b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
	my_board[row][col] = human
	print(my_board)
	val = terminal_case(my_board,human)
	
	if val:
		print(a +" won")
	else:	
		a = "O"
		new_board = list(my_board)
		ai_turn = myBestMove(new_board)
		print(ai_turn)
		my_board[ai_turn[0]][ai_turn[1]] = ai
		b[ai_turn[0]][ai_turn[1]].config(text=a,state=DISABLED,disabledforeground=colour[a])



def draw_case(board):

	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == " ":
				return False


	return True

			



my_board = [
				[" "," "," "],
				[" "," "," "],
				[" "," "," "]

			]
root = Tk()
root.title("Tic-Tac-Toe")
colour={'O':"red",'X':"green"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j,turn=turn:click(row,col,turn))
                b[i][j].grid(row=i,column=j)


root.mainloop()
