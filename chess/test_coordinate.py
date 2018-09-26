from unittest import TestCase
from .coordinate import Coordinate


class TestCoordinate(TestCase):

    def setUp(self):
        self.coordinate = Coordinate("e7")

    def test_init(self):
        self.assertEqual(self.coordinate.rank, "7")
        self.assertEqual(self.coordinate.file, "e")

    def test_rank_idx(self):
        self.assertEqual(self.coordinate.rank_idx, 1)

    def test_file_idx(self):
        self.assertEqual(self.coordinate.file_idx, 4)

