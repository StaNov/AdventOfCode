from . import OreMine


class CarSpy:
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.position = position
        self.moved = False
        self.those_must_move_after_this = []
        self.those_must_move_before_this = []

    def move(self):
        self.moved = True

        for before in self.those_must_move_before_this:
            assert before.moved, "Not all cars were moved that should move before this one."

        for after in self.those_must_move_after_this:
            assert not after.moved, "Some car was incorrectly moved before this one."

    def can_move_only_before(self, before):
        self.those_must_move_after_this = before

    def can_move_only_after(self, after):
        self.those_must_move_before_this = after


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


def test_cars_move_in_correct_order():
    car_1 = CarSpy((1, 1))
    car_2 = CarSpy((1, 5))
    car_3 = CarSpy((5, 5))

    car_1.can_move_only_before([car_2, car_3])
    car_2.can_move_only_after([car_1])
    car_2.can_move_only_before([car_3])
    car_3.can_move_only_after([car_1, car_2])

    mine = OreMine([car_3, car_1, car_2])

    mine.simulate_step()

    assert car_3.moved
    assert car_1.moved
    assert car_2.moved
