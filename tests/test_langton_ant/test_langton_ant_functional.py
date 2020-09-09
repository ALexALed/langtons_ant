from langton_ant import LangtonsAnt


def test_langton_ant():
    initial_state = [[True, True, True], [False, False, False], [True, False, False]]

    la = LangtonsAnt(initial_state=initial_state, start_position=[1, 1])
    status = la.next()
    assert status

    x, y = la.ant_position

    assert x == 0
    assert y == 1
    assert la.state[1][1] == True

    status = la.next()
    assert status

    x, y = la.ant_position

    assert x == 0
    assert y == 2
    assert la.state[1][0] == True

    status = la.next()
    assert not status
