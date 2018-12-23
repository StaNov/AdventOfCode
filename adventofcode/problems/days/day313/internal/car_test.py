from .car import Car


class DirectionSpy:
    APPLY_ON_RESULT = 50, 60

    def __init__(self):
        super().__init__()
        self.applied_on = None

    def apply_on(self, argument):
        self.applied_on = argument
        return DirectionSpy.APPLY_ON_RESULT


def test_create_car():
    car = Car((10, 20), DirectionSpy())

    assert (10, 20) == car.position
    assert None is car.direction.applied_on


def test_car_moves():
    direction = DirectionSpy()
    car = Car((10, 20), direction)

    car.move()

    assert DirectionSpy.APPLY_ON_RESULT == car.position
    assert (10, 20) == direction.applied_on
