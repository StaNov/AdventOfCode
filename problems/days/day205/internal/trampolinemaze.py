class TrampolineMaze:

    def __init__(self, values):
        self._values = values

    def is_finished(self):
        return len(self._values) == 0
