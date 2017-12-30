from . import LineCalculatorMinMax


def test_calculate_two_same_numbers():
    assert_result("1 1", 0)


def test_calculate_two_different_numbers_descending():
    assert_result("5 2", 3)


def test_calculate_two_different_numbers_ascending():
    assert_result("1 8", 7)


def test_calculate_multiple_different_numbers():
    assert_result("1 8 4 12 2", 11)


def assert_result(line, expected_value):
    assert LineCalculatorMinMax(line).calculate_line() == expected_value
