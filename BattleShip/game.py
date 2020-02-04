from typing import Iterable, TypeVar
from .board import Board
from .player import Player

class BattleShipGame(object):
    def __init__(self,dimensions:int,dimensions2:int, blank_char: str= "*") -> None:
        self.blank_char = blank_char
        self.board = Board(dimensions,dimensions2,blank_char)
        self.players = [Player() for _ in range(2)]
        self._cur_player_turn = 0

    def setup(self)->None:
        pass
    def play(self)-> None:
        while not self.is_game_over():
            self.display_game_state()
            cur_player.take_turn()
            self.change_turn()
        self.display_the_winner()

    def display_game_state(self)-> None:
        print(self.board)
        pass

    def is_game_over(self):
        return self.someone_won()

    def someone_won(self)->bool:
        return self.guessed_all()

    def change_turn(self)-> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

    def get_cur_player(self)-> "Player":
        return self.players[self._cur_player_turn]
        pass

    def guessed_all(self):
        #the list of tuples of coordinates are all Xs
        pass