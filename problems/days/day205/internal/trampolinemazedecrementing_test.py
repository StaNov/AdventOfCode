from .trampolinemazedecrementing import TrampolineMazeDecrementing


def test_value_decreased_when_big_number():
    initial_value = 10

    maze = TrampolineMazeDecrementing([initial_value])
    maze.process_until_finished()
    assert initial_value - 1 == maze._values[0]
