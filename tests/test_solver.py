import pytest

from sudoku_solver_py.solver import solve, get_possible_values, Square


@pytest.mark.parametrize(
    'square, expected_solved_square',
    [
        [
            [
                [0, 0, 0, 0, 6, 0, 7, 0, 0],
                [0, 5, 9, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0],
                [6, 0, 0, 5, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 0, 4, 6, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 9, 1],
                [8, 0, 0, 7, 4, 0, 0, 0, 0]
            ],

            [
                [2, 3, 8, 9, 6, 5, 7, 1, 4],
                [7, 5, 9, 4, 1, 3, 6, 8, 2],
                [4, 1, 6, 2, 7, 8, 9, 5, 3],
                [9, 4, 5, 1, 3, 6, 2, 7, 8],
                [6, 8, 7, 5, 2, 4, 1, 3, 9],
                [3, 2, 1, 8, 9, 7, 4, 6, 5],
                [1, 6, 2, 3, 5, 9, 8, 4, 7],
                [5, 7, 4, 6, 8, 2, 3, 9, 1],
                [8, 9, 3, 7, 4, 1, 5, 2, 6],
            ]
        ]
    ]
)
def test_solver(square: Square, expected_solved_square: Square):
    # act
    solve(square)

    # arrange
    assert square == expected_solved_square


@pytest.mark.parametrize(
    'column, row, expected_values',
    [
        [1, 1, [2, 4, 7]],
        [3, 0, [2, 6]],
    ]
)
def test_get_possible_values(column, row, expected_values):
    # arrange
    square = [
        [5, 3, 1, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    # act
    values = get_possible_values(column=column, row=row, square=square)

    # arrange
    assert values == expected_values
