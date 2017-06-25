from .states import StateJustReading


class LettersProcessorStateContext:

    def __init__(self):
        self.output_length = 0
        self._state = StateJustReading()

    def process_letter(self, letter):
        if len(letter) != 1:
            raise Exception("Argument must be one letter!")

        self._state.process_letter(self, letter)

    def get_processed_output_length(self):
        return self.output_length

    def set_state(self, state):
        self._state = state

    def add_to_output_length(self, length_to_add):
        self.output_length += length_to_add
