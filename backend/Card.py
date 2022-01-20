import random

from enum import Enum;
from colorama import Style, Fore

class Suit(Enum):
	HEARTS = 0
	DIAMONDS = 1
	SPADES = 2
	CLUBS = 3

class Card:
	def __init__(self, name: str, value: [int], suit: Suit):
		self.name = name
		self.value = value
		self.suit = suit

class CardGroup:
	def __init__(self, cards):
		self.cards = cards

	def printCards(self):
		printStr = ''
		maxWidth = 4
		counter = 0
		for card in self.cards:
			if(counter >= maxWidth):
				counter = 0
				print(printStr)
				printStr = ''
			cardText = self.getCardInColor(card)
			while(len(cardText) < 25):
				cardText += ' '
			printStr += cardText
			counter += 1
		if(len(printStr) != 0):
			print(printStr)

	def getCardInColor(self, card: Card):
		if(card.suit == Suit.HEARTS or card.suit == Suit.DIAMONDS):
			return f'{Fore.RED}|{card.name} of {card.suit.name}|{Style.RESET_ALL}'
		if(card.suit == None):
			return f'{Fore.GREEN}|{card.name} of NONE|{Style.RESET_ALL}'
		return f'{Fore.BLUE}|{card.name} of {card.suit.name}|{Style.RESET_ALL}'

class CardFactory:
	@staticmethod
	def determineInfo(index):
		quarter = index % 13
		quarter += 1
		if(quarter == 1):
			return ['A', [0, 14]]
		if(quarter <= 10):
			return [quarter, [quarter]]
		if(quarter == 11):
			return ['J', [quarter]]
		if(quarter == 12):
			return ['Q', [quarter]]
		if(quarter == 13):
			return ['K', [quarter]]

	@staticmethod
	def constructDeck():
		deck = []
		for index in range(52):
			for suit in [Suit.HEARTS, Suit.DIAMONDS, Suit.SPADES, Suit.CLUBS]:
				info = CardFactory.determineInfo(index)
				deck.append(Card(info[0], info[1], suit))
		deck.append(Card('*', range(13), None))
		deck.append(Card('*', range(13), None))
		return deck

	@staticmethod
	def generateDeckForGame(num_players):
		deck = []
		for _ in range(num_players // 2):
			deck += CardFactory.constructDeck()
		return deck

	@staticmethod
	def shuffleDeck(deck: [Card]):
		random.shuffle(deck)

