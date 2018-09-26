class Board(object):

    def __init__(self, grid):
        self._grid = grid

    def get_piece_at(self, coord):
        return self._grid[coord.rank_idx][coord.file_idx]
