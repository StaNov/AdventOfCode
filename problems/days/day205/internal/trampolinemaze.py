class TrampolineMaze:

    def __init__(self, values):
        self._values = values
        self._step_done = False

    def is_finished(self):
        return len(self._values) == 0 or self._step_done

    def do_step(self):
        self._step_done = True
