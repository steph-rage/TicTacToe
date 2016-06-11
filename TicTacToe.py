A = [" ", " ", " "]			#Initialize the rows of the grid with blank spaces
B = [" ", " ", " "] 
C = [" ", " ", " "]
row_selector = {"A": A, "B": B, "C": C}			#Makes it easy to grab rows given user input
marks = []				#Initialize variables to be used
current_player = 0
counter = 0
done = False

def print_grid():
	print("%s | %s | %s" % (A[0], A[1], A[2]))
	print("----------")
	print("%s | %s | %s" % (B[0], B[1], B[2]))
	print("----------")
	print("%s | %s | %s" % (C[0], C[1], C[2]))
	print("\n")

def choose_marks():		#Ask player 1 to pick X or O and assign player 2 to the other
	marks.append(input("Player 1, please choose your mark: ").upper())
	if marks[0] == "X":
		marks.append("O")
	elif marks[0] == "O":
		marks.append("X")
	else:
		marks.pop()		#Delete player's mark if it is not X or O
		print("Please choose either X or O for your mark")
		choose_marks()
		
def check_win():
	for row in row_selector:		#Check for a win across
			if row_selector[row][0] == row_selector[row][1] == row_selector[row][2]:
				return row_selector[row][0]
	for col in range(3):		#Check for a win down
			if A[col] == B[col] == C[col]:
				return A[col]
	if A[0] == B[1] == C[2]:		#Check for a win diagonally
		return A[0]
	if A[2] == B[1] == C[0]:
		return A[2]
	else:
		return False
	
def next_turn(player):		#Ask the next player to choose a space 
	space = input("Player %d, please choose a space: " % (player + 1))
	space = list(space)
	if space[0].upper() not in ["A", "B", "C"] or space[1] not in ["1", "2", "3"] or len(space) != 2:	#Make sure the space is allowed
		print("That is not a valid space on our Tic Tac Toe board.")
		next_turn(player)
	else:
		row = space[0].upper()
		col = int(space[1]) - 1
		if row_selector[row][col] == " ":		#Place the player's mark in their space
			row_selector[row][col] = marks[player]
			print_grid()
		else:
			print("That space is already taken!")		#Unless the space is taken
			next_turn(player)
		

print_grid()
choose_marks()
print("Rows are A, B, C and columns are 1, 2, 3")
while done == False:			#Play the game!
	next_turn(current_player)
	if check_win() == "X":
		print("The X's win!")
		done = True
	elif check_win() == "O":		#Until somebody wins
		print("The O's win!")
		done = True
	elif counter == 8:			#Or the grid is full
		print("Nobody wins :-(")
		done = True
	else:				#Count the number of turns and switch to the next player
		counter += 1
		current_player = (current_player + 1)%2
