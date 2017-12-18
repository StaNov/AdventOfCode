import pytest

from .inputfileparser import InputFileParser


def test_parse_empty():
    assert {} == InputFileParser().parse("")


@pytest.mark.skip
def test_parse_one_line():
    assert {"abc": 123} == InputFileParser().parse("abc (123)")
