import random

# Cards in UNO are in the format "[colour][number]", e.g. "R2", "B9", "G0". 
# In this version, special cards such as the +2, +4 and reverse cards are not supported (yet). 
# In this version, you do not need to call "Uno!" when you have a single card left. 

# All the variables

deck = []
playerCards = [[], []]

currentCardOnTable = ""
currentPlayer = 1

gameHasNotEndedYet = True

# All the functions

def cardCanBePlayed(card): 
	return card in playerCards[currentPlayer] and ((card[0] == currentCardOnTable[0]) or (card[1] == currentCardOnTable[1]))

def playCard(card): 
	global currentCardOnTable

	currentCardOnTable = card
	playerCards[currentPlayer].remove(card)
		
def drawCard():
	nextCard = deck.pop()
	playerCards[currentPlayer].append(nextCard)

def showPlayerCards():
	print("")
	cards = ""
	for card in playerCards[currentPlayer]:
		cards += "[ " + card + " ]"
	print(cards)

def showCurrentCardOnTable():
	print("")
	print("The current card on the table is " + currentCardOnTable + "!")

def createNewDeck():
	colours = ["R", "G", "B", "Y"]
	for colour in colours: 
		for number in range(10):
			card = colour + str(number)
			deck.append(card)
	random.shuffle(deck)

def switchPlayer():
	global currentPlayer

	currentPlayer = (currentPlayer + 1) % 2
	print("")
	print("It's Player " + str(currentPlayer) + "\'s turn!")

def checkIfPlayerHasWon():
	global playerCards

	if playerCards[currentPlayer] == []:
		gameHasNotEndedYet = False
		print("")
		print("Yay! Player " + str(currentPlayer) + " has won the game! Well done!")
		quit()

# All the code that will actually run

createNewDeck()

for i in range(6):
	drawCard()

switchPlayer()

for i in range(6):
	drawCard()

currentCardOnTable = deck.pop()
showCurrentCardOnTable()

while (gameHasNotEndedYet):
	showPlayerCards()

	command = raw_input("Play a card or draw one from the deck: ")

	if command == "draw":
		drawCard()
		continue
	
	if cardCanBePlayed(command):
		playCard(command)
		showCurrentCardOnTable()
		checkIfPlayerHasWon()
		switchPlayer()
	else:
		print("Sorry, but you cannot play this card.")
