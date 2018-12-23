class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        self.cars.sort(key=lambda c: c.position)

        for car in self.cars:
            car.move()
            self._check_collisions(car)

            class StraightRoadType:
                def rotate(self, direction):
                    return direction

            car.turn(StraightRoadType())

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
