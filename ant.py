from typing import Tuple
from enum import Enum


class Orientation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class TurnDirection(Enum):
    LEFT = -1
    RIGHT = 1


class Ant:
    def __init__(
        self, x: int, y: int, orientation: Orientation = Orientation.UP
    ) -> None:
        self._x = x
        self._y = y
        self.orientation = orientation

    @property
    def position(self) -> Tuple[int, int]:
        return self._x, self._y

    def move(self, step_size: int = 1) -> None:

        move_axis = (
            "x"
            if self.orientation == Orientation.LEFT
            or self.orientation == Orientation.RIGHT
            else "y"
        )

        move_direction = (
            1
            if self.orientation == Orientation.RIGHT
            or self.orientation == Orientation.DOWN
            else -1
        )

        if move_axis == "x":
            self._x += move_direction * step_size
        else:
            self._y += move_direction * step_size

    def turn(self, direction: TurnDirection) -> None:
        new_orientation = self.orientation.value + direction.value
        if not 0 < new_orientation < 3:
            new_orientation %= 4
        self.orientation = Orientation(new_orientation)
