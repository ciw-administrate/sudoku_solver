from app.sudoku_solver import SudokuSolver
import unittest


class TestSudokuSolver(unittest.TestCase):
    def test_nothing_test_returns_true(self):
        expected_value = True
        self.assertEqual(SudokuSolver.solve(), expected_value)
