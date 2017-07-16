from . import InputParser


def test_parse_line():
    assert InputParser.parse_line("123 456 789") == (123, 456, 789)


def test_parse_vertically():
    input_ = "101 201 301\n102 202 302\n103 203 303\n401 501 601\n402 502 602\n403 503 603"
    result = [
        (101, 102, 103),
        (201, 202, 203),
        (301, 302, 303),
        (401, 402, 403),
        (501, 502, 503),
        (601, 602, 603)
    ]

    assert InputParser.parse_vertically(input_) == result
