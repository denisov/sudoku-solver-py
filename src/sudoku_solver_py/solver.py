import copy
from dataclasses import dataclass

from typing import TypeAlias


@dataclass
class PossibleValues:
    """Возможные значения в данной ячейке"""
    column: int
    row: int
    values: list[int]


Square: TypeAlias = list[list[int]]


def solve(square: Square) -> bool:
    """Решает судоку."""
    while True:
        cell_with_min_possible_values = _get_cell_with_min_possible_values(square)
        if cell_with_min_possible_values is None:
            return True
        if len(cell_with_min_possible_values.values) == 1:
            column = cell_with_min_possible_values.column
            row = cell_with_min_possible_values.row
            square[row][column] = cell_with_min_possible_values.values[0]
            continue
        if len(cell_with_min_possible_values.values) == 0:
            return False
        if len(cell_with_min_possible_values.values) > 1:
            break

    for v in cell_with_min_possible_values.values:
        square_copy = copy.deepcopy(square)
        square_copy[cell_with_min_possible_values.row][cell_with_min_possible_values.column] = v
        if solve(square_copy):
            for row in range(9):
                for column in range(9):
                    square[row][column] = square_copy[row][column]
            return True


def get_possible_values(column, row, square: Square) -> list[int]:
    """Возвращает возможные значения для данной ячейки"""
    values = {v for v in range(1, 10)}
    # значения строки
    values -= set(square[row])
    # значения столбца
    values -= set([square[_y][column] for _y in range(9)])
    # значения из под-квадрата
    values -= set(_get_values_from_subsquare(square=square, column_start=(column // 3) * 3, row_start=(row // 3) * 3))

    return list(values)


def _get_cell_with_min_possible_values(square: Square) -> PossibleValues | None:
    """Возвращает ячейку с наименьшим числом возможных значений"""
    possible_values: PossibleValues | None = None
    for row in range(9):
        for column in range(9):
            if square[row][column] != 0:
                continue
            possible_values_candidate = get_possible_values(column=column, row=row, square=square)
            if possible_values is None or len(possible_values_candidate) < len(possible_values.values):
                possible_values = PossibleValues(
                    values=possible_values_candidate,
                    column=column,
                    row=row,
                )
    return possible_values


def _get_values_from_subsquare(square: Square, column_start: int, row_start: int, size=3):
    """Возвращает значения из под-квадрата """
    values = []
    for row in range(row_start, row_start + size):
        for column in range(column_start, column_start + size):
            values.append(square[row][column])
    return values
