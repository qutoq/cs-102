import unittest
import sys

from src.lab3.sudoku import group, get_row, get_col, get_block , find_empty_positions, find_possible_values, check_solution, generate_sudoku, solve

grid = \
[['5', '3', '.', '.', '7', '.', '.', '.', '.'],
['6', '.', '.', '1', '9', '5', '.', '.', '.'],
['.', '9', '8', '.', '.', '.', '.', '6', '.'],
['8', '.', '.', '.', '6', '.', '.', '.', '3'],
['4', '.', '.', '8', '.', '3', '.', '.', '1'],
['7', '.', '.', '.', '2', '.', '.', '.', '6'],
['.', '6', '.', '.', '.', '.', '2', '8', '.'],
['.', '.', '.', '4', '1', '9', '.', '.', '5'],
['.', '.', '.', '.', '8', '.', '.', '7', '9']]

fake_grid = \
[['1', '2', '3', '1', '2', '3', '1', '2', '3'],
['4', '5', '6', '4', '5', '6', '4', '5', '6'],
['7', '8', '9', '7', '8', '9', '7', '8', '9'],
['1', '2', '3', '1', '2', '3', '1', '2', '3'],
['4', '5', '6', '4', '5', '6', '4', '5', '6'],
['7', '8', '9', '7', '8', '9', '7', '8', '9'],
['1', '2', '3', '1', '2', '3', '1', '2', '3'],
['4', '5', '6', '4', '5', '6', '4', '5', '6'],
['7', '8', '9', '7', '8', '9', '7', '8', '9']]

true_grid = \
[['7', '4', '5', '8', '3', '2', '9', '6', '1'],
['8', '3', '2', '6', '9', '1', '5', '4', '7'],
['9', '6', '1', '5', '7', '4', '2', '8', '3'],
['4', '5', '8', '3', '2', '6', '7', '1', '9'],
['2', '9', '6', '1', '4', '7', '8', '3', '5'],
['3', '1', '7', '9', '5', '8', '6', '2', '4'],
['5', '2', '3', '4', '8', '9', '1', '7', '6'],
['6', '8', '4', '7', '1', '5', '3', '9', '2'],
['1', '7', '9', '2', '6', '3', '4', '5', '8']]


class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2],[3, 4]])
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_get_row(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)), ['4', '.', '6'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)), ['.', '8', '9'])

    def test_get_col(self):
        self.assertEqual(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '4', '7'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)), ['2', '.', '8'])
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])

    def test_get_block(self):
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEqual(get_block(grid, (8, 8)), ['2', '8', '.', '.', '.', '5', '.', '7', '9'])

    def test_find_empty_positions(self):
        self.assertEqual(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0, 2))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))

    def test_find_possible_values(self):
        self.assertEqual(find_possible_values(grid, (0, 2)), {'1', '2', '4'})
        self.assertEqual(find_possible_values(grid, (4, 7)), {'2', '5', '9'})

    def test_check_solution(self):
        self.assertEqual(check_solution(fake_grid), False)
        self.assertEqual(check_solution(true_grid), True)

    def test_solve(self):
        self.assertEqual(check_solution(solve(grid)), True)
        self.assertEqual(check_solution(solve(generate_sudoku(40))), True)
        self.assertEqual(check_solution(solve(generate_sudoku(10))), True)


if __name__ == "__main__":
    unittest.main()