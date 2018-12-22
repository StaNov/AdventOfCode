class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        car = self.cars[0]
        car.position = car.direction.apply_on(car.position)
