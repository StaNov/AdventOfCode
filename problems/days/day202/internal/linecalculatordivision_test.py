from . import LineCalculatorDivision


def test_calculate_two_divisible_numbers():
    assert_result("8 2", 4)


def test_calculate_multiple_divisible_numbers():
    assert_result("11 23 13 2 17 19 10 31", 5)


def assert_result(line, expected_value):
    assert LineCalculatorDivision(line).calculate_line() == expected_value
