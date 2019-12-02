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
        print("row 0 = " + str(solution[0]))
        column: List[int] = []
        for row_number in range(len(solution)):
            column.append(solution[row_number][column_number])
        total: int = 0
        for number in column:
            total += number
        return total

    @staticmethod
    def sort_row(solution: List[List[int]], row_number: int) -> List[int]:
        row: List[int] = solution[row_number].copy()
        sorted_row: List[int] = []
        for number in range(1, 10):
            if number in row:
                number_index = row.index(number)
                temp_num = row.pop(number_index)
                sorted_row.append(temp_num)
        return sorted_row
