import pytest

from problems.utils.inputfileparser import InputFileParser


def test_parse_empty_string():
    assert "" == InputFileParser().parse("")


@pytest.mark.skip
def test_parse():
    assert "abc" == InputFileParser().parse("abc")