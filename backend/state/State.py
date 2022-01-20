
from Card import CardGroup, CardFactory

class State:
  def __init__(self, num_players: int):
    self.players = [None] * num_players
    self.activePlayerIndex = 0
    self.activePlayer = self.players[0]
    self.activeMayIRequester = None
    self.mayIRequestWinner = None
    self.turn = 0
    self.round = 0

  def setup(self):
    # Deck setup
    self.deck: CardGroup = CardGroup(CardFactory.generateDeckForGame(len(self.players)))
    self.discard: CardGroup = CardGroup([])

    CardFactory.shuffleDeck(self.deck.cards)
    self.dealCards(0)
    for i in self.players:
      print(i.name)
      i.hand.printCards()

  def dealCards(self, round: int):
    if(round == 0):
      for i in range(len(self.players) * 10):
        self.players[i % len(self.players)].hand.cards.append(self.deck.cards.pop(0))

  def getIndexOfPlayer(self, player):
    i = 0
    for p in self.players:
      if(p.name == player.name):
        return i
      i += 1
  