#Started on 2/20/2020 at 3:04 pm. 
#This program was made using the backtrackning algorithm adapted from TechWithTim.
import pygame # If you have python installed, type + run "pip install pygame" in cmd to install pygame.
import time, sys, random

# Initialize the program.
pygame.init()

# Define initial variable values.
WIN_WIDTH = 400
WIN_HEIGHT = 400

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

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
backgroundColour = (255, 255, 255)
screen.fill(backgroundColour)

pygame.display.set_caption('Sudoku')

clock = pygame.time.Clock()

cellCoordinates1, cellCoordinates2, cellCoordinates3, cellCoordinates4, cellCoordinates5, cellCoordinates6, cellCoordinates7,  cellCoordinates8, cellCoordinates9 = [[0,0], [1,0], [2,0], [0,1], [1,1], [2,1], [0,2], [1,2], [2,2]], [[0,3], [1,3], [2,3], [0,4], [1,4], [2,4], [0,5], [1,5], [2,5]], [[0,6], [1,6], [2,6], [0,7], [1,7], [2,7], [0,8], [1,8], [2,8]], [[3,0], [4,0], [5,0], [3,1], [4,1], [5,1], [3,2], [4,2], [5,2]], [[3,3], [4,3], [5,3], [3,4], [4,4], [5,4], [3,5], [4,5], [5,5]], [[3,6], [4,6], [5,6], [3,7], [4,7], [5,7], [3,8], [4,8], [5,8]], [[6,0], [7,0], [8,0], [6,1], [7,1], [8,1], [6,2], [7,2], [8,2]], [[6,3], [7,3], [8,3], [6,4], [7,4], [8,4], [6,5], [7,5], [8,5]], [[6,6], [7,6], [8,6], [6,7], [7,7], [8,7], [6,8], [7,8], [8,8]]

# Define an array of the coordinates of each block, so it is more convenient to cycle through.
blockPositions = [cellCoordinates1, cellCoordinates2, cellCoordinates3, cellCoordinates4, cellCoordinates5, cellCoordinates6, cellCoordinates7, cellCoordinates8, cellCoordinates9]

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


def getBlockIndex(columnPosition, rowPosition):
	for block in range(9):
		for piece in range(9):
			if columnPosition == blockPositions[block][piece][1] and rowPosition == blockPositions[block][piece][0]:
				return piece


# Determine what values are not taken in the row.
def testRow(columnPosition, rowPosition):
	colavailableList = [1,2,3,4,5,6,7,8,9]
	# Remove all values that cannot be used by changing them to zero.
	for i in range(9):
		if numberArray[rowPosition][i] > 0:
			colavailableList[numberArray[rowPosition][i]-1] = 0

	# Filter out the unnecessary zeros.
	newList = list(filter(lambda x: (x != 0), colavailableList))
	return newList


# Determine what values are not taken in the column.
def testColumn(columnPosition, rowPosition):
	rowavailableList = [1,2,3,4,5,6,7,8,9]
	# Remove all values that cannot be used by changing them to zero.
	for i in range(9):
		if numberArray[i][columnPosition] > 0:
		 	rowavailableList[numberArray[i][columnPosition]-1] = 0

	# Filter out the unnecessary zeros.
	newList = list(filter(lambda x: (x != 0), rowavailableList))
	return newList


# Verify the 3x3 group of 1-9.
def testBlock(columnPosition, rowPosition):
	thisBlock = getBlock(columnPosition, rowPosition)
	availableList = [1,2,3,4,5,6,7,8,9]

	for i in range(9):
		thisNoNo = numberArray[blockPositions[thisBlock-1][i][0]][blockPositions[thisBlock-1][i][1]]
		if thisNoNo > 0:
			availableList[thisNoNo - 1] = 0

	newList = list(filter(lambda x: (x != 0), availableList))   # Filter out every zero in the list.

	return newList
	

def drawText(labelText, xPos, yPos):
	font = pygame.font.Font('freesansbold.ttf', 25)
	text = font.render(labelText, True, (0, 0, 0))
	textRect = text.get_rect()
	#textRect.center = (xPos // 2, yPos // 2)
	textRect.center = (xPos, yPos)
	return screen.blit(text, textRect)


def drawNumbers():
	screen.fill(backgroundColour)

	pygame.draw.rect(screen, (169,169,169), (140, 20, 120, 120))
	pygame.draw.rect(screen, (169,169,169), (140, 260, 120, 120))
	pygame.draw.rect(screen, (169,169,169), (20, 140, 120, 120))
	pygame.draw.rect(screen, (169,169,169), (260, 140, 120, 120))

	for line in range(10):
		pygame.draw.line(screen, (0, 0, 0), (20 + (line*40), 20), (20 + (line*40), 380))
		pygame.draw.line(screen, (0, 0, 0), (20, 20 + (line*40)), (380, 20 + (line*40)))

	for row in range(9):
		for col in range(9):
			#if numberArray[row][col] > 0:
				#pygame.draw.rect(screen, (242, 248, 252), (col*40+20, row*40+20, 36, 36))
			drawText(str(numberArray[row][col]), col*40 + 40,row*40 + 40)


def findEmptySpot(array):
	for y in range(9):
		for x in range(9):
			if array[y][x] == 0:
				return (y, x)

	return None


def solveBoard():
	findZero = findEmptySpot(numberArray)
	if not findZero:
		return True
	else:
		rowPosition, columnPosition = findZero # If the board has no zeros, determine the value for the next cell closest to the top left.

	colAvailable = testColumn(columnPosition, rowPosition)
	rowAvailable = testRow(columnPosition, rowPosition)
	blockAvailable = testBlock(columnPosition, rowPosition)

	numbersPossible = [1,2,3,4,5,6,7,8,9]
	random.shuffle(numbersPossible)
	
	for value in range(9):
		if (numbersPossible[value] in rowAvailable) and (numbersPossible[value] in blockAvailable) and (numbersPossible[value] in colAvailable):
			numberArray[rowPosition][columnPosition] = numbersPossible[value]
			
			if solveBoard():
				return True
							
			numberArray[rowPosition][columnPosition] = 0

	return False

# Reuable function that will reset the array and generate a nwe board.
def generatePuzzle():
	global numberArray
	numberArray = [[random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0,  random.randint(1, 9), 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0,  random.randint(1, 9), 0 ,0],[0,  random.randint(1, 9), 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0,  random.randint(1, 9), 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0,  random.randint(1, 9) ,0],[0, 0,  random.randint(1, 9), 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0,  random.randint(1, 9), 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, 0 , random.randint(1, 9)]]
	solveBoard()

# Main loop to continuously draw objects and process user input.
def updateDisplay():
	timeTracker = 0
	while True:
		timeTracker += 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if  event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
			elif event.type == pygame.KEYUP:
				if  event.key == pygame.K_g:
					generatePuzzle()

		solveBoard()
		drawNumbers()

		pygame.display.update()
		clock.tick(30)

updateDisplay()