from typing import Iterable
from .board import Board
from .ship import Ship
import sys

class Player(object):
    def __init__(self,other_players: Iterable["Player"],num_rows:int,num_cols:int, blank_char: str= "*") -> None:
        self.shipconfig = self.read_config()
        self.name = self.get_name_from_player(other_players)
        self.board = Board(num_rows,num_cols,blank_char)
        self.return_ship_name(self.shipconfig)
        self.return_ship_initials(self.shipconfig)
        self.return_ship_lengths(self.shipconfig)
        self.owned_ships = []
        for i in range(len(self.shipconfig)):
            self.orientation = self.get_orientation()
            self.coordinates = self.get_starting_coordinates()
            self.owned_ships.append(
                Ship(self.shipname[i],self.shipinitials[i], int(self.shiplengths[i]), self.orientation, self.coordinates))
            self.display_own_board()

        print("hello bobo1: ", self.owned_ships[0])
        print("hello bobo2: ", self.owned_ships[1])
        print("hello bobo3: ", self.owned_ships[2])


    def __str__(self) -> str:
        return self.name


#reads the config file (returns a list of list)
    def read_config(self) -> list:
        file_path = open(sys.argv[1])
        num_rows, num_cols = file_path.readline().split()
        # print(num_rows, num_cols)
        line = file_path.readline()
        shipconfig = []
        while line != "":
            name, length = line.split()
            shipconfig.append([name, length])
            line = file_path.readline()
        print(shipconfig)
        return shipconfig

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
    def get_starting_coordinates(self)->tuple:
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

    def return_ship_name(self,list):
        self.first=[]
        self.shipname = []
        for i in list:
            for j in i:
                self.first.append(j)
        for i in range(len(self.first)):
            if i %2 ==0:
                self.shipname.append(self.first[i])
        print(self.shipname)
        return self.shipname

#converts our list of lists to a list of first letters
    def return_ship_initials(self,list):
        self.second=[]
        self.shipinitials = []
        for i in list:
            for j in i:
                self.second.append(j[0])
        for i in range(len(self.second)):
            if i %2 ==0:
                self.shipinitials.append(self.second[i])
        print(self.shipinitials)
        return self.shipinitials

#converts our list of lists to a list of ship lengths
    def return_ship_lengths(self,list):
        self.third=[]
        self.shiplengths = []
        for i in list:
            for j in i:
                self.third.append(j[0])
        for i in range(len(self.third)):
            if i %2 ==1:
                self.shiplengths.append(self.third[i])
        print(self.shiplengths)
        return self.shiplengths

    def create_ship_objects(self):
        pass

    def display_own_board(self):
        print(self.board)

#####################################################################################
#beginning gameplay methods

    def get_shot_input(self):
        self.inputshot = input(p1", enter the location you want to fire at in the form row, column:",sep = "")
        self.x,self.y=self.inputshot.split(sep=",")
        return (int(self.x),int(self.y))

    # must replace other.board and p2 bc idk actual variable names for opponent and opponent's board
    #also check destroy is not working properly
    def check_shot_hit_miss(self):
        if other.board[self.x][self.y]=="*":
            other.board[self.x][self.y]="O"
            return "Miss"
        elif other.board[self.x][self.y] != "*" and other.board[self.x][self.y] != "X" and other.board[self.x][self.y] != "O":
            for i in self.shipname:
                if other.board[self.x][self.y]==i[0]:
                    other.board[self.x][self.y] = "X"
                    return "You hit {}'s {}!".format(p2,i)

    def check_destroy(self):
        pass
