from .states import LettersProcessorStateContext


class LettersProcessor:

    def __init__(self):
        self.context = self.create_letters_processor_state_context()

    def create_letters_processor_state_context(self):
        return LettersProcessorStateContext()

    def process_letter(self, letter):
        self.context.process_letter(letter)

    def get_processed_output_length(self):
        return self.context.get_processed_output_length()
