import pygame
import time, sys, random
from SudokuGenerator import generatePuzzle
# Add timer
# Add mistake counter by state = "WRONG"
# Clean up code
# Add input buttons?
# MAke how to play
#~~ Speed up the generator, get rid of all prints
# Look for heres

# Initialize the program.
pygame.init()

# Define initial variable values.
WIN_WIDTH = 400
WIN_HEIGHT = 400 + 50 # 50px for the timer
MARGIN = 40
gameOver = False

numberArray = generatePuzzle([[random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, random.randint(1, 9), 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, random.randint(1, 9), 0 ,0],[0, random.randint(1, 9), 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, random.randint(1, 9), 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, random.randint(1, 9) ,0],[0, 0, random.randint(1, 9), 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, random.randint(1, 9), 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, 0 , random.randint(1, 9)]])
inputArray = []
for rows in range(9):
	inputArray.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
backgroundColour = (255, 255, 255)
screen.fill(backgroundColour)

pygame.display.set_caption('Sudoku')

start_time = time.time()
clock = pygame.time.Clock()

inptObjects = []

def drawText(labelText, xPos, yPos, thisType):
	font = pygame.font.Font('freesansbold.ttf', 25)
	if thisType == "Input":
		thisColor = (52, 72, 97)#(117, 58, 14)
	elif thisType == "Back":
		thisColor = (0, 0, 0)
	elif thisType == "Red":
		thisColor = (132, 21, 0)#(245, 57, 12)
	elif thisType == "Timer":
		thisColor = (148, 163, 183)
	text = font.render(labelText, True, thisColor)
	textRect = text.get_rect()
	textRect.center = (xPos, yPos+3)
	return screen.blit(text, textRect)

def checkValue(number, ROW, COL): # Adapted from TechWithTim
		# Check the row
		for col in range(9):
			if numberArray[ROW][col] == number and COL != col:
				return False

		# Check the col
		for row in range(9):
			if numberArray[row][COL] == number and ROW != row:
				return False

		# Check box
		boxX = COL // 3
		boxY = ROW // 3

		for i in range(boxY*3, boxY*3 + 3):
			for j in range(boxX * 3, boxX*3 + 3):
				if numberArray[i][j] == number and i != ROW and j != COL:
					return False

		return True

class numberPicker():
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.size = 40
		self.xPos = col * self.size + MARGIN
		self.yPos = row * self.size + MARGIN
		self.state = "Nothing"

	def clickedAction(self):
		mouseX, mouseY = pygame.mouse.get_pos()
		if mouseX > self.xPos - self.size/2 and mouseX < self.xPos + self.size/2:
			if mouseY > self.yPos - self.size/2 and mouseY < self.yPos + self.size/2:
				self.state = "Clicked"

		elif self.state != "WRONG":
			# if checkValue(inputArray[self.row][self.col], self.row, self.col) == False:
			# 	inputArray[self.row][self.col] = 0
			self.state = "Nothing"

	def processMouse(self, inputN):
		mouseX, mouseY = pygame.mouse.get_pos()

		# Here, make sure you can input another value after you got it wrong, WITHOUT reclicking the box
		if self.state == "Clicked" or self.state == "WRONG":
			#Inputing a number from click!
			if inputN == 0:
				numberArray[self.row][self.col] = inputN
				inputArray[self.row][self.col] = inputN
				self.state = "Nothing"
				return None

			boole = checkValue(inputN, self.row, self.col)
			if boole: #Returns True
				numberArray[self.row][self.col] = inputN
				inputArray[self.row][self.col] = inputN
				self.state = "Nothing"
				return None
			else:
				self.state = "WRONG"
				#inputArray[self.row][self.col] = inputN


		return None

	def helper(self):
		mouseX, mouseY = pygame.mouse.get_pos()

		if mouseX > self.xPos - self.size/2and mouseX < self.xPos + self.size - self.size/2:
			if mouseY > self.yPos - self.size/2 and mouseY < self.yPos + self.size - self.size/2:

				highlighterColor = (206, 229, 255)#(255, 243, 204)#(255, 239, 224)#(197, 197, 197)#(238, 239, 243)
				for col in range(9):
					# if numberArray[self.yPos][col] == 0:
					if col != self.col:
						pygame.draw.rect(screen, highlighterColor, ((col*40 + MARGIN) - self.size/2, self.yPos - self.size/2, self.size, self.size))

				for row in range(9):
					# if numberArray[row][self.xPos] == 0:
					if row != self.row:
						pygame.draw.rect(screen, highlighterColor, (self.xPos - self.size/2, (row*40 + MARGIN) - self.size/2, self.size, self.size))

				boxX = self.col // 3
				boxY = self.row // 3

				for i in range(boxY*3, boxY*3 + 3):
					for j in range(boxX * 3, boxX*3 + 3):
						if i != self.row and j != self.col:
						# if numberArray[i][j] == 0:
							pygame.draw.rect(screen, highlighterColor, ((j*40 + MARGIN) - self.size/2, (i*40 + MARGIN) - self.size/2, self.size, self.size))

	def draw(self):
		if self.state == "Nothing":
			pass
			#self.helper()
		elif self.state == "WRONG":
			#m = 4#(245, 57, 12)
			pygame.draw.rect(screen, (246, 60, 81) , (self.xPos - self.size/2, self.yPos - self.size/2, self.size, self.size))
			drawText("X", self.xPos, self.yPos, "Red")
		elif self.state == "Clicked":
			#self.helper()
			thisSize = 6
			pygame.draw.rect(screen, (255,165,0), (self.xPos - self.size/2 + thisSize/2 - 1, self.yPos - self.size/2 + thisSize/2 - 1, self.size - thisSize + 2, self.size - thisSize + 2), 6)
			
