from ant import Ant
from ant import Orientation, TurnDirection


def test_ant_created():
    ant = Ant(1, 1)

    assert ant
    x, y = ant.position
    assert x == 1
    assert y == 1
    assert ant.orientation == Orientation.UP


def test_ant_do_turn():
    ant = Ant(1, 1)
    assert ant.orientation == Orientation.UP
    ant.turn(TurnDirection.LEFT)
    assert ant.orientation == Orientation.LEFT
    ant.turn(TurnDirection.LEFT)
    assert ant.orientation == Orientation.DOWN


def test_ant_do_move():
    ant = Ant(1, 1)
    x, y = ant.position
    assert x == 1
    assert y == 1
    ant.move()
    x, y = ant.position
    assert x == 1
    assert y == 0
    ant.turn(TurnDirection.RIGHT)
    ant.move()
    x, y = ant.position
    assert x == 2
    assert y == 0
