from typing import Iterable
from .board import Board

class Player(object):
    def __init__(self) -> None:
        self.name = None
        self.board = None


    def get_name_from_player(self,other_player: Iterable["Player"])->str:
        already_used_names = set([player.name for player in other_player])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has been used. Pick another name.')


    def __str__(self) -> str:
        return self.name

