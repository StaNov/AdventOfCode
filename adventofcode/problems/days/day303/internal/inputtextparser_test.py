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


def test_parse_more_lines():
    result_list = InputTextParser().parse(
        "#123 @ 1,456: 98x765\n"
        "#12 @ 12,45: 987x65\n"
        "#1 @ 123,4: 9876x5\n"
    )

    assert 3 == len(result_list)

    assert 123 == result_list[0].id
    assert 12 == result_list[1].position_x
    assert 4 == result_list[2].position_y
    assert 987 == result_list[1].size_x
    assert 5 == result_list[2].size_y
