#Started on 2/20/2020 at 3:04 pm. 
#This program was made using the backtrackning algorithm adapted from TechWithTim.
import random

numberArray = [
			  [random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, random.randint(1, 9), 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, random.randint(1, 9), 0, 0],
			  [0, random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, random.randint(1, 9), 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, random.randint(1, 9), 0],
			  [0, 0, random.randint(1, 9), 0, 0, 0, 0, 0, 0],
			  [0, 0, 0, 0, 0, random.randint(1, 9), 0, 0, 0],
			  [0, 0, 0, 0, 0, 0, 0, 0, random.randint(1, 9)]
		      ]

# Define an array of the coordinates of each block, so it is more convenient to cycle through.
cellCoordinates1, cellCoordinates2, cellCoordinates3, cellCoordinates4, cellCoordinates5, cellCoordinates6, cellCoordinates7,  cellCoordinates8, cellCoordinates9 = [[0,0], [1,0], [2,0], [0,1], [1,1], [2,1], [0,2], [1,2], [2,2]], [[0,3], [1,3], [2,3], [0,4], [1,4], [2,4], [0,5], [1,5], [2,5]], [[0,6], [1,6], [2,6], [0,7], [1,7], [2,7], [0,8], [1,8], [2,8]], [[3,0], [4,0], [5,0], [3,1], [4,1], [5,1], [3,2], [4,2], [5,2]], [[3,3], [4,3], [5,3], [3,4], [4,4], [5,4], [3,5], [4,5], [5,5]], [[3,6], [4,6], [5,6], [3,7], [4,7], [5,7], [3,8], [4,8], [5,8]], [[6,0], [7,0], [8,0], [6,1], [7,1], [8,1], [6,2], [7,2], [8,2]], [[6,3], [7,3], [8,3], [6,4], [7,4], [8,4], [6,5], [7,5], [8,5]], [[6,6], [7,6], [8,6], [6,7], [7,7], [8,7], [6,8], [7,8], [8,8]]
blockPositions = [cellCoordinates1, cellCoordinates2, cellCoordinates3, cellCoordinates4, cellCoordinates5, cellCoordinates6, cellCoordinates7, cellCoordinates8, cellCoordinates9]

# Return which block this cell is in based on the coordinates (starting from the top left).
def getBlock(columnPosition, rowPosition): 
	if columnPosition >= 0 and columnPosition <= 2:
		if rowPosition >= 0 and rowPosition <= 2:
			return 1
		elif rowPosition >= 3 and rowPosition <= 5:
			return 4
		elif rowPosition >= 6 and rowPosition <= 8:
			return 7
	elif columnPosition >= 3 and columnPosition <= 5:
		if rowPosition >= 0 and rowPosition <= 2:
			return 2
		elif rowPosition >= 3 and rowPosition <= 5:
			return 5
		elif rowPosition >= 6 and rowPosition <= 8:
			return 8
	elif columnPosition >= 6 and columnPosition <= 8:
		if rowPosition >= 0 and rowPosition <= 2:
			return 3
		elif rowPosition >= 3 and rowPosition <= 5:
			return 6
		elif rowPosition >= 6 and rowPosition <= 8:
			return 9


# Return which cell inside of the block this is in based on the coordinates (starting from the top left).
def getBlockIndex(columnPosition, rowPosition):
	for block in range(9):
		for piece in range(9):
			if columnPosition == blockPositions[block][piece][1] and rowPosition == blockPositions[block][piece][0]:
				return piece


# Determine what values are not taken in the row.
def testRow(columnPosition, rowPosition, arrayToTest):
	colavailableList = [1,2,3,4,5,6,7,8,9]
	# Remove all values that cannot be used by changing them to zero.
	for i in range(9):
		if arrayToTest[rowPosition][i] > 0:
			colavailableList[arrayToTest[rowPosition][i]-1] = 0

	# Filter out the unnecessary zeros.
	newList = list(filter(lambda x: (x != 0), colavailableList))
	return newList


# Determine what values are not taken in the column.
def testColumn(columnPosition, rowPosition, arrayToTest):
	rowavailableList = [1,2,3,4,5,6,7,8,9]
	# Remove all values that cannot be used by changing them to zero.
	for i in range(9):
		if arrayToTest[i][columnPosition] > 0:
		 	rowavailableList[arrayToTest[i][columnPosition]-1] = 0

	# Filter out the unnecessary zeros.
	newList = list(filter(lambda x: (x != 0), rowavailableList))
	return newList


# Verify the 3x3 group of 1-9.
def testBlock(columnPosition, rowPosition, arrayToTest):
	thisBlock = getBlock(columnPosition, rowPosition)
	availableList = [1,2,3,4,5,6,7,8,9]

	for i in range(9):
		thisNoNo = arrayToTest[blockPositions[thisBlock-1][i][0]][blockPositions[thisBlock-1][i][1]]
		if thisNoNo > 0:
			availableList[thisNoNo - 1] = 0

	newList = list(filter(lambda x: (x != 0), availableList))   # Filter out every zero in the list.

	return newList
	

# Find the next zero in the array, starting from the top left corner.
def findEmptySpot(array):
	for y in range(9):
		for x in range(9):
			if array[y][x] == 0:
				return (y, x)

	return None


# Using backtracking and recursion, this will produce a sudoku grid.
def solveBoard(boardToSolve):
	findZero = findEmptySpot(boardToSolve)
	if not findZero:
		return True
	else:
		rowPosition, columnPosition = findZero # If the board has no zeros, determine the value for the next cell closest to the top left.

	colAvailable = testColumn(columnPosition, rowPosition, boardToSolve)
	rowAvailable = testRow(columnPosition, rowPosition, boardToSolve)
	blockAvailable = testBlock(columnPosition, rowPosition, boardToSolve)

	numbersPossible = [1,2,3,4,5,6,7,8,9]
	random.shuffle(numbersPossible)
	
	for value in range(9):
		if (numbersPossible[value] in rowAvailable) and (numbersPossible[value] in blockAvailable) and (numbersPossible[value] in colAvailable):
			boardToSolve[rowPosition][columnPosition] = numbersPossible[value]
			
			if solveBoard(boardToSolve):
				return True
							
			boardToSolve[rowPosition][columnPosition] = 0

	return False


# Go through the entire puzzle array to count the zeros
def countTheZeros(array):
	localZeroCount = 0
	for rowPos in range(9):
		for colPos in range(9):
			if array[rowPos][colPos] == 0:
				localZeroCount+=1
	return localZeroCount


# Randomnly place zeros
def minimizeBoard(array):
	desiredZeroAmount = 50
	while countTheZeros(array) < desiredZeroAmount:
	 # This will stop when the desired amount of zeros have been placed.
		rowPosition = random.randint(0,8)
		columnPosition = random.randint(0,8)
		# Make sure a zero is not already there
		while array[rowPosition][columnPosition] == 0:
			rowPosition = random.randint(0,8)
			columnPosition = random.randint(0,8)

		if array[rowPosition][columnPosition] != 0:
			array[rowPosition][columnPosition] = 0

	
# Reuable function that will reset the array and generate a nwe board.
def generatePuzzle(array):
	solveBoard(array)
	minimizeBoard(array)
	return array


numberArray = [[random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, random.randint(1, 9), 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, random.randint(1, 9), 0 ,0],[0, random.randint(1, 9), 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, random.randint(1, 9), 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, random.randint(1, 9) ,0],[0, 0, random.randint(1, 9), 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, random.randint(1, 9), 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, 0 , random.randint(1, 9)]]
generatePuzzle(numberArray)