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
            self.players.append(Player(self.players,num_rows,num_cols,player_num+1,blank_char))
            #self.display_own_board()
        #print("{}'s Scanning Board: \n{}".format(self.players[self.current_player_index], self.display_scanning_board()))
        #print("{}'s Board: \n{}".format(self.players[self.current_player_index],self.display_own_board()))
        #self.status = self.get_cur_player().check_shot_hit_miss(self.get_other_player())

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
        self.display_current()
        while True:
        #while self.someone_won() != True:
            self.get_cur_player().get_shot_input()
            self.get_cur_player().check_shot_hit_miss(self.get_other_player())
            self.get_cur_player().add_to_scanningboard()
            if self.is_cur_player_winner(self.get_other_player()):
                self.display_current()
                print(f'{self.get_other_player()} won the game!')
                break
            self.display_opponent() #display the other player's board
            self.change_turn()
            #print(self.someone_won())
        # self.display_last()
        #self.display_the_winner()
        #pass

# #First time displaying board
#     def display_first(self):
#         print("{}'s Scanning Board \n{}".format(self.players[self.current_player_index], self.display_scanning_board()))
#         print("{}'s Board \n{}".format(self.players[self.current_player_index], self.display_own_board()))


#Printing Both Boards with Format
    def display_current(self):
        print("{}'s Scanning Board \n{}".format(self.players[self.current_player_index], self.display_scanning_board()))
        print("{}'s Board \n{}".format(self.players[self.current_player_index], self.display_own_board()))


    def display_opponent(self):
        print("{}'s Scanning Board \n{}".format(self.players[self.opponent_player_index], self.display_other_scanning_board()))
        print("{}'s Board \n{}".format(self.players[self.opponent_player_index], self.display_enemy_board()))

#Printing last Boards
    def display_last(self):
        print("{}'s Scanning Board \n{}".format(self.players[self.opponent_player_index], self.final_scanning_board()))
        print("{}'s Board \n{}".format(self.players[self.opponent_player_index], self.final_board()))

#Display the current player's own board
    def display_own_board(self):
        return self.get_cur_player().board

#Display the other player's own board
    def display_enemy_board(self):
        return self.get_other_player().board

#Display the other player's scanning board
    def display_other_scanning_board(self)->None:
        return self.get_other_player().scanningboard

# Display current player's scanning board
    def display_scanning_board(self) -> None:
        return self.get_cur_player().scanningboard


#Identify the current player
    def get_cur_player(self) -> "Player":
        return self.players[self.current_player_index]

#Identify the opponent player
    def get_other_player(self) -> "Player":
        return self.players[self.opponent_player_index]



#Final own board
    def final_board(self):
        return self.get_other_player().board

# Final own board
    def final_scanning_board(self):
        return self.get_other_player().scanningboard


# changes player's turn
    def change_turn(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % 2
        self.opponent_player_index = (self.opponent_player_index + 1) % 2

#someone wins and prints somthing
    def someone_won(self)->bool:
        return self.check_win()

    def check_win(self)-> bool:
        self.condition = True
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if self.get_cur_player().board[i][j] != "X" and self.get_cur_player().board[i][j] != "O" and (self.get_cur_player().board[i][j]).isalpha():
                    self.condition = False
                    # print("check win: other's board:\n",self.get_cur_player().board)
                    # print("in the loop:", self.condition)
                    return self.condition
        return self.condition





#display the winner
    def display_the_winner(self)->None:
        self.winner = self.get_other_player()
        # if self.someone_won():
        #     print(f'{self.get_other_player()} won the game!')


    def is_cur_player_winner(self,other)->bool:
        self.condition = True
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if other.board[i][j] != "X" and other.board[i][j] != "O" and (
                        other.board[i][j]).isalpha():
                    self.condition = False
                    # print("check win: other's board:\n",self.get_cur_player().board)
                    # print("in the loop:", self.condition)
                    return self.condition
        return self.condition