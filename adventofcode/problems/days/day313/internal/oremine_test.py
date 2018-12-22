from .carspy import CarSpy
from .oremine import OreMine, CollisionHappened


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
    car_1 = CarSpy((0, 0))
    car_2 = CarSpy((0, 1))
    car_3 = CarSpy((0, 2))
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


def test_moving_to_occupied_position_causes_collision():
    car_1 = CarSpy((0, 0), (1, 1))
    car_2 = CarSpy((1, 1))

    mine = OreMine([car_1, car_2])

    try:
        mine.simulate_step()
        assert False, "Collision not detected!"
    except CollisionHappened as e:
        assert (1, 1) == e.collision_position


def test_simulate_until_collision_happens():
    car_1 = CarSpy((0, 0), (1, 1))
    car_2 = CarSpy((10, 10))

    mine = OreMine([car_1, car_2])

    assert (10, 10) == mine.simulate_until_first_collision()
