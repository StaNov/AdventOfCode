class Car:

    def __init__(self, position, direction):
        super().__init__()
        self.position = position
        self.direction = direction

    def move(self):
        self.position = self.direction.apply_on(self.position)
