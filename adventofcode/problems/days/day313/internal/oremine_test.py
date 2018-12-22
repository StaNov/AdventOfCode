from . import OreMine


class CarSpy:
    def __init__(self):
        super().__init__()
        self.moved = False

    def move(self):
        self.moved = True


def test_create_empty_ore_mine():
    cars = OreMine([]).cars
    assert 0 == len(cars)


def test_create_ore_mine_with_one_car():
    car = CarSpy()
    mine = OreMine([car])

    assert 1 == len(mine.cars)
    assert not car.moved


def test_car_moves_after_one_step():
    car = CarSpy()
    mine = OreMine([car])

    mine.simulate_step()

    assert car.moved
