import time

import pytest

from adventofcode.problems.utils import testsuite
from . import HelperClass


@pytest.fixture
def helper():
    return HelperClass()


def test_helper_method(helper):
    # TODO
    assert 0 == helper.helper_method("test")


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")


@pytest.mark.skip
@testsuite.time_expensive
def test_time_expensive_test():
    time.sleep(1)
