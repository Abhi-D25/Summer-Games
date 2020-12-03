from time import sleep
sudoku  = [
			[5,3,0,		0,7,0,		0,0,0],
			[6,0,0,		1,9,5,		0,0,0],
			[0,9,8,		0,0,0,		0,6,0],

			[8,0,0,		0,6,0,		0,0,3],
			[4,0,0,		8,0,3,		0,0,1],
			[7,0,0,		0,2,0,		0,0,6],

			[0,6,0,		0,0,0,		2,8,0],
			[0,0,0,		4,1,9,		0,0,5],
			[0,0,0,		0,8,0,		0,8,9]	
		]

def blank_space(brd):
	"""
	->finds ther blank spaces on the board which are marked as 0
	-> The parameter 'brd' takes a board (2-D List representation of a sudoku board)
	-> the function returns the position of a blank space in a tuple (x,y)
	"""

	for i in range(len(brd)): 		#length of the board is 9
		for j in range(len(brd)):
			if brd[i][j] == 0:
				return (i,j)

	return 0

def rules(brd, pos, num):

	''' This function takes 3 parameters: - the board, (brd)
										 - the positon of the blank space, (pos)
	 									 - the number being inserted (num)
	 	This function is used to check if the number assigned follows all the sudoku rules or not
	 	'''
	#Check the row

	for i in range(0, len(brd)):
		if brd[pos[0]][i] == num and pos[1] != i:
			return False

	#Check the column

	for i in range(0, len(brd)):
		if brd[i][pos[1]] == num and pos[0] != i:
			return False

	#Check the 3X3 box

	box_x = pos[1]//3
	box_y = pos[0]//3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x*3, box_x*3 + 3):
			if brd[i][j] == num and (i,j) != pos:
				return False
	return True

def solve(brd):
	#This function solves the whole sudoku board using the backtracking method(recursion)
	#The parameter taken is the board which should be solved
	#At the end of this function, the solved board is returned (TRUE)

	blank = blank_space(brd)
	#To check step by step uncomment the next 3 lines
	#print()
	#print()
	#display_board(brd)

	if blank:
		row, col = blank
	else:
		return True

	for i in range(1,10):
		if rules(brd, (row,col), i):
			brd[row][col] = i

			if solve(brd):
				return True

			brd[row][col] = 0

	return False

def display_board(brd):
	#This function prints the board by taking the parameter of the board that needs to be printed
	#It can be called to display the board before it is solved and after it is solved
	for i in range(len(brd)):
		#To break line after every line
		print()

		#To print the horizontal divisions on the board
		if i % 3 == 0 and i!=0:
			print(' - '*11)

		#For printing the verical divisions at the start of every column
		for j in range(len(brd)):
			if j % 3 == 0:
				print('|', end=" ")

			if j == 8:
				print(brd[i][j], "|", end=" ")
			else:
				print(str(brd[i][j]) + " ", end=" ")
	print()
	print()

print("------------------ The sudoku puzzle to be solved is: -------------------")
display_board(sudoku)
sleep(1)
solve(sudoku)
print("------------------ The solution to your sudoku puzzle is: -------------------")
display_board(sudoku)






