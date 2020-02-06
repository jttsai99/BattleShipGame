from typing import Iterable
from .board import Board
from .ship import Ship
import sys

class Player(object):
    def __init__(self,other_players: Iterable["Player"],num_rows:int,num_cols:int, blank_char: str= "*") -> None:
        self.shipconfig = self.read_config()
        self.name = self.get_name_from_player(other_players)
        self.board = Board(num_rows,num_cols,blank_char)
        self.return_ship_initials(self.shipconfig)
        self.return_ship_lengths(self.shipconfig)
        self.owned_ships = self.adding_shipobj_to_player_list(orientation = "horizontal",coordinates=(0,0))


    def __str__(self) -> str:
        return self.name


#reads the config file (returns a list of list)
    def read_config(self) -> list:
        file_path = open(sys.argv[1])
        num_rows, num_cols = file_path.readline().split()
        # print(num_rows, num_cols)
        line = file_path.readline()
        self.shipconfig = []
        while line != "":
            name, length = line.split()
            self.shipconfig.append([name, length])
            line = file_path.readline()
        print(self.shipconfig)
        return self.shipconfig

#ask player for their name
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

#get coordinates
#ask for coordinates from player
    def ship_coordinates(self)->tuple:
        coords = input(
            "Please give the coordinates where you would like to place the ship in row,column form."'\n')
        splitcoords = coords.split(sep=',')
        x= int(splitcoords[0])
        y= int(splitcoords[1])
        self.coordinates = (x,y)
        return self.coordinates


#ask for orientation from player
    def get_orientation(self) -> str:
            self.orientation = str(input("Do you want your ship to be placed horizontal or vertical?"))
            return self.orientation
            #while self.orientation not in "horizontal" or self.orientation not in "vertical":
             #    print("ERROR: Your response must be a prefix of 'horizontal' or 'vertical'.")
             #    self.orientation = str(input("Do you want your ship to be placed horizontal or vertical?"))



    # def add_to_owned_ships(self):
    #     file_path = open(sys.argv[1])
    #     num_rows, num_cols = file_path.readline().split()
    #     line = file_path.readline()
    #     self.owned_ships = []
    #     while line != "":
    #         name, length = line.split()
    #         self.owned_ships.append([name, length])
    #         line = file_path.readline()
    #     return


#converts our list of lists to a list of first letters
    def return_ship_initials(self,list):
        self.firsts=[]
        self.shipinitials = []
        for i in list:
            for j in i:
                self.firsts.append(j[0])
        for i in range(len(self.firsts)):
            if i %2 ==0:
                self.shipinitials.append(self.firsts[i])
        print(self.shipinitials)
        return self.shipinitials

#converts our list of lists to a list of ship lengths
    def return_ship_lengths(self,list):
        self.second=[]
        self.shiplengths = []
        for i in list:
            for j in i:
                self.second.append(j[0])
        for i in range(len(self.second)):
            if i %2 ==1:
                self.shiplengths.append(self.second[i])
        print(self.shiplengths)
        return self.shiplengths


#actually making the ship object into a list of objects
    def adding_shipobj_to_player_list(self,orientation,coordinates):
        for i in range(len(self.shipinitials)):
            self.owned_ships.append((Ship(self.shipinitials[i],self.shiplengths[i],self.orientation,self.coordinates)))
        print("hello", self.owned_ships)