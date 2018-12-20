import time

import pytest

from .car import Car
from adventofcode.problems.framework import testsuite
from . import OreMine


def test_create_empty_ore_mine():
    cars = OreMine([]).cars
    assert 0 == len(cars)


def test_create_ore_mine_with_two_cars():
    cars = OreMine([Car((0, 0)), Car((1, 1))]).cars
    assert 2 == len(cars)


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")


@testsuite.time_expensive
def test_time_expensive_test():
    time.sleep(1)
