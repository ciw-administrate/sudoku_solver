from typing import List


class SudokuSolver(object):
    @staticmethod
    def sum_of_row(solution: List[List[int]], row_number: int) -> int:
        row: List[int] = solution[row_number]
        total: int = 0
        for number in row:
            total += number
        return total
