import pygame
import time, sys, random
from SudokuGenerator import generatePuzzle
# FIX clickableObj typo
# Initialize the program.
pygame.init()

# Define initial variable values.
WIN_WIDTH = 400
WIN_HEIGHT = 400
MARGIN = 40
gameOver = False

numberArray = generatePuzzle([[random.randint(1, 9), 0, 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0,  random.randint(1, 9), 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0,  random.randint(1, 9), 0 ,0],[0,  random.randint(1, 9), 0, 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0,  random.randint(1, 9), 0, 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0,  random.randint(1, 9) ,0],[0, 0,  random.randint(1, 9), 0, 0, 0, 0, 0 ,0],[0, 0, 0, 0, 0,  random.randint(1, 9), 0, 0 ,0],[0, 0, 0, 0, 0, 0, 0, 0 , random.randint(1, 9)]])
inputArray = []
for rows in range(9):
	inputArray.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
backgroundColour = (255, 255, 255)
screen.fill(backgroundColour)

pygame.display.set_caption('Sudoku')

clock = pygame.time.Clock()

clickableOjbects = []

def drawText(labelText, xPos, yPos, thisType):
	font = pygame.font.Font('freesansbold.ttf', 25)
	if thisType == "Input":
		thisColor =  (117, 58, 14)
	elif thisType == "Back":
		thisColor =  (0, 0, 0)
	text = font.render(labelText, True, thisColor)
	textRect = text.get_rect()
	textRect.center = (xPos, yPos)
	return screen.blit(text, textRect)

def checkValue(number, ROW, COL):
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
		if mouseX > self.xPos  - self.size/2 and mouseX < self.xPos + self.size/2:
			if mouseY > self.yPos  - self.size/2 and mouseY < self.yPos + self.size/2:
				self.state = "Clicked"

		else: self.state = "Nothing"

	def processMouse(self, inputN):
		mouseX, mouseY = pygame.mouse.get_pos()

		if self.state == "Clicked":
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

		"""#self.state = "Nothing"
		for obj in clickableOjbects:
			if obj.state == "Clicked":
				return
		if self.state != "Clicked" and mouseX > self.xPos  - self.size/2 and mouseX < self.xPos + self.size/2:
			if mouseY > self.yPos - self.size/2 and mouseY < self.yPos + self.size/2:
				#self.state = "Nothing"
				boole = checkValue(inputN, self.row, self.col)
				if boole: #Returns True
					numberArray[self.row][self.col] = inputN

					# Get rid of this object because this piece is solved DO NOT DO THIS BECUASE IT CAN BE WRONG
					# localCounter = 0
					# for obj in clickableOjbects:
					# 	if obj.row == self.row and obj.col == self.col:
					# 		clickableOjbects.pop(localCounter)
					# 	localCounter+=1

					# what is this here!
					for col in range(9):
						pygame.draw.rect(screen, (255,0,0), ((col*40 + MARGIN) - self.size/2, self.yPos - self.size/2, self.size, self.size), 3)

					# # Check the col
					# for row in range(9):
					# 	if numberArray[row][COL] == number and ROW != row:
					# 		return False

					# # Check box
					# boxX = COL // 3
					# boxY = ROW // 3

					# for i in range(boxY*3, boxY*3 + 3):
					# 	for j in range(boxX * 3, boxX*3 + 3):
					# 		if numberArray[i][j] == number and i != ROW and j != COL:
					# 			return False


					return None

				else:
					self.state = "WRONG"
				#self.state = "WRONG"""
		return None

	def helper(self):
		mouseX, mouseY = pygame.mouse.get_pos()

		if mouseX > self.xPos  - self.size/2and mouseX < self.xPos + self.size  - self.size/2:
			if mouseY > self.yPos  - self.size/2 and mouseY < self.yPos + self.size  - self.size/2:

				highlighterColor = (255,160,122)#(255, 239, 224)#(197, 197, 197)#(238, 239, 243)
				for col in range(9):
					# if numberArray[self.yPos][col] == 0:
					pygame.draw.rect(screen, highlighterColor, ((col*40 + MARGIN) - self.size/2, self.yPos - self.size/2, self.size, self.size))

				for row in range(9):
					# if numberArray[row][self.xPos] == 0:
					pygame.draw.rect(screen, highlighterColor, (self.xPos - self.size/2, (row*40 + MARGIN) - self.size/2, self.size, self.size))

				boxX = self.col // 3
				boxY = self.row // 3

				for i in range(boxY*3, boxY*3 + 3):
					for j in range(boxX * 3, boxX*3 + 3):
						# if numberArray[i][j] == 0:
						pygame.draw.rect(screen, highlighterColor, ((j*40 + MARGIN) - self.size/2, (i*40 + MARGIN) - self.size/2, self.size, self.size))

	def draw(self):
		if self.state == "Nothing":
			None#self.helper()
		elif self.state == "WRONG":
			pygame.draw.rect(screen, (255,0,0), (self.xPos - self.size/2, self.yPos - self.size/2, self.size, self.size), 3)
		elif self.state == "Clicked":
			#self.helper()
			thisSize = 6
			pygame.draw.rect(screen, (255,165,0), (self.xPos - self.size/2 + thisSize/2 - 1, self.yPos - self.size/2 + thisSize/2 - 1, self.size - thisSize + 2, self.size - thisSize + 2 ), 6)
			
