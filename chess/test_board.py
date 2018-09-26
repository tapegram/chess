from .board import Board
from .coordinate import Coordinate
from .pieces import Queen

from unittest import TestCase


class TestBoard(TestCase):

    def test_get_piece_at(self):
        board = Board(grid=[[Queen()]])
        self.assertIsInstance(
            board.get_piece_at(Coordinate("a8")), Queen)
