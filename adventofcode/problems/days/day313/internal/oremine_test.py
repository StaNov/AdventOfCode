from . import OreMine
from .car import Car


def test_create_empty_ore_mine():
    cars = OreMine([]).cars
    assert 0 == len(cars)


def test_create_ore_mine_with_one_car():
    mine = OreMine([Car((0, 0))])
    cars = mine.cars
    assert 1 == len(cars)
    assert (0, 0) == cars[0].position


def test_car_moves_down_after_one_step():
    mine = OreMine([Car((0, 0))])
    mine.simulate_step()
    assert (0, 1) == mine.cars[0].position


def test_car_moves_down_after_one_step_another_location():
    mine = OreMine([Car((5, 5))])
    mine.simulate_step()
    assert (5, 6) == mine.cars[0].position
