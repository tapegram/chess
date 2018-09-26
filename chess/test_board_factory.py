import itertools

from .board import Board
from .board_factory import BoardFactory
from .pieces import (
    Pawn,
    Rook,
    Knight,
    Bishop,
    Queen,
    King,
)
from .coordinate import Coordinate

from unittest import TestCase


class TestBoardFactory(TestCase):

    def test_create_new(self):
        board = BoardFactory().create_new()

        self.assertIsInstance(board, Board)

        piece = board.get_piece_at(Coordinate("a8"))
        self.assertIsInstance(piece, Rook)

        piece = board.get_piece_at(Coordinate("b8"))
        self.assertIsInstance(piece, Knight)

        piece = board.get_piece_at(Coordinate("c8"))
        self.assertIsInstance(piece, Bishop)

        piece = board.get_piece_at(Coordinate("d8"))
        self.assertIsInstance(piece, Queen)

        piece = board.get_piece_at(Coordinate("e8"))
        self.assertIsInstance(piece, King)

        piece = board.get_piece_at(Coordinate("f8"))
        self.assertIsInstance(piece, Bishop)

        piece = board.get_piece_at(Coordinate("g8"))
        self.assertIsInstance(piece, Knight)

        piece = board.get_piece_at(Coordinate("h8"))
        self.assertIsInstance(piece, Rook)

        piece = board.get_piece_at(Coordinate("a7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("b7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("c7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("d7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("e7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("f7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("g7"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("h7"))
        self.assertIsInstance(piece, Pawn)


        empty_ranks = range(3, 7)
        empty_files = "abcdefgh"

        for file, rank in itertools.product(empty_files, empty_ranks):
            self.assertIsNone(
                board.get_piece_at(
                    Coordinate("{}{}".format(file, rank))))

        piece = board.get_piece_at(Coordinate("a2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("b2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("c2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("d2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("e2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("f2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("g2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("h2"))
        self.assertIsInstance(piece, Pawn)

        piece = board.get_piece_at(Coordinate("a1"))
        self.assertIsInstance(piece, Rook)

        piece = board.get_piece_at(Coordinate("b1"))
        self.assertIsInstance(piece, Knight)

        piece = board.get_piece_at(Coordinate("c1"))
        self.assertIsInstance(piece, Bishop)

        piece = board.get_piece_at(Coordinate("d1"))
        self.assertIsInstance(piece, King)

        piece = board.get_piece_at(Coordinate("e1"))
        self.assertIsInstance(piece, Queen)

        piece = board.get_piece_at(Coordinate("f1"))
        self.assertIsInstance(piece, Bishop)

        piece = board.get_piece_at(Coordinate("g1"))
        self.assertIsInstance(piece, Knight)

        piece = board.get_piece_at(Coordinate("h1"))
        self.assertIsInstance(piece, Rook)
