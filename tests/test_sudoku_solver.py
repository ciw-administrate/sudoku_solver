from app.sudoku_solver import SudokuSolver
import unittest


class TestSudokuSolver(unittest.TestCase):
    puzzle_one = [
        [2, 1, 9, 3, 7, 6, 4, 5, 0],
        [5, 0, 0, 0, 8, 0, 9, 0, 1],
        [4, 6, 0, 5, 0, 1, 0, 3, 7],
        [1, 4, 6, 0, 2, 0, 5, 0, 3],
        [0, 8, 0, 1, 0, 5, 6, 0, 9],
        [9, 0, 2, 6, 3, 8, 0, 1, 4],
        [0, 9, 5, 0, 1, 4, 3, 7, 2],
        [3, 2, 0, 9, 5, 7, 0, 4, 6],
        [8, 7, 0, 0, 0, 3, 0, 0, 5]
    ]

    solution_one = [
        [2, 1, 9, 3, 7, 6, 4, 5, 8],
        [5, 3, 7, 4, 8, 2, 9, 6, 1],
        [4, 6, 8, 5, 9, 1, 2, 3, 7],
        [1, 4, 6, 7, 2, 9, 5, 8, 3],
        [7, 8, 3, 1, 4, 5, 6, 2, 9],
        [9, 5, 2, 6, 3, 8, 7, 1, 4],
        [6, 9, 5, 8, 1, 4, 3, 7, 2],
        [3, 2, 1, 9, 5, 7, 8, 4, 6],
        [8, 7, 4, 2, 6, 3, 1, 9, 5]
    ]

    def test_sum_of_first_row_equals_45(self):
        expected_value = 45
        sum_of_first_row = SudokuSolver.sum_of_row(TestSudokuSolver.solution_one, 0)
        self.assertEqual(sum_of_first_row, expected_value)

    def test_sum_of_first_column_equals_45(self):
        expected_value = 45
        sum_of_first_column = SudokuSolver.sum_of_column(TestSudokuSolver.solution_one, 0)
        self.assertEqual(sum_of_first_column, expected_value)

    def test_first_row_contains_each_number_from_1_to_9(self):
        expected_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sorted_row = SudokuSolver.sort_row(TestSudokuSolver.solution_one, 0)
        self.assertEqual(expected_value, sorted_row)
