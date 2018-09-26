from unittest import TestCase
from .piece import Piece
from ..coordinate import Coordinate


class TestPiece(TestCase):

    def test_can_make_move(self):
        with self.assertRaises(NotImplementedError):
            start = Coordinate("a1")
            end = Coordinate("a2")
            Piece().can_make_move(start, end)
