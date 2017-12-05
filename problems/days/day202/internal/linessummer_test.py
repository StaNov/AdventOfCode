import pytest

from .linessummer import LinesSummer
from .linecalculator import LineCalculator


class LineCalculatorTest(LineCalculator):

    def __init__(self, line):
        super().__init__(line)

    def calculate_line(self):
        return 1


@pytest.fixture
def summer():
    return LinesSummer(LineCalculatorTest)


def test_empty_file_calculates_zero_lines(summer):
    assert summer.sum_processed_lines("") == 0


def test_one_line(summer):
    assert summer.sum_processed_lines("one line") == 1


def test_two_lines(summer):
    assert summer.sum_processed_lines("first\nsecond") == 2
