# test_queens.py
#
# ICS 33 Fall 2023
# Project 0: History of Modern
#
# Unit tests for the QueensState class in "queens.py".
#
# Docstrings are not required in your unit tests, though each test does need to have
# a name that clearly indicates its purpose.  Notice, for example, that the provided
# test method is named "test_zero_queen_count_initially" instead of something generic
# like "test_queen_count", since it doesn't entirely test the "queen_count" method,
# but instead focuses on just one aspect of how it behaves.  You'll want to do likewise.

from queens import QueensState
from collections import namedtuple as nmd
from queens import DuplicateQueenError
from queens import  MissingQueenError
import unittest


Position = nmd(typename =  'position', field_names = ['ro', 'col'])
Position.__doc__ = 'A position on the chessboard, representing the zero-based row and column numbers.'
Position.ro.__doc__ = 'A zero-based row #'
Position.col.__doc__ = 'A zero-based col #'


class TestQueensState(unittest.TestCase):
    def test_queen_count_is_zero_initially(self):
        state = QueensState(8, 8)
        self.assertEqual(state.queen_count(), 0)



if __name__ == '__main__':
    unittest.main()
