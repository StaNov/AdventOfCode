import pytest

from .linessummer import LinesSummer
from .linecalculator import LineCalculator


@pytest.fixture
def line_calculator():
    return LineCalculatorTest()


@pytest.fixture
def summer(line_calculator):
    return LinesSummer(line_calculator)


class LineCalculatorTest(LineCalculator):
    def calculate_line(self, line):
        return 1


def test_empty_file_calculates_zero_lines(summer):
    assert summer.sum_processed_lines("") == 0


def test_one_line(summer):
    assert summer.sum_processed_lines("one line") == 1


def test_two_lines(summer):
    assert summer.sum_processed_lines("first\nsecond") == 2
