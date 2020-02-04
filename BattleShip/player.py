from typing import Iterable
from .board import Board

class Player(object):
    def __init__(self,other_players: Iterable["Player"] ,Board: object, Board2: object) -> None:
        self.name = self.get_name_from_player(other_players)
        self.board_own = Board
        self.board_scan = Board2

        self.coordinates = Board
    def create_own_board(self):
        pass

    def get_name_from_player(self,other_player: Iterable["Player"])->str:
        already_used_names = set([player.name for player in other_player])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has been used. Pick another name.')

    def get_coordinates_from_player(self, other_player: Iterable["Player"]) -> int:
        already_used_coordinates = set([player.coordinates for player in other_player])
        while True:
            name = input('Please enter your name: ')
            if name not in already_used_coordinates:
                return self.coordinates
            else:
                print(f'{self.coordinates} has been used. Pick another name.')
    def __str__(self) -> str:
        return self.name