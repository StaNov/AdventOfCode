class RegistersSpy:
    def __init__(self):
        self._called_name = None
        self._called_value = None

    def add(self, name, value):
        self._called_name = name
        self._called_value = value

    def get(self, name):
        return 0

    def called_with_name_and_value(self):
        return self._called_name, self._called_value
