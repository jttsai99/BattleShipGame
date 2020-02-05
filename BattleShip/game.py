from typing import Iterable, TypeVar
from .board import Board
from .player import Player
from .ship import Ship
import sys

class BattleShipGame(object):
    def __init__(self,num_rows:int,num_cols:int, blank_char: str= "*") -> None:
        self.read_config()
        self.num_rows = num_rows
        self.blank_char = blank_char
        self._cur_player_turn = 0
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players,num_rows,num_cols, blank_char))
            self.display_game_state()
        self.shipsconfig = []
        #for ship_num in range(len(self.shipdic)):
        #   self.shipsconfig.append(Ship(self.shipdic[ship_num],self.shipdic[ship_num]))
        for entry, value in self.shipdic.items():
            self.shipsconfig.append([entry,value])
        print(self.shipsconfig)

        #self.players[0].ships

    def read_config(self):
        file_path = open(sys.argv[1])
        num_rows, num_cols = file_path.readline().split()
        print(num_rows, num_cols)
        line = file_path.readline()
        self.shipdic = {}
        while line != "":
            name, length = line.split()
            self.shipdic[name] = length
            line = file_path.readline()
        print(self.shipdic)

        pass
    def play(self)-> None:
        while not self.is_game_over():
            self.display_game_state()
            self.cur_player.take_turn()
            self.change_turn()
        self.display_the_winner()
        pass


    def display_game_state(self)-> None:
        print(self.get_cur_player().board)

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

    def ask_orientation(self)->str:
        userinput = input("enter horizontal or vertical for the orientation: ")
        if userinput == "horizontal":
            return "horizontal"
        elif userinput == "vertical":
            return "vertical"
        else:
            return "enter horizontal or vertical"

    def get_coordinates(self)->tuple:
        userinput = input(" ")