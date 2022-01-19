
from enum import Enum;

class Suit(Enum):
  HEARTS = 0
  DIAMONDS = 1
  SPADES = 2
  CLUBS = 3

class Card:
	def __init__(self, name: str, value: int, suit: Suit) -> None:
		self.name = name
		self.value = value
		self.suit = suit

class CardFactory:
	def determineInfo(self, index):
		quarter = index % 14
		if(quarter == 0):
			return ['ace', [0, 14]]
		if(quarter < 10):
			return [quarter, [quarter]]
		if(quarter == 11):
			return ['jack', [quarter]]
		if(quarter == 12):
			return ['queen', [quarter]]
		if(quarter == 13):
			return ['king', [quarter]]
		if(quarter == 14):
			return ['joker', range(14)]

	def constructDeck(self):
		deck = Card[52]
		for index in range(52):
			for suit in [Suit.HEARTS, Suit.DIAMONDS, Suit.SPADES, Suit.CLUBS]:
				info = self.determineInfo(index)
				deck[index] = Card(info[0], info[1], suit)

	def generateDeckForGame(self, num_players):
		deck = []
		for _ in num_players:
			deck.append(self.constructDeck())
		return deck

