from Card import CardGroup

class Player:
  def __init__(self, playerIndex: int):
    self.playerIndex = playerIndex
    self.hand = CardGroup([])
