from .player import Player
import sys

class BattleShipGame(object):
    def __init__(self,num_rows:int,num_cols:int, blank_char: str= "*") -> None:
        self.read_config()  #read the config file and got a dictionary {'name', length}
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.blank_char = blank_char
        self._cur_player_turn = 0
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players,num_rows,num_cols, blank_char))
            #self.display_own_board()
        self.player1 = self.players[0]
        self.player2 = self.players[1]


#reads the config file (completed)
    def read_config(self)-> list:
        file_path = open(sys.argv[1])
        num_rows, num_cols = file_path.readline().split()
        #print(num_rows, num_cols)
        line = file_path.readline()
        self.shipconfig = []
        while line != "":
            name, length = line.split()
            self.shipconfig.append([name,length])
            line = file_path.readline()
        #print(self.shipconfig)
        return self.shipconfig

#Actually Playing the Game
    def play(self)-> None:
        while not self.someone_won():
            self.getting_shipconfig_info()
            self.display_own_board()
            self._cur_player.take_turn()
            #self.change_turn()
        #self.display_the_winner()
        pass

#display the current player's own board
    def display_own_board(self)-> None:
        print(self.get_cur_player().board)

#display the opponent's board (current player's scanning board)
    def display_scanning_board(self)->None:
        #print(self.scanningboard)
        pass

#changes player's turn
    def change_turn(self)-> None:
        self._cur_player_turn = (self._cur_player_turn + 1) % 2

#identify the current player
    def get_cur_player(self)-> "Player":
        return self.players[self._cur_player_turn]
        pass


#someone wins and prints somthing
    def someone_won(self)->bool:
        return self.guessed_all()

#someone guess all opponent ship coordinates
    def guessed_all(self)->bool:
        #the list of tuples of coordinates are all Xs
        return True
        pass


#getting cooridnates into tuples
    def ship_coordinates(self)->tuple:
        coords = input(
            "Please give the coordinates where you would like to place the ship in row,column form."'\n')
        splitcoords = coords.split(sep=',')
        x= int(splitcoords[0])
        y= int(splitcoords[1])
        coordinates = (x,y)
        return coordinates