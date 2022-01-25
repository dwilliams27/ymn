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

  def getCardInColor(self):
    if(self.suit == Suit.HEARTS or self.suit == Suit.DIAMONDS):
      return f'{Fore.RED}|{self.name} of {self.suit.name}|{Style.RESET_ALL}'
    if(self.suit == None):
      return f'{Fore.GREEN}|{self.name} of NONE|{Style.RESET_ALL}'
    return f'{Fore.BLUE}|{self.name} of {self.suit.name}|{Style.RESET_ALL}'

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
      cardText = card.getCardInColor()
      while(len(cardText) < 25):
        cardText += ' '
      printStr += cardText
      counter += 1
    if(len(printStr) != 0):
      print(printStr)

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
    # deck.append(Card('*', range(13), None))
    # deck.append(Card('*', range(13), None))
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

  @staticmethod
  def canGoDownR1Helper(four_potential_map):
    return (four_potential_map[0] > 0 and four_potential_map[0] + four_potential_map[1] >= 3)
    
  @staticmethod
  def canGoDownR1(cards: [Card]):
    countMap = {}
    for card in cards:
      if(card.name in countMap):
        countMap[card.name] += 1
      else:
        countMap[card.name] = 1

    freqMap = {}
    for key in countMap:
      if(key != '*'):
        if(countMap[key] in freqMap):
          freqMap[countMap[key]] += 1
        else:
          freqMap[countMap[key]] = 1
    
    four_potential_map = { 0: 0, 1: 0 }
    for key in freqMap:
      if key <= 6:
        nkey = key
        if nkey > 4:
          nkey = 4
        if((4 - nkey) in four_potential_map):
          four_potential_map[4 - nkey] += freqMap[key]
        else:
          four_potential_map[4 - nkey] = freqMap[key]

    # Need to handle jokers
    # jokers = countMap['*'] 
    # while(jokers > 0):
    #   if(four_potentialMap[])
    # print(f'3:{threegroups} 4:{biggroups}')
    return CardFactory.canGoDownR1Helper(four_potential_map)
