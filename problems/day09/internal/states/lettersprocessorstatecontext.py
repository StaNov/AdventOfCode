from .states import StateJustReading


class LettersProcessorStateContext:

    def __init__(self):
        self.output = ""
        self._state = StateJustReading()

    def process_letter(self, letter):
        if len(letter) != 1:
            raise Exception("Argument must be one letter!")

        self._state.process_letter(self, letter)

    def get_processed_output(self):
        self.add_to_output(self._state.return_remaining_letters())
        return self.output

    def set_state(self, state):
        self._state = state

    def add_to_output(self, content_to_add):
        self.output = self.output + content_to_add
