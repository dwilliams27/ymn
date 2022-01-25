from abc import ABC, abstractmethod
from enum import Enum;

from state.State import State
from state.Actions import Action, ActionList, DrawDeckCardAction, DrawDiscardCardAction, \
  DenyMayIRequestAction, ApproveMayIRequestAction, AskMayIAction, PassAction, DiscardCardAction, GoDownAction
from Card import CardFactory

state_module = __import__('state')

class Decision(ABC):
  @abstractmethod
  def getPossibleActions(self):
    pass

class AskMayIDecision(Decision):
  def __init__(self, player, state: State):
    self.player = player
    self.state = state

  def getPossibleActions(self):
    if(self.state.activePlayerIndex == self.player.playerIndex):
      return [PassAction(self.player), DrawDiscardCardAction(self.player)]
    if(self.state.activeMayIRequester != None or self.player.mayIs >= 3):
      return [PassAction(self.player)]
    return [PassAction(self.player), AskMayIAction(self.player)]

class AllowMayIDecision(Decision):
  def __init__(self, player, state: State):
    self.player = player
    self.state = state
  
  def getPossibleActions(self):
    if(self.player.isDown and self.state.activePlayer.name != self.player.name):
      return [ApproveMayIRequestAction(self.player)]
    if(self.player.playerIndex == self.state.activePlayerIndex):
      return [ApproveMayIRequestAction(self.player), DrawDiscardCardAction(self.player)]
    return [ApproveMayIRequestAction(self.player), DenyMayIRequestAction(self.player)]

class AskDrawDecision(Decision):
  def __init__(self, player, state: State):
    self.player = player
    self.state = state

  def getPossibleActions(self):
    if(len(self.state.discard.cards) > 0):
      return [DrawDeckCardAction(self.player), DrawDiscardCardAction(self.player)]
    return [DrawDeckCardAction(self.player)]

class AskDiscardDecision(Decision):
  def __init__(self, player, state: State):
    self.player = player
    self.state = state

  def getPossibleActions(self):
    return [DiscardCardAction(self.player)]

class AskGoDownDecision(Decision):
  def __init__(self, player, state: State):
    self.player = player
    self.state = state

  def getPossibleActions(self):
    # return [PassAction(self.player), GoDownAction(self.player)]
    return [GoDownAction(self.player)]