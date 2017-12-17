from .trampolinemaze import TrampolineMaze


def test_empty_maze_takes_zero_steps_to_finish():
    maze = TrampolineMaze([])
    maze.process_until_finished()
    assert 0 == maze.get_steps_done()


def test_maze_with_one_is_finished_after_one_step():
    maze = TrampolineMaze([1])
    maze.process_until_finished()
    assert 1 == maze.get_steps_done()


def test_maze_with_one_and_two_is_finished_after_two_steps():
    maze = TrampolineMaze([1, 2])
    maze.process_until_finished()
    assert 2 == maze.get_steps_done()


def test_maze_with_zero_is_finished_after_two_step():
    maze = TrampolineMaze([0])
    maze.process_until_finished()
    assert 2 == maze.get_steps_done()


def test_to_string():
    maze = TrampolineMaze([1, 2, 3, 4, 5])
    maze._current_index = 3
    assert " 1 ,  2 ,  3 , (4),  5 " == str(maze)
