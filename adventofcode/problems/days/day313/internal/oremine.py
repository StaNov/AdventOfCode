from .direction import Direction


class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        car = self.cars[0]
        previous_x, previous_y = car.position

        if car.direction == Direction.DOWN:
            car.position = (
                previous_x,
                previous_y + 1
            )
        elif car.direction == Direction.UP:
            car.position = (
                previous_x,
                previous_y - 1
            )
