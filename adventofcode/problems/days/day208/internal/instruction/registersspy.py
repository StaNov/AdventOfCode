class RegistersSpy:
    def __init__(self):
        self._called_values = []

    def add(self, name, value):
        self._called_values.append((name, value))

    def get(self, name):
        return 0

    def called_commands(self):
        return tuple(self._called_values)
