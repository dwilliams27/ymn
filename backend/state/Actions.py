from abc import ABC, abstractmethod
from enum import Enum;
from colorama import Fore, Style

from Card import CardFactory
from . import State

class Action(ABC):
  def __init__(self, player):
    self.player = player

  @abstractmethod
  def transform(self, state: State) -> None:
    pass

class DrawPile(Enum):
  DECK = 'Deck'
  DISCARD = 'Discard pile'

class ActionList(Enum):
  Pass = 'PassAction'
  ChangeActivePlayer = 'ChangeActivePlayerAction'
  DrawDeckCard = 'DrawDeckCardAction'
  DrawDiscardCard = 'DrawDiscardCardAction'
  AskMayI = 'AskMayIAction'
  ApproveMayIRequest = 'ApproveMayIRequestAction'
  DenyMayIRequest = 'DenyMayIRequestAction'
  RewardPlayerWithMayI = 'RewardPlayerWithMayIAction'


class PassAction(Action):
  def transform(self, state: State):
    pass

class ChangeActivePlayerAction(Action):
  def __init__(self, newIndex: int):
    self.newIndex = newIndex

  def transform(self, state: State):
    state.activePlayer = state.players[self.newIndex]
    state.activePlayerIndex = self.newIndex

class DrawDeckCardAction(Action):
  def __init__(self, player):
    self.playerIndex = player.playerIndex
    self.player = player

  def transform(self, state: State):
    if(len(state.deck.cards) == 0):
      state.deck.cards.append(state.discard.cards)
      CardFactory.shuffleDeck(state.deck.cards)
      state.discard.cards = []
    state.players[self.playerIndex].hand.cards.append(state.deck.cards.pop(0))
    print(f'{self.player.getPrintableName()} draws a card from the {Fore.MAGENTA}Deck{Style.RESET_ALL}')

class DrawDiscardCardAction(Action):
  def __init__(self, player):
    self.playerIndex = player.playerIndex
    self.player = player

  def transform(self, state: State):
    if(len(state.discard.cards) == 0):
      print('Cannot draw from empty discard pile')
      raise
    state.players[self.playerIndex].hand.cards.append(state.discard.cards.pop(0))
    print(f'{self.player.getPrintableName()} draws a card from the {Fore.MAGENTA}Discard pile{Style.RESET_ALL}')

class AskMayIAction(Action):
  def transform(self, state: State):
    if(state.activeMayIRequester != None):
      print('Another player already has an active May I request')
      raise
    state.activeMayIRequester = self.player

class ApproveMayIRequestAction(Action):
  def transform(self, state: State):
    pass

class DenyMayIRequestAction(Action):
  def transform(self, state: State):
    state.mayIRequestWinner = self.player
    state.activeMayIRequester = None

class RewardPlayerWithMayIAction(Action):
  def transform(self, state: State):
    DrawDeckCardAction(self.player).transform(state)
    DrawDiscardCardAction(self.player).transform(state)
    self.player.mayIs += 1
    state.mayIRequestWinner = self.player
    state.activeMayIRequester = None

class DiscardCardAction(Action):
  def __init__(self, player):
    self.playerIndex = player.playerIndex
    self.player = player

  def setCardIndex(self, cardIndex):
    self.cardIndex = cardIndex

  def transform(self, state: State):
    state.discard.cards.insert(0, self.player.hand.cards.pop(self.cardIndex))

class GoDownAction(Action):
  def transform(self, state: State):
    self.player.isDown = True
    pass