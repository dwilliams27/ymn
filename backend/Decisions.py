from abc import ABC, abstractmethod
from enum import Enum;

from backend.State import State
from backend.Actions import PassAction

class Decision(ABC):
  @abstractmethod
  def decide(self):
    pass

  @abstractmethod
  def getPossibleActions(self):
    pass

class AskMayIDecision(Decision):
  def __init__(self, state: State):
    self.state = state
    self.allowedActions = [None, ]

  def getPossibleActions(self):
    if(self.state.activeMayIRequest != None):
      return [PassAction.id]
    return [Actions.PASS, Actions.ASK_MAY_I]