for row in range(9):
	for col in range(9):
		if numberArray[row][col] == 0:
			inptObjects.append(numberPicker(row, col))

startArray = numberArray

def drawTimer():
	global timeElapsed, start_time

	elapsed_time = time.time() - start_time
	#time.strftime("%H:%M:%S", time.gmtime(elapsed_time))

	#pygame.draw.rect(screen, (200,150,70), (140, 20, 120, 120))
	drawText(str(time.strftime("%M:%S", time.gmtime(elapsed_time))), 60, WIN_HEIGHT - 37, "Timer")


def drawNumbers():
	yMarg = 0
	color1 = (200,150,70)
	color2 = (230,210,185)
	gray = (238, 236, 224)
	#Gray color (probably too dark anyways):(125, 125, 125)
	pygame.draw.rect(screen, (255, 255, 255), (140, 20 + yMarg, 120, 120))
	pygame.draw.rect(screen, (255, 255, 255), (140, 260 + yMarg, 120, 120))
	pygame.draw.rect(screen, (255, 255, 255), (20, 140 + yMarg, 120, 120))
	pygame.draw.rect(screen, (255, 255, 255), (260, 140 + yMarg, 120, 120))

	pygame.draw.rect(screen, (238, 236, 224) , (20, 20 + yMarg, 120, 120))
	pygame.draw.rect(screen, (238, 236, 224), (260, 260 + yMarg, 120, 120))
	pygame.draw.rect(screen, (238, 236, 224), (20, 260 + yMarg, 120, 120))
	pygame.draw.rect(screen, (238, 236, 224), (260, 20 + yMarg, 120, 120))
	pygame.draw.rect(screen, (238, 236, 224), (140, 140 + yMarg, 120, 120))

	
	for obj in inptObjects:
		obj.draw()

	for row in range(9):
		for col in range(9):
			# if numberArray[row][col] > 0:
			# 	drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN, "Input")
			if startArray[row][col] > 0:
				drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN + yMarg, "Back")
			if inputArray[row][col] > 0:
				drawText(str(inputArray[row][col]), col*40 + MARGIN,row*40 + MARGIN + yMarg, "Input")

	for line in range(10):
		pygame.draw.line(screen, (0, 0, 0), (20 + (line*40), 20 + yMarg), (20 + (line*40), 380 + yMarg))
		pygame.draw.line(screen, (0, 0, 0), (20, 20 + (line*40) + yMarg), (380, 20 + (line*40) + yMarg))

	global gameOver
	if not any(0 in sublist for sublist in numberArray):
		for row in range(9):
			for col in range(9):
				if not checkValue(numberArray[row][col], row, col):
					return False
				gameOver = True

