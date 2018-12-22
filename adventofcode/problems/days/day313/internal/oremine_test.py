from . import OreMine
from .car import Car


class DirectionSpy:
    def __init__(self) -> None:
        super().__init__()
        self.applied_on = None

    def apply_on(self, argument):
        self.applied_on = argument


def test_create_empty_ore_mine():
    cars = OreMine([]).cars
    assert 0 == len(cars)


def test_create_ore_mine_with_one_car():
    mine = OreMine([Car((0, 0), DirectionSpy())])
    cars = mine.cars
    assert 1 == len(cars)

    car = cars[0]
    assert (0, 0) == car.position
    assert None is car.direction.applied_on


def test_car_moves_after_one_step():
    mine = OreMine([Car((0, 0), DirectionSpy())])
    mine.simulate_step()
    assert (0, 0) == mine.cars[0].direction.applied_on
