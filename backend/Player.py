import random

from colorama import Fore, Style
from Card import CardGroup
from utils.NameGen import NameFactory
from Decisions import Decision
from state.Actions import PassAction, AskMayIAction, ApproveMayIRequestAction, DenyMayIRequestAction, DiscardCardAction, GoDownAction

class Player:
  def __init__(self, playerIndex: int, isAI = True):
    self.playerIndex = playerIndex
    self.hand = CardGroup([])
    self.isDown = False
    self.mayIs = 0
    if(isAI):
      self.name = NameFactory.generateName()

  def makeDecision(self, decision: Decision, state):
    # Random for now
    possibleActions = decision.getPossibleActions()
    rand = random.randrange(len(possibleActions))

    if(isinstance(possibleActions[rand], PassAction)):
      print(f'{self.getPrintableName()} decided to pass')
      
    if(isinstance(possibleActions[rand], AskMayIAction)):
      print(f'{self.getPrintableName()} decided to ask to May I')

    if(isinstance(possibleActions[rand], ApproveMayIRequestAction)):
      print(f'{self.getPrintableName()} will allow the May I request')

    if(isinstance(possibleActions[rand], DenyMayIRequestAction)):
      print(f'{self.getPrintableName()} denies the May I request')

    if(isinstance(possibleActions[rand], DiscardCardAction)):
      randCard = random.randrange(len(self.hand.cards))
      print(f'{self.getPrintableName()} will discard a {self.hand.cards[randCard].getCardInColor()}')
      possibleActions[rand].setCardIndex(randCard)

    if(isinstance(possibleActions[rand], GoDownAction)):
      print(f'{self.getPrintableName()} WANTS TO GO DOWN')
      self.hand.printCards()

    possibleActions[rand].transform(state)

  def getPrintableName(self):
    return f'{Fore.YELLOW}{self.name}{Style.RESET_ALL}'
    
