import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def calculator():
    return DayCalculator()


def test_example_1_vertical_collision(calculator):
    assert "3,3" == DayCalculator(
        r" /-\ " "\n"
        r" | v " "\n"
        r" | | " "\n"
        r" | | " "\n"
        r" | ^ " "\n"
        r" \-/ " "\n"
    ).calculate_part_1()


def test_example_1_horizontal_collision(calculator):
    assert "4,0" == DayCalculator(
        r" />---<\ " "\n"
        r" |     | " "\n"
        r" \-----/ " "\n"
    ).calculate_part_1()


def test_example_1_corner_collision_1(calculator):
    assert "1,1" == DayCalculator(
        r" /-<\ " "\n"
        r" |  | " "\n"
        r" |  | " "\n"
        r" ^  | " "\n"
        r" \--/ " "\n"
    ).calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_corner_collision_2(calculator):
    assert "1,4" == DayCalculator(
        r" /--\ " "\n"
        r" v  | " "\n"
        r" |  | " "\n"
        r" |  | " "\n"
        r" \-</ " "\n"
    ).calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_1_full(calculator):
    assert "7,3" == DayCalculator(
        r"/->-\         " "\n"
        r"|   |  /----\ " "\n"
        r"| /-+--+-\  | " "\n"
        r"| | |  | v  | " "\n"
        r"\-+-/  \-+--/ " "\n"
        r"  \------/    " "\n"
    ).calculate_part_1()


# TODO
@pytest.mark.skip
def test_main_1(calculator):
    # TODO
    assert 0 == calculator.calculate_part_1()


# TODO
@pytest.mark.skip
def test_example_2_1(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 1").calculate_part_2()


# TODO
@pytest.mark.skip
def test_example_2_2(calculator):
    # TODO
    assert 0 == DayCalculator("Part 2, example 2").calculate_part_2()


# TODO
@pytest.mark.skip
def test_main_2(calculator):
    # TODO
    assert 0 == calculator.calculate_part_2()
