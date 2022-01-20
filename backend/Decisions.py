from abc import ABC, abstractmethod
from enum import Enum;

from state.State import State
from state.Actions import Action, ActionList

state_module = __import__('state')

class Decision(ABC):
  @abstractmethod
  def getPossibleActions(self):
    pass

class AskMayIDecision(Decision):
  def __init__(self, state: State):
    self.state = state

  def getPossibleActions(self):
    if(self.state.activeMayIRequester != None):
      return [getattr(state_module.Actions, ActionList.Pass.value)]
    return [getattr(state_module.Actions, ActionList.Pass.value), getattr(state_module.Actions, ActionList.AskMayI.value)]

class AllowMayIDecision(Decision):
  def __init__(self, player, state: State):
    self.player = player
    self.state = state
  
  def getPossibleActions(self):
    if(self.player.isDown and self.state.activePlayer.name != self.player.name):
      return [getattr(state_module.Actions, ActionList.DenyMayIRequest)]
    return [getattr(state_module.Actions, ActionList.ApproveMayIRequest.value), getattr(state_module.Actions, ActionList.DenyMayIRequest.value)]
