class Registers:
    def __init__(self) -> None:
        self.value = 0

    def get(self, name):
        return self.value

    def add(self, name, value):
        self.value += value
