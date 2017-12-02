import pytest
from .main import DayCalculator


# TODO rename to day_calculator
@pytest.fixture
def main():
    return DayCalculator()


# TODO do it in abstract way?
# def test_main():
#     main.test_both_parts("expected_result_1", "expected_result_2")
# make argument None if the part should not be tested
def test_main_1(main):
    # TODO
    assert main.calculate_part_1() == 0


def test_main_2(main):
    # TODO
    assert main.calculate_part_2() == 0
