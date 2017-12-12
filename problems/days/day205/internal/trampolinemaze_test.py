from .trampolinemaze import TrampolineMaze


def test_empty_maze_is_already_finished():
    assert TrampolineMaze([]).is_finished()


def test_maze_with_one_is_not_initially_finished():
    assert not TrampolineMaze([1]).is_finished()
