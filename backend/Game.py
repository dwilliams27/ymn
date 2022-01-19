from Card import CardFactory
from Player import Player
from State import State
from Actions import ChangeActivePlayerAction

class Game:
  def __init__(self, num_players):
    self.state = State(num_players)

  def advanceTurn():
    newIndex = -1
    if(self.state.activePlayerIndex < len(self.state.players) - 1):
      newIndex = self.state.activePlayerIndex + 1
    else:
      newIndex = 0
    ChangeActivePlayerAction(newIndex).transform(self.state)
