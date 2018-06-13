import pytest

from .daycalculator import DayCalculator


@pytest.fixture
def main():
    return DayCalculator()


def test_main_1_on_empty_input(main):
    assert 0 == main.calculate_part_1("")


# TODO
@pytest.mark.skip
def test_main_1_with_all_conditions_true(main):
    custom_input = (
        "a inc 10 if a = 0\n"
        "a inc 10 if b <= 0\n"
        "a inc 10 if c > -1\n"
        "a inc 10 if d < 2\n"
        "a dec -10 if e >= 0")

    assert 50 == main.calculate_part_1(custom_input)


def test_main_1(main):
    # TODO
    # assert 0 == main.calculate_part_1()
    pass


def test_main_2(main):
    # TODO
    # assert 0 == main.calculate_part_2()
    pass
