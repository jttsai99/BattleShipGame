from typing import Iterable
from .board import Board

class Player(object):
    def __init__(self,other_players: Iterable["Player"],num_rows:int,num_cols:int, blank_char: str= "*") -> None:
        self.name = self.get_name_from_player(other_players)
        self.board = Board(num_rows,num_cols,blank_char)
        self.ownedships = []


    def get_name_from_player(self,other_player: Iterable["Player"])->str:
        already_used_names = set([player.name for player in other_player])
        while True:
            name = input('Player please enter your name: ')
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has been used. Pick another name.')

    #def get_coordinates_from_player(self, other_player: Iterable["Player"]) -> int:
        # already_used_coordinates = set([player.coordinates for player in other_player])
        # while True:
        #     name = input('Please enter your name: ')
        #     if name not in already_used_coordinates:
        #         return self.coordinates
        #     else:
        #         print(f'{self.coordinates} has been used. Pick another coordinate.')

    def ship_coordinates(self)->tuple:
        coords = input(
            "Please give the coordinates where you would like to place the ship in row,column form."'\n')
        splitcoords = coords.split(sep=',')
        x= int(splitcoords[0])
        y= int(splitcoords[1])
        coordinates = (x,y)
        return coordinates

    def __str__(self) -> str:
        return self.name

    def get_orientation(self) -> str:
            self.orientation = str(input("Do you want your ship to be placed horizontal or vertical?"))
            while self.orientation not in "horizontal" or self.orientation not in "vertical":
                 print("ERROR: Your response must be a prefix of 'horizontal' or 'vertical'.")
                 self.orientation = str(input("Do you want your ship to be placed horizontal or vertical?"))
            return self.orientation


Ship(name,length)