def drawArray():
	yMarg = 0
	for row in range(9):
		for col in range(9):
			# if numberArray[row][col] > 0:
			# 	drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN, "Input")
			if startArray[row][col] > 0:
				drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN + yMarg, "Back")
			if inputArray[row][col] > 0:
				drawText(str(inputArray[row][col]), col*40 + MARGIN,row*40 + MARGIN + yMarg, "Back")

	for line in range(10):
		pygame.draw.line(screen, (0, 0, 0), (20 + (line*40), 20 + yMarg), (20 + (line*40), 380 + yMarg))
		pygame.draw.line(screen, (0, 0, 0), (20, 20 + (line*40) + yMarg), (380, 20 + (line*40) + yMarg))


def restartGame():
	global gameOver
	global numberArray
	global inputArray
	global inptObjects
	global startArray
	global start_time

	gameOver = False
	start_time = time.time()

	numberArray = generatePuzzle([[random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, random.randint(1, 9), 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, random.randint(1, 9), 0 ,0],[0, random.randint(1, 9), 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, random.randint(1, 9), 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, random.randint(1, 9) ,0],[0, 0, random.randint(1, 9), 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, random.randint(1, 9), 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, 0 , random.randint(1, 9)]])
	inputArray = []
	for rows in range(9):
		inputArray.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

	inptObjects = []

	for row in range(9):
		for col in range(9):
			if numberArray[row][col] == 0:
				inptObjects.append(numberPicker(row, col))
	
	startArray = numberArray

	updateDisplay()


# Main loop to continuously draw objects and process user input.
def updateDisplay():
	timeTracker = 0
	global gameOver

	while not gameOver:
		mouseX, mouseY = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_g:
					None#generatePuzzle()
				elif event.key == pygame.K_1:
					for obj in inptObjects: 
						obj.processMouse(1)
				elif event.key == pygame.K_2:
					for obj in inptObjects: 
						obj.processMouse(2)
				elif event.key == pygame.K_3:
					for obj in inptObjects: 
						obj.processMouse(3)
				elif event.key == pygame.K_4:
					for obj in inptObjects: 
						obj.processMouse(4)
				elif event.key == pygame.K_5:
					for obj in inptObjects: 
						obj.processMouse(5)
				elif event.key == pygame.K_6:
					for obj in inptObjects: 
						obj.processMouse(6)
				elif event.key == pygame.K_7:
					for obj in inptObjects: 
						obj.processMouse(7)
				elif event.key == pygame.K_8:
					for obj in inptObjects: 
						obj.processMouse(8)
				elif event.key == pygame.K_9:
					for obj in inptObjects: 
						obj.processMouse(9)
				elif event.key == pygame.K_0:
					for obj in inptObjects: 
						obj.processMouse(0)

			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for obj in inptObjects:
					obj.state = "Nothing"
					obj.clickedAction()
		
		screen.fill(backgroundColour)	
		drawNumbers()
		drawTimer()
		#drawText("Time: " + str(round(timeTracker/100)), 0, 10, "Back")
		pygame.display.update()

		#timeTracker += 8.3#16.66666666667
		clock.tick(60)

	finishTime = time.time() - start_time

	#Stop processing coverField, wait for user to restart the game.
	while gameOver: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					restartGame() # HERE, reset startime variable
			
		screen.fill(backgroundColour)
		#secs = round(timeTracker / 1000)
		#drawGame()
		drawArray()
		thisRectW = 280
		pygame.draw.rect(screen, (239, 255, 234), (WIN_WIDTH/2 - thisRectW/2, (WIN_HEIGHT - 50)/2 - 30/2, thisRectW, 30))
		drawText("Press space to restart.", WIN_WIDTH/2, (WIN_HEIGHT - 50)/2, "Back")
		drawText(("Completed in: " + str(time.strftime("%M:%S", time.gmtime(finishTime)))), WIN_WIDTH/2, WIN_HEIGHT - 37, "Timer")

		pygame.display.flip()

		clock.tick(60)

updateDisplay()