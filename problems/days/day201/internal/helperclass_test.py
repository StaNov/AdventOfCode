import pytest

from . import HelperClass


@pytest.fixture
def helper():
    return HelperClass()


def test_helper_method(helper):
    assert helper.helper_method("test") == 0


def test_with_exception():
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
