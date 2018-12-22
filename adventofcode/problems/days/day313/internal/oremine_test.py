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


def test_all_cars_move_after_one_step():
    car_1 = CarSpy()
    car_2 = CarSpy()
    car_3 = CarSpy()
    mine = OreMine([car_1, car_2, car_3])

    mine.simulate_step()

    assert car_1.moved
    assert car_2.moved
    assert car_3.moved
