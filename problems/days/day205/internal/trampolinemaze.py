class TrampolineMaze:

    def __init__(self, values):
        self._values = values
        self._steps_done = 0
        self._current_index = 0

    def process_until_finished(self):
        while not self.is_finished():
            self.do_step()

    def is_finished(self):
        return self._current_index >= len(self._values)

    def do_step(self):
        if self.is_finished():
            raise CannotDoStepOnFinishedMaze()

        self._steps_done += 1

        new_current_index = self._current_index + self._values[self._current_index]
        self._values[self._current_index] += 1
        self._current_index = new_current_index

    def get_steps_done(self):
        return self._steps_done


class CannotDoStepOnFinishedMaze(Exception):
    pass
