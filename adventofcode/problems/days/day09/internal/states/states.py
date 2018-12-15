import re

from .lettersprocessorstate import LettersProcessorState


class StateJustReading(LettersProcessorState):
    def process_letter(self, caller, letter):
        if letter != "(":
            caller.add_to_output_length(1)
            return

        caller.set_state(StateReadingParenthesesContent())

    def is_ok_to_get_output_length_in_this_state(self):
        return True


class StateReadingParenthesesContent(LettersProcessorState):

    def __init__(self):
        self.parentheses_content = ""

    def process_letter(self, caller, letter):
        if letter == "(":
            raise Exception("No parenthesis inside parentheses!")

        if letter != ")":
            self.parentheses_content = self.parentheses_content + letter
            return

        match = re.fullmatch(r"(\w+)x(\w+)", self.parentheses_content)

        if match is None:
            raise Exception("Bad format of parentheses content: " + self.parentheses_content)

        what_to_repeat_length = int(match.group(1))
        what_to_repeat_how_many = int(match.group(2))
        caller.set_state(StateReadingWhatToRepeat(what_to_repeat_length, what_to_repeat_how_many))

    def is_ok_to_get_output_length_in_this_state(self):
        return False


class StateReadingWhatToRepeat(LettersProcessorState):

    def __init__(self, length, repeat_count):
        self.length = length
        self.repeat_count = repeat_count
        self.read_text_chunk = ""

    def process_letter(self, caller, letter):
        self.read_text_chunk += letter

        if len(self.read_text_chunk) == self.length:
            caller.process_read_text_chunk(self.repeat_count, self.read_text_chunk)
            caller.set_state(StateJustReading())

    def is_ok_to_get_output_length_in_this_state(self):
        return False
