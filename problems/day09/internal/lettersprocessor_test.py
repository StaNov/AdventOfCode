import pytest

from . import LettersProcessor


@pytest.fixture
def processor():
    return LettersProcessor()


def test_helper_method(processor):
    # TODO
    assert len(processor.get_processed_output()) == 0


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
