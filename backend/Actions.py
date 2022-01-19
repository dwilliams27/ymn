from abc import ABC, abstractmethod
from enum import Enum;

from Player import Player
from State import State

class Action(ABC):
  @property
  @abstractmethod
  def id(self):
    pass

  @abstractmethod
  def transform(self, state: State) -> None:
    pass

class DrawPile(Enum):
  DECK = 0
  DISCARD = 1

class PassAction(Action):
  def transform(self, state):
    pass

class ChangeActivePlayerAction(Action):
  def __init__(self, newIndex: int):
    super().__init__()
    self.newIndex = newIndex

  def transform(self, state: State):
    state.activePlayer = state.players[self.newIndex]
    state.activePlayerIndex = self.newIndex

class DrawCardAction(Action):
  def __init__(self, playerIndex: int, pile: DrawPile):
    self.playerIndex = playerIndex
    self.pile = pile

  def transform(self, state: State):
    if(self.pile == DrawPile.DECK):
      state.players[self.playerIndex].hand.cards.append(state.deck.cards.pop(0))
    if(self.pile == DrawPile.DISCARD):
      if(len(state.discard.cards) == 0):
        print("Cannot draw from empty discard pile")
        raise
      state.players[self.playerIndex].hand.cards.append(state.discard.cards.pop(0))

class AskMayIAction(Action):
  def __init__(self, player: Player):
    self.player = player

  def transform(self, state: State):
    if(state.activeMayIRequest != None):
      print("Another player already has an active May I request")
      raise
    state.activeMayIRequest = self.player

class ApproveMayIRequestAction(Action):
  def transform(self, state: State):
    pass

class DenyMayIRequestAction(Action):
  def __init__(self, player: Player):
    self.player = player

  def transform(self, state: State):
    state.mayIRequestWinner = self.player
    state.activeMayIRequester = None

class Actions(Enum):
  PASS = PassAction
  