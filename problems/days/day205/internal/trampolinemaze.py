class TrampolineMaze:

    def __init__(self, values, is_decrementing=False):
        self._is_decrementing = is_decrementing
        self._values = values
        self._steps_done = 0

    def process_until_finished(self):
        values = self._values
        values_length = len(values)
        is_decrementing = self._is_decrementing
        current_index = 0
        steps_done = 0

        while not current_index >= values_length:
            jump_distance = values[current_index]
            new_current_index = current_index + jump_distance
            value_to_add = -1 if is_decrementing and jump_distance >= 3 else 1

            values[current_index] += value_to_add
            current_index = new_current_index

            steps_done += 1

        self._steps_done = steps_done

    def get_steps_done(self):
        return self._steps_done
