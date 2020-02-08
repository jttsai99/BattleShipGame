from typing import Iterable
from .board import Board
from .ship import Ship
import sys

class Player(object):
    def __init__(self,other_players: Iterable["Player"],num_rows:int,num_cols:int,count, blank_char: str= "*") -> None:
        self.shipconfig = self.read_config()        #reads config file and return [["Mouse",'1'],....]
        self.count = count
        self.name = self.get_name_from_player(other_players)#gets player name
        self.board = Board(num_rows,num_cols,blank_char)    #initializes player's own board
        self.display_own_board()
        self.scanningboard = Board(num_rows,num_cols,blank_char)
        self.return_ship_names(self.shipconfig)  #get a list of shipName
        self.return_ship_initials(self.shipconfig) #get a list of shipInitials
        self.return_ship_lengths(self.shipconfig)   #get a list of shipLengths
        self.owned_ships = []   #creates a list for player's Owned ships
        for i in range(len(self.shipconfig)):       #iterates the config specified amount of time eg: how many ships there
            self.orientation = self.get_orientation(i)   #gets ship orientation by user input returns string
            self.coordinates = self.get_starting_coordinates(i)  #get coordinates by user input return tuple
            self.owned_ships.append(
                Ship(self.shipnames[i],self.shipinitials[i], int(self.shiplengths[i]), self.orientation, self.coordinates))
            #appends each ship to Owned Ship list by giving (name,initals,length,orientation,coordinates)


            #places the ships on the board
            self.board.place_ship_on_board(self.owned_ships[i].ship_coordinates,self.owned_ships[i].get_ship_marker())
            #displays the own board
            self.display_own_board()

        #print(self.get_player_name())

        ##prints out the ship infos
        #print("hello bobo1: ", self.owned_ships[0])
        #print("hello bobo2: ", self.owned_ships[1])
        #print("hello bobo3: ", self.owned_ships[2])


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
        #print(shipconfig)
        return shipconfig

#ask player for their name
    def get_name_from_player(self,other_player: Iterable["Player"])->str:
        already_used_names = set([player.name for player in other_player])
        while True:

            name = input('Player {} please enter your name: '.format(self.count))
            if name not in already_used_names:
                return name
            else:
                print(f'{name} has been used. Pick another name.')

#get coordinates
#ask for coordinates from player
    def get_starting_coordinates(self,i)->tuple:
        coords = input(
            "{}, enter the starting position for your {} ship, which is {} long, in the form row, column: ".format(self.name,self.shipnames[i],self.shiplengths[i]))
        splitcoords = coords.split(sep=',')
        x= int(splitcoords[0])
        y= int(splitcoords[1])
        self.coordinates = (x,y)
        return self.coordinates


#ask for orientation from player,
    def get_orientation(self,i) -> str:
        self.orientation = input("{} enter horizontal or vertical for orientation of {} which is {} long: ".format(self.name,self.shipnames[i],self.shiplengths[i]))
        if self.orientation.lower() in "horizontal":
            self.orientation = "horizontal"
        elif self.orientation.lower() in "vertical":
            self.orientation = "vertical"
        while self.orientation.lower() not in "horizontal" and self.orientation.lower() not in "vertical":
            print(self.orientation, "does not represent an Orientation")
            self.orientation = input("{} enter horizontal or vertical for orientation of {} which is {} long: ".format(self.name,self.shipnames[i],self.shiplengths[i]))
            if self.orientation.lower() in "horizontal":
                self.orientation = "horizontal"
            elif self.orientation.lower() in "vertical":
                self.orientation = "vertical"
        return self.orientation












# converts our list of lists to a list of shipnames
    def return_ship_names(self,list):
        self.first=[]
        self.shipnames = []
        for i in list:
            for j in i:
                self.first.append(j)
        for i in range(len(self.first)):
            if i %2 ==0:
                self.shipnames.append(self.first[i])
        #print(self.shipnames)
        return self.shipnames

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
        #print(self.shipinitials)
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
        #print(self.shiplengths)
        return self.shiplengths


#display player's Placement Board
    def display_own_board(self):
        #print("{}'s Placement Board".format(self.name))
        print("{}'s Placement Board".format(self.name))
        print(self.board)

    #get the player's name
    def get_player_name(self):
        return self.name

#####################################################################################
#beginning gameplay methods

    def get_shot_input(self)->tuple:
        self.ishot = input("{}, enter the location you want to fire at in the form row, column:".format(self.name))
        self.x,self.y = self.ishot.split(sep=",")
        self.inputshot = (int(self.x),int(self.y))
        # print(type(self.x))
        # print(type(self.y))
        return self.inputshot

    # must replace other.board and p2 bc idk actual variable names for opponent and opponent's board
    # also check destroy is not working properly
    # other = get opposite player's board
    def check_shot_hit_miss(self,other)->str:
        self.status =""
        if other.board[int(self.x)][int(self.y)]== "*":
            other.board[int(self.x)][int(self.y)]="O"
            self.status = "Miss"
            print(self.status)
            return self.status



        elif other.board[int(self.x)][int(self.y)] != "*" and other.board[int(self.x)][int(self.y)] != "X" and other.board[int(self.x)][int(self.y)] != "O":
            for i in self.shipnames: #["Mouse","Cat","Dog"]
                self.hitshipname = i
                if other.board[int(self.x)][int(self.y)]==self.hitshipname[0]:
                    other.board[int(self.x)][int(self.y)] = "X"
                    if self.check_destroy(other) == False:
                        self.status = ("You hit {}'s {}!".format(other,self.hitshipname))
                        print(self.status)
                        return self.status

                    elif self.check_destroy(other) == True:
                        self.status = ("You hit {}'s {}! You destroyed {}'s {}".format(other,self.hitshipname,other,self.hitshipname))
                        print(self.status)
                        return self.status

#Player' object has no attribute 'hitshipname'
    #other = get opposite player's board
    def check_destroy(self,other):
        for ship in self.shipnames:
            if ship == self.hitshipname:
                destroylist = []
                for t in other.owned_ships[0].list_coords:
                    destroylist.append(other.board[t[0]][t[1]])
                if self.hitshipname[0] in destroylist:
                    return False
                if self.hitshipname[0] not in destroylist:
                    return True



# this is giving us "NoneType is not iterable"
    #
    def add_to_scanningboard(self):
        if self.status == "Miss":
            self.scanningboard[int(self.x)][int(self.y)] = "O"
        if "hit" in self.status:
             self.scanningboard[int(self.x)][int(self.y)] = "X"
        return self.scanningboard
