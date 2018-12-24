from .roadtype import RoadType


class OreMine:
    def __init__(self, cars, roads=None):
        if roads is None:
            roads = []

        self.cars = cars
        self.roads = {}

        for road_position, road_type in roads:
            self.roads[road_position] = road_type

    def simulate_step(self):
        self.cars.sort(key=lambda c: c.position)

        for car in self.cars:
            self._move_and_turn_car(car)

    def _move_and_turn_car(self, car):
        car.move()
        self._check_collisions(car)
        road_under_car = self.roads.get(car.position, RoadType.STRAIGHT)
        car.turn(road_under_car)

    def _check_collisions(self, car):
        same_position_count = sum(car.position == c.position for c in self.cars)

        if same_position_count > 1:
            raise CollisionHappened(car.position)

    def simulate_until_first_collision(self):
        try:
            while True:
                self.simulate_step()
        except CollisionHappened as collision:
            return collision.collision_position


class CollisionHappened(BaseException):
    def __init__(self, collision_position, *args: object):
        super().__init__(*args)
        self.collision_position = collision_position
