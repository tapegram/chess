from .board import Board
from .pieces import *


class BoardFactory(object):

    def create_new(self):
        grid = [
            [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()],
            [Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()],
            [Rook(), Knight(), Bishop(), King(), Queen(), Bishop(), Knight(), Rook()],
        ]
        return Board(grid=grid)
