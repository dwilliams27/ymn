from abc import ABC, abstractmethod
from enum import Enum;
from colorama import Fore, Style

from . import State

class Action(ABC):
  @abstractmethod
  def transform(self, state: State) -> None:
    pass

class DrawPile(Enum):
  DECK = 'Deck'
  DISCARD = 'Discard pile'

class ActionList(Enum):
  Pass = 'PassAction'
  ChangeActivePlayer = 'ChangeActivePlayerAction'
  DrawCard = 'DrawCardAction'
  AskMayI = 'AskMayIAction'
  ApproveMayIRequest = 'ApproveMayIRequestAction'
  DenyMayIRequest = 'DenyMayIRequestAction'
  RewardPlayerWithMayI = 'RewardPlayerWithMayIAction'


class PassAction(Action):
  def __init__(self, player):
    self.player = player

  def transform(self, state: State):
    print(f'{self.player.name} is passing...')
    pass

class ChangeActivePlayerAction(Action):
  def __init__(self, newIndex: int):
    self.newIndex = newIndex

  def transform(self, state: State):
    state.activePlayer = state.players[self.newIndex]
    state.activePlayerIndex = self.newIndex

class DrawCardAction(Action):
  def __init__(self, playerIndex: int, player: str, pile: DrawPile):
    self.playerIndex = playerIndex
    self.pile = pile
    self.player = player

  def transform(self, state: State):
    if(self.pile == DrawPile.DECK):
      state.players[self.playerIndex].hand.cards.append(state.deck.cards.pop(0))
    if(self.pile == DrawPile.DISCARD):
      if(len(state.discard.cards) == 0):
        print('Cannot draw from empty discard pile')
        raise
      state.players[self.playerIndex].hand.cards.append(state.discard.cards.pop(0))
    print(f'{player.getPrintableName()} draws a card from the {Fore.MAGENTA}{self.pile.value}{Style.RESET_ALL}')

class AskMayIAction(Action):
  player = None

  def __init__(self, player):
    self.player = player

  def transform(self, state: State):
    if(state.activeMayIRequester != None):
      print('Another player already has an active May I request')
      raise
    state.activeMayIRequester = self.player

class ApproveMayIRequestAction(Action):
  def transform(self, state: State):
    pass

class DenyMayIRequestAction(Action):
  def __init__(self, player):
    self.player = player

  def transform(self, state: State):
    print()
    state.mayIRequestWinner = self.player
    state.activeMayIRequester = None

class RewardPlayerWithMayIAction(Action):
  def __init__(self, player):
    self.player = player

  def transform(self, state: State):
    DrawCardAction(state.getIndexOfPlayer(self.player), self.player.name, DrawPile.DECK).transform(state)
    DrawCardAction(state.getIndexOfPlayer(self.player), self.player.name, DrawPile.DISCARD).transform(state)
    state.mayIRequestWinner = self.player
    state.activeMayIRequester = None
