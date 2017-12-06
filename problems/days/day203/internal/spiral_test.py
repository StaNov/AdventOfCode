import pytest

from . import Spiral


@pytest.fixture
def spiral():
    return Spiral()


def test_helper_method(spiral):
    # TODO
    assert spiral.helper_method("test") == 0


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
