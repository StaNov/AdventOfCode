class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        self.cars[0].position = 0, 1
