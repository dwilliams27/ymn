from colorama import Fore, Style

from Card import CardFactory
from Player import Player
from state.State import State
from state.Actions import ActionList, RewardPlayerWithMayIAction
from Decisions import AskMayIDecision, AllowMayIDecision

class Game:
  def __init__(self, num_players):
    self.state = State(num_players)
    for i in range(num_players):
      self.state.players[i] = Player(i)
    
    self.state.setup()
    self.begin()

  def advanceIndex(self, index, plist):
    newIndex = -1
    if(index < len(plist) - 1):
      newIndex = index + 1
    else:
      newIndex = 0
    return newIndex

  def verifyRoundOver(self):
    for player in self.state.players:
      if len(player.hand) == 0:
        self.state.winner = player
        return True
    return False

  def getIndexOfPlayer(self, player):
    i = 0
    for p in self.state.players:
      if(p.name == player.name):
        return i
      i += 1

  def handleMayIs(self):
    for player in self.state.players:
      player.makeDecision(AskMayIDecision(self.state), self.state)
      if(self.state.activeMayIRequester is not None):
        print(f'Player {self.state.activeMayIRequester.getPrintableName()} wants to May I')
        stopIndex = self.getIndexOfPlayer(player)
        done = False
        index = self.state.activePlayerIndex
        while(not done):
          self.state.players[index].makeDecision(AllowMayIDecision(self.state.players[index], self.state), self.state)
          if(self.state.activeMayIRequester is not None):
            index = self.advanceIndex(index, self.state.players)
            if(index == stopIndex):
              # Player May I is successful
              RewardPlayerWithMayIAction(player).transform(self.state)
              done = True
          else:
            RewardPlayerWithMayIAction(player).transform(self.state)
            done = True
        # Somebody has May I'd and won, turn begins now
        break

  def begin(self):
    #while(not self.verifyRoundOver()):
    # Check if anyone wants to May I
    if(len(self.state.discard.cards) != 0):
      self.handleMayIs()

    # Begin turn
    print(f'{self.state.players[self.state.activePlayerIndex].getPrintableName()} begins their turn')

    # Player must decide card to take

