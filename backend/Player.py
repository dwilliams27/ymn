from Card import CardGroup
from utils.NameGen import NameFactory

class Player:
  def __init__(self, playerIndex: int, isAI = True):
    self.playerIndex = playerIndex
    self.hand = CardGroup([])
    if(isAI):
      self.name = NameFactory.generateName()
