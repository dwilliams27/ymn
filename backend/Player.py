import random

from colorama import Fore, Style
from Card import CardGroup
from utils.NameGen import NameFactory
from Decisions import Decision
from state.Actions import ActionList

class Player:
  def __init__(self, playerIndex: int, isAI = True):
    self.playerIndex = playerIndex
    self.hand = CardGroup([])
    self.isDown = False
    if(isAI):
      self.name = NameFactory.generateName()

  def makeDecision(self, decision: Decision, state):
    # Random for now
    possibleActions = decision.getPossibleActions()
    rand = random.randrange(len(possibleActions))
    if(possibleActions[rand].__name__ == ActionList.Pass.value):
      possibleActions[rand](self).transform(state)
    if(possibleActions[rand].__name__ == ActionList.AskMayI.value):
      possibleActions[rand](self).transform(state)

  def getPrintableName(self):
    return f'{Fore.YELLOW}{self.name}{Style.RESET_ALL}'
    
