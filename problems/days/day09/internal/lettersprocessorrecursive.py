from .states import LettersProcessorStateContextRecursive
from . import LettersProcessor


class LettersProcessorRecursive(LettersProcessor):

    def create_letters_processor_state_context(self):
        return LettersProcessorStateContextRecursive()