for row in range(9):
	for col in range(9):
		if numberArray[row][col] == 0:
			clickableOjbects.append(numberPicker(row, col))

startArray = numberArray

def drawNumbers():
	screen.fill(backgroundColour)
	#Gray color (probably too dark anyways):(125, 125, 125)
	pygame.draw.rect(screen, (200,150,70), (140, 20, 120, 120))
	pygame.draw.rect(screen, (200,150,70), (140, 260, 120, 120))
	pygame.draw.rect(screen, (200,150,70), (20, 140, 120, 120))
	pygame.draw.rect(screen, (200,150,70), (260, 140, 120, 120))

	pygame.draw.rect(screen, (230,210,185), (20, 20, 120, 120))
	pygame.draw.rect(screen, (230,210,185), (260, 260, 120, 120))
	pygame.draw.rect(screen, (230,210,185), (20, 260, 120, 120))
	pygame.draw.rect(screen, (230,210,185), (260, 20, 120, 120))
	pygame.draw.rect(screen, (230,210,185), (140, 140, 120, 120))

	for obj in clickableOjbects:
		obj.draw()

	for row in range(9):
		for col in range(9):
			# if numberArray[row][col] > 0:
			# 	drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN, "Input")
			if startArray[row][col] > 0:
				drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN, "Back")
			if inputArray[row][col] > 0:
				drawText(str(numberArray[row][col]), col*40 + MARGIN,row*40 + MARGIN, "Input")

	for line in range(10):
		pygame.draw.line(screen, (0, 0, 0), (20 + (line*40), 20), (20 + (line*40), 380))
		pygame.draw.line(screen, (0, 0, 0), (20, 20 + (line*40)), (380, 20 + (line*40)))

	global gameOver
	if not any(0 in sublist for sublist in numberArray):
		for row in range(9):
			for col in range(9):
				if not checkValue(numberArray[row][col], row, col):
					return False
				gameOver = True

# Main loop to continuously draw objects and process user input.
def updateDisplay():
	timeTracker = 0
	global gameOver
	while not gameOver:
		timeTracker += 1
		mouseX, mouseY = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()
				#
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_g:
					None#generatePuzzle()
				elif event.key == pygame.K_1:
					for obj in clickableOjbects: 
						obj.processMouse(1)
				elif event.key == pygame.K_2:
					for obj in clickableOjbects: 
						obj.processMouse(2)
				elif event.key == pygame.K_3:
					for obj in clickableOjbects: 
						obj.processMouse(3)
				elif event.key == pygame.K_4:
					for obj in clickableOjbects: 
						obj.processMouse(4)
				elif event.key == pygame.K_5:
					for obj in clickableOjbects: 
						obj.processMouse(5)
				elif event.key == pygame.K_6:
					for obj in clickableOjbects: 
						obj.processMouse(6)
				elif event.key == pygame.K_7:
					for obj in clickableOjbects: 
						obj.processMouse(7)
				elif event.key == pygame.K_8:
					for obj in clickableOjbects: 
						obj.processMouse(8)
				elif event.key == pygame.K_9:
					for obj in clickableOjbects: 
						obj.processMouse(9)
				elif event.key == pygame.K_0:
					for obj in clickableOjbects: 
						obj.processMouse(0)

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				print("CLICKED")
				for obj in clickableOjbects:
					obj.state = "Nothing"
					obj.clickedAction()

		drawNumbers()

		pygame.display.update()
		clock.tick(30)

	#Stop processing coverField, wait for user to restart the game.
	while gameOver: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYUP:
				pass#HEREif  event.key == pygame.K_SPACE:
					#startGame()
			
		gameDisplay.fill(backgroudColour)

		#drawGame()
		drawText("Press space to restart.", 175, 175)
		drawText("Time: " + str(timeTracker), 175, 210)

		pygame.display.flip()

		clock.tick(60)

updateDisplay()