def solve(board):
	loc = findNext(board)
	if loc == None: 
		if isSolved(board):
			for r in board:
				print(r)
			return True
		else:
			return False
	else:
		row = loc[0]
		col = loc[1]
		
		options = list(range(1, 10))

		solved = False
		while (len(options) > 0 and not solved):
			board[row][col] = options.pop(0)
			
			if broken(board, row, col):
				board[row][col] = 0
				continue

			solved = solve(board)

		return solved

def broken(board, row, column):
	choice = board[row][column]

	for c in range(9):
		if board[row][c] == choice and c != column:
			return True
	
	for r in range(9):
		if board[r][column] == choice and r != row:
			return True
	
	r = 0
	if row > 2: r = 3
	if row > 5: r = 6
	c = 0
	if column > 2: c = 3
	if column > 5: c = 6

	for k in range(3):
		for i in range(3):
			if board[r][c] == choice and (r, c) != (row, column):
				return True
			c += 1
		c -= 3
		r += 1

	return False


def isSolved(board):
	for row in board:
		for k in range(1, 10):
			if k not in row:
				return False

	column = []
	for col in range(9):
		for row in range(len(board)):
			column.append(board[row][col])
		
		for k in range(1, 10):
			if k not in column:
				return False
		column.clear()
	
	box = []
	for n in range(3):
		offset = n*3

		for row in range(3):
			row += offset
			for col in range(3):
				col += offset
				box.append(board[row][col])

		for k in range(1, 10):
			if k not in box:
				return False
		box.clear()
	return True
		
def findNext(board):
	for r in range(9):
		for c in range(9):
			if board[r][c] == 0:
				return (r, c)
	return None

board = [
	[0, 0, 0, 0, 2, 6, 8, 0, 0],
	[7, 0, 0, 0, 5, 1, 0, 0, 9],
	[8, 0, 0, 4, 0, 0, 0, 0, 0],
	[0, 5, 0, 1, 9, 0, 0, 0, 3],
	[0, 0, 3, 0, 6, 0, 4, 2, 0],
	[0, 0, 7, 0, 4, 0, 0, 1, 0],
	[0, 7, 9, 0, 0, 0, 0, 0, 0],
	[1, 6, 0, 0, 0, 0, 0, 0, 8],
	[5, 0, 0, 0, 0, 9, 0, 6, 0]
	]

print(solve(board))