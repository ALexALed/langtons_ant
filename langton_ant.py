from grid import Grid
from ant import Ant, TurnDirection
from typing import List


class LangtonsAnt:
    def __init__(
        self, initial_state: List[List[bool]], start_position: List[int]
    ) -> None:
        self._grid = Grid(initial_state)
        self._ant = Ant(start_position[0], start_position[1])

    def next(self) -> bool:
        current_ant_position_x, current_ant_position_y = self._ant.position

        if self._grid.get_color(current_ant_position_x, current_ant_position_y):
            self._grid.change_color(current_ant_position_x, current_ant_position_y)
            self._ant.turn(TurnDirection.RIGHT)
            self._ant.move()
        else:
            self._grid.change_color(current_ant_position_x, current_ant_position_y)
            self._ant.turn(TurnDirection.LEFT)
            self._ant.move()

        return self.validate_move()

    @property
    def state(self):
        return self._grid.state

    @property
    def ant_position(self):
        return self._ant.position

    def validate_move(self) -> bool:
        current_ant_position_x, current_ant_position_y = self._ant.position
        return self._grid.validate_point(current_ant_position_x, current_ant_position_y)

    def validate(self) -> bool:
        return self._grid.validate()
