import unittest

from Card import CardFactory, Card

class TestCard(unittest.TestCase):
  def genCard(self, name):
    return Card(name, 0, None)

  def test_r1_win(self):
    hand = [self.genCard('2'), self.genCard('2'), self.genCard('2'), self.genCard('2'), \
      self.genCard('3'), self.genCard('3'), self.genCard('3'), self.genCard('3'), \
      self.genCard('4'), self.genCard('4'), self.genCard('4'), self.genCard('4')]
    self.assertTrue(CardFactory.canGoDownR1(hand))

  def test_r1_lose(self):
    hand = [self.genCard('2'), self.genCard('2'), self.genCard('2'), self.genCard('2'), \
      self.genCard('3'), self.genCard('3'), self.genCard('3'), self.genCard('3'), \
      self.genCard('4'), self.genCard('4'), self.genCard('5'), self.genCard('5')]
    self.assertFalse(CardFactory.canGoDownR1(hand))