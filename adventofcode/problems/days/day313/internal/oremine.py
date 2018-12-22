class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        self.cars.sort(key=lambda c: c.position)

        for car in self.cars:
            car.move()
