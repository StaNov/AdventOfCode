class OreMine:
    def __init__(self, cars):
        self.cars = cars

    def simulate_step(self):
        previous_x, previous_y = self.cars[0].position
        self.cars[0].position = (
            previous_x,
            previous_y + 1
        )
