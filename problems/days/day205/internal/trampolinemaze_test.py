import pytest

from .trampolinemaze import TrampolineMaze, CannotDoStepOnFinishedMaze


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


def test_maze_with_one_and_two_is_finished_after_two_steps():
    maze = TrampolineMaze([1, 2])
    maze.process_until_finished()
    assert 2 == maze.get_steps_done()


def test_do_step_on_finished_maze_raises_exception():
    maze = TrampolineMaze([])
    maze.process_until_finished()
    with pytest.raises(CannotDoStepOnFinishedMaze):
        maze.do_step()


@pytest.mark.skip
def test_maze_with_zero_is_finished_after_two_step():
    maze = TrampolineMaze([0])
    maze.process_until_finished()
    assert 2 == maze.get_steps_done()
