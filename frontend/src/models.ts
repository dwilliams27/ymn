import { Player } from "./player";

export interface Game {
  players: Player[];
  deck: Card[];
  discard: Card[];
}

export interface Suit {
  name: 'hearts' | 'diamonds' | 'spades' | 'clubs';
  color: 'red' | 'black';
}

export interface Card {
  suit: Suit;
  owner: Player;
}
