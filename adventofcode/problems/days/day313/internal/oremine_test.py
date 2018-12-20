import time

import pytest

from .car import Car
from adventofcode.problems.framework import testsuite
from . import OreMine


def test_create_empty_ore_mine():
    cars = OreMine([]).cars
    assert 0 == len(cars)


def test_create_ore_mine_with_one_car():
    cars = OreMine([Car((0, 0))]).cars
    assert 1 == len(cars)


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")


@testsuite.time_expensive
def test_time_expensive_test():
    time.sleep(1)
