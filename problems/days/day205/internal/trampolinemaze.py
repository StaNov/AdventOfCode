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

        jump_distance = self._values[self._current_index]
        new_current_index = self._current_index + jump_distance
        self._values[self._current_index] += self._value_to_add_to_source_item(jump_distance)
        self._current_index = new_current_index

    def get_steps_done(self):
        return self._steps_done

    def _value_to_add_to_source_item(self, jump_distance):
        return 1


class CannotDoStepOnFinishedMaze(Exception):
    pass
