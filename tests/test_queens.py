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

    def test_queen_is_empty_originally(self):
        state = QueensState(8,8)
        self.assertEqual(state.queens(), second = [])

    def test_queen_false_originally(self):
        state = QueensState(8,8)
        self.assertEqual(state.has_queen(Position(2,3)),second = False)

    def test_with_queens_amend(self):
        state = QueensState(8,8)
        state = state.with_queens_added([Position(0, 3), Position(3,5), Position(7,6)])

    def test_with_queens_added_duplicate(self):
        state = QueensState(8, 8)
        state = state.with_queens_added([Position(0,3), Position(3,5), Position(7,6)])
        self.assertRaises(DuplicateQueenError, state.with_queens_added, [Position(7,6)])

    def test_with_queens_removed(self):
        state = QueensState(8, 8)
        state = state.with_queens_added([Position(0,3), Position(3,5), Position(7,6), Position(7,7)])
        state = state.with_queens_removed([Position(3,5), Position(7,6)])
        self.assertEqual(state.queen_count(), 2)
        self.assertEqual(state.queens(), [Position(0,3), Position(7,7)])
        self.assertEqual(state.has_queen(Position(7,6)), False)
        self.assertEqual(state.has_queen(Position(7,7)), True)

    def test_with_queens_removed_missing(self):
        state = QueensState(8, 8)
        self.assertRaises(MissingQueenError, state.with_queens_removed, [Position(7,6), Position(7,7)])

    def test_any_queens_unsafe_true(self):
        state = QueensState(8, 8)
        state = state.with_queens_added([Position(0,3), Position(3,5), Position(7,6), Position(7,7)])
        self.assertEqual(state.any_queens_unsafe(), True)

    def test_any_queens_unsafe_false_1(self):
        state = QueensState(8, 8)
        state = state.with_queens_added([Position(0,0), Position(1,2)])
        self.assertEqual(state.any_queens_unsafe(), False)

    def test_any_queens_unsafe_false_2(self):
        state = QueensState(8, 8)
        state = state.with_queens_added([Position(0,0), Position(1,2), Position(2,4)])
        self.assertEqual(state.any_queens_unsafe(), False)



if __name__ == '__main__':
    unittest.main()
