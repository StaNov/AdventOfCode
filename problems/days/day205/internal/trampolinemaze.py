class TrampolineMaze:

    def __init__(self, values):
        self._values = values
        self._steps_done = 0

    def process_until_finished(self):
        value_to_add_to_source_item = self._value_to_add_to_source_item
        values = self._values
        values_length = len(values)
        current_index = 0
        steps_done = 0

        while not current_index >= values_length:
            jump_distance = values[current_index]
            new_current_index = current_index + jump_distance
            values[current_index] += value_to_add_to_source_item(jump_distance)
            current_index = new_current_index

            steps_done += 1

        self._steps_done = steps_done

    def get_steps_done(self):
        return self._steps_done

    def _value_to_add_to_source_item(self, jump_distance):
        return 1
