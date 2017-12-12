class TrampolineMaze:

    def __init__(self, values):
        self._values = values
        self._steps_done = 0

    def is_finished(self):
        return len(self._values) == 0 or len(self._values) == self._steps_done

    def do_step(self):
        self._steps_done += 1
