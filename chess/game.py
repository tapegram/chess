class Game(object):

    def __init__(self, board, is_white_turn=True):
        self._board = board
        self._is_white_turn = is_white_turn

    def can_make_move(self, coord_start, coord_end):
        pass

    def make_move(self, coord_start, coord_end):
        pass
