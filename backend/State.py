
from Card import CardGroup, CardFactory
from Player import Player

class State:
  def __init__(self, num_players: int):
    self.players = [None] * num_players
    for i in range(num_players):
      self.players[i] = Player(i)
    self.activePlayerIndex = 0
    self.activePlayer = self.players[0]
    self.activeMayIRequester = None
    self.mayIRequestWinner = None
    self.turn = 0
    self.deck: CardGroup = CardGroup(CardFactory.generateDeckForGame(num_players))
    self.discard: CardGroup = CardGroup([])

    self.deck.printCards()
