from .states import LettersProcessorStateContext


class LettersProcessor:

    def __init__(self):
        self.context = LettersProcessorStateContext()

    def process_letter(self, letter):
        self.context.process_letter(letter)

    def get_processed_output_length(self):
        return self.context.get_processed_output_length()
