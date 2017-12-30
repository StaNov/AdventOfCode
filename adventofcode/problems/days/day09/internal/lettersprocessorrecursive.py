from . import LettersProcessor
from .states import LettersProcessorStateContextRecursive


class LettersProcessorRecursive(LettersProcessor):

    def create_letters_processor_state_context(self):
        return LettersProcessorStateContextRecursive()
