from .trampolinemaze import TrampolineMaze


def test_empty_maze_is_already_finished():
    assert TrampolineMaze([]).is_finished()
