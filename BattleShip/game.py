from .player import Player
import sys

class BattleShipGame(object):
    def __init__(self,num_rows:int,num_cols:int, blank_char: str= "*") -> None:
        self.read_config()  #read the config file and got a dictionary {'name', length}
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.blank_char = blank_char
        self.current_player_index = 0
        self.opponent_player_index = 1
        self.players = []
        for player_num in range(2):
            self.players.append(Player(self.players,num_rows,num_cols, blank_char))
            #self.display_own_board()
        #print("{}'s Scanning Board: \n{}".format(self.players[self.current_player_index], self.display_scanning_board()))
        #print("{}'s Board: \n{}".format(self.players[self.current_player_index],self.display_own_board()))


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
        while True:
            self.display()
            self.get_cur_player().get_shot_input()
            self.get_cur_player().check_shot_hit_miss(self.get_other_player())
            #self.get_cur_player().add_to_scanningboard(self.get_other_player())
            self.change_turn()
        #self.display_the_winner()
        pass


#Printing Both Boards with Format
    def display(self):
        print("{}'s Scanning Board: \n{}".format(self.players[self.current_player_index], self.display_scanning_board()))
        print("{}'s Board: \n{}".format(self.players[self.current_player_index], self.display_own_board()))

#Display the current player's own board
    def display_own_board(self)-> None:
        return self.get_cur_player().board

#Identify the current player
    def get_cur_player(self) -> "Player":
        return self.players[self.current_player_index]

#Identify the opponent player
    def get_other_player(self) -> "Player":
        return self.players[self.opponent_player_index]

#display the opponent's board (current player's scanning board)
    def display_scanning_board(self)->None:
        return self.get_cur_player().scanningboard


# #changing the turn
#     def current_player(self) -> None:
#         if self.current_player_index == 0:
#             self.current_player_index = 1
#         else:
#             self.current_player_index = 0
#
#
# #opposite player
#     def enemy_player(self) -> None:
#         if self.opponent_player_index == 0:
#             self.opponent_player_index = 1
#         else:
#             self.opponent_player_index = 0

# changes player's turn
    def change_turn(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % 2
        self.opponent_player_index = (self.opponent_player_index + 1) % 2

#someone wins and prints somthing
    def someone_won(self)->bool:
        return self.guessed_all()

#someone guess all opponent ship coordinates
    def guessed_all(self)->bool:
        #the list of tuples of coordinates are all Xs
        return True
        pass