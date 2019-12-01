from typing import List


class SudokuSolver(object):
    @staticmethod
    def sum_of_row(solution: List[List[int]], row_number: int) -> int:
        row: List[int] = solution[row_number]
        total: int = 0
        for number in row:
            total += number
        return total

    @staticmethod
    def sum_of_column(solution: List[List[int]], column_number: int) -> int:
        column: List[int] = []
        row: List[int]
        for i in range(len(solution)):
            column.append(solution[i][column_number])
        total: int = 0
        for number in column:
            total += number
        return total
