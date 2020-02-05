from . import player
from . import board

Board = board.Board

class MoveError(Exception):
    ...



class Move(object):
    def __init__(self, maker: "player.Player", row: int, col: int) -> None:
        self.maker = maker
        self.row = row
        self.col = col

    @classmethod
    def from_str(cls, maker: "player.Player", str_move: str) -> "Move":
        """

        :param maker:
        :param str_move: should be in the form row, col
        :return:
        """

        try:
            row, col = str_move.split(',')
        except ValueError:
            raise MoveError(f'{str_move} is not in the form row, col')

        try:
            row = int(row)
        except ValueError:
            raise MoveError(f'row needs to be an integer. {row} is not an integer')

        try:
            col = int(col)
        except ValueError:
            raise MoveError(f'col needs to be an integer. {col} is not an integer')

        return cls(maker, row, col)

    def make(self, the_board: "board.Board"):
        if not the_board.is_in_bounds(self.row, self.col):
            raise MoveError(f'{self.row}, {self.col} is not in bounds')
        elif the_board[self.row][self.col] != the_board.blank_char:
            raise MoveError(f"You can't play at {self.row}, {self.col} because someone already played there")
        else:
            the_board[self.row][self.col] = self.maker.piece
