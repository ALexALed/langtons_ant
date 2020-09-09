from collections.abc import Sequence
import statistics
from typing import List


class Validator:
    def __init__(self, grid: "Grid") -> None:
        self._grid = grid

    def validate_grid_length(self) -> bool:
        return self._grid._len_x > 0 and self._grid._len_y > 0

    def validate_grid_form(self) -> bool:

        if not isinstance(self._grid.state, Sequence):
            return False

        if not isinstance(self._grid.state[0], Sequence):
            return False

        return (
            statistics.mean([len(row) for row in self._grid.state]) == self._grid._len_x
        )

    def validate(self) -> bool:
        return self.validate_grid_form() and self.validate_grid_length()


class Grid:
    def __init__(self, initial_state: List[List[bool]]) -> None:
        self._state = initial_state
        self._len_x = 0
        if initial_state and isinstance(initial_state[0], Sequence):
            self._len_x = len(initial_state[0])
        self._len_y = len(initial_state)

    @property
    def state(self) -> List[List[bool]]:
        return self._state

    def get_color(self, x: int, y: int) -> bool:
        return self._state[y][x]

    def change_color(self, x: int, y: int) -> None:
        self._state[y][x] = not self._state[y][x]

    def validate_point(self, x: int, y: int) -> bool:
        return 0 <= x <= self._len_x and 0 <= y <= self._len_y

    def validate(self) -> bool:
        return Validator(self).validate()
