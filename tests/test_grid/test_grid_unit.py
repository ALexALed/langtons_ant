from grid import Grid


def test_grid_created():
    init_state = [[True, True], [True, False]]
    grid = Grid(init_state)
    assert grid
    assert grid.state == init_state


def test_grid_color():
    grid = Grid([[True, True], [True, False]])
    assert grid.get_color(1, 1) is False
    grid.change_color(1, 1)
    assert grid.get_color(1, 1) is True


def test_grid_validation():
    grid = Grid([[True, True], [True, False]])
    assert grid.validate()

    grid = Grid([True])
    assert not grid.validate()

    grid = Grid([[False, True], [True,]])
    assert not grid.validate()
