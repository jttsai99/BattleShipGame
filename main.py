import sys
from BattleShip.game import BattleShipGame
from BattleShip.get_ship import Get_Ship
if __name__ == '__main__':
    input_file = open(sys.argv[1])
    num_rows,num_cols = input_file.readline().split()
    #print(num_rows,num_cols)
    game= BattleShipGame(int(num_rows),int(num_cols))
    game.start()