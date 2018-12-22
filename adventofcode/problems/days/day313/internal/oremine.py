class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        for car in self.cars:
            car.move()
