from .trampolinemaze import TrampolineMaze


def test_empty_maze_is_already_finished():
    assert TrampolineMaze([]).is_finished()


def test_maze_with_one_is_not_initially_finished():
    assert not TrampolineMaze([1]).is_finished()


def test_maze_with_one_is_finished_after_one_step():
    maze = TrampolineMaze([1])
    maze.do_step()
    assert maze.is_finished()


def test_maze_with_one_and_two_is_not_finished_after_one_step():
    maze = TrampolineMaze([1, 2])
    maze.do_step()
    assert not maze.is_finished()
