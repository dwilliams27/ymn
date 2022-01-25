from colorama import Fore, Style

from Card import CardFactory
from Player import Player
from state.State import State
from state.Actions import ActionList, RewardPlayerWithMayIAction, DrawDiscardCardAction, DrawPile
from Decisions import AskMayIDecision, AllowMayIDecision, AskDrawDecision, AskDiscardDecision, AskGoDownDecision

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
    for index in range(len(self.state.players)):
      dsize = len(self.state.discard.cards)
      player = self.state.players[(self.state.activePlayerIndex + index) % len(self.state.players)]
      player.makeDecision(AskMayIDecision(player, self.state), self.state)
      if(dsize != len(self.state.discard.cards)):
        # Player whos turn it is took the discard card
        return False
      if(self.state.activeMayIRequester is not None):
        stopIndex = self.getIndexOfPlayer(player)
        done = False
        index = self.state.activePlayerIndex
        while(not done):
          dsize = len(self.state.discard.cards)
          self.state.players[index].makeDecision(AllowMayIDecision(self.state.players[index], self.state), self.state)
          if(dsize != len(self.state.discard.cards)):
            # Player whos turn it is took the discard card
            print(f'{self.state.players[index].getPrintableName()} denies the May I')
            return False
          if(self.state.activeMayIRequester is not None):
            index = self.advanceIndex(index, self.state.players)
            if(index == stopIndex):
              # Player May I is successful
              RewardPlayerWithMayIAction(player).transform(self.state)
              done = True
          else:
            RewardPlayerWithMayIAction(self.state.players[index]).transform(self.state)
            done = True
        # Somebody has May I'd and won, turn begins now
        break
    return True

  def advancePlayerTurn(self):
    self.state.activePlayerIndex = self.advanceIndex(self.state.activePlayerIndex, self.state.players)

  def anyoneDown(self):
    for player in self.state.players:
      if(player.isDown):
        return True
    return False

  def begin(self):
    while(not self.anyoneDown()):
      # Begin turn
      activePlayer = self.state.players[self.state.activePlayerIndex]
      print(f'{activePlayer.getPrintableName()} begins their turn')

      canDraw = True
      # Check if anyone wants to May I
      if(len(self.state.discard.cards) != 0):
        canDraw = self.handleMayIs()

      # Player must decide card to take
      if(canDraw):
        print('candraw')
        activePlayer.makeDecision(AskDrawDecision(activePlayer, self.state), self.state)

      # Player is given chance to go down
      if(CardFactory.canGoDownR1(activePlayer.hand.cards)):
        activePlayer.makeDecision(AskGoDownDecision(activePlayer, self.state), self.state)

      # Player must discard
      activePlayer.makeDecision(AskDiscardDecision(activePlayer, self.state), self.state)

      self.advancePlayerTurn()
