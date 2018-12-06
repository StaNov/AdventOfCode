from .inputtextparser import InputTextParser


def test_parse_empty_input():
    assert [] == InputTextParser().parse("")


def test_parse_one_line():
    result_list = InputTextParser().parse("#123 @ 12,34: 56x789")

    assert 1 == len(result_list)

    result = result_list[0]
    assert 123 == result.id
    assert 12 == result.position_x
    assert 34 == result.position_y
    assert 56 == result.size_x
    assert 789 == result.size_y
