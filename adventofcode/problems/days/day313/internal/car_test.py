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


class RoadTypeSpy:
    def __init__(self, final_direction):
        super().__init__()
        self.final_direction = final_direction
        self.initial_direction_called_on = None

    def rotate(self, initial_direction):
        self.initial_direction_called_on = initial_direction
        return self.final_direction


def test_car_turns():
    initial_position = (10, 20)
    initial_direction = DirectionSpy()
    final_direction = DirectionSpy()
    road_type = RoadTypeSpy(final_direction)

    car = Car(initial_position, initial_direction)
    car.turn(road_type)

    assert initial_direction is road_type.initial_direction_called_on
    assert final_direction is car.direction
    assert initial_position is car.position
