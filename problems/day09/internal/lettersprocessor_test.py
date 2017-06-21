import pytest

from . import LettersProcessor


@pytest.fixture
def processor():
    return LettersProcessor()


def test_empty_input(processor):
    assert processor.get_processed_output() == ""


def test_process_empty_string(processor):
    with pytest.raises(Exception):
        processor.process_letter("")
