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

        match = re.fullmatch("(\w+)x(\w+)", self.parentheses_content)

        if match is None:
            raise Exception("Bad format of parentheses content: " + self.parentheses_content)

        what_to_repeat_length = int(match.group(1))
        what_to_repeat_how_many = int(match.group(2))
        caller.set_state(StateReadingWhatToRepeat(what_to_repeat_length, what_to_repeat_how_many))

    def is_ok_to_get_output_length_in_this_state(self):
        return False


class StateReadingWhatToRepeat(LettersProcessorState):

    def __init__(self, length, how_many):
        self.length = length
        self.how_many = how_many
        self.already_read_letters_counter = 0

    def process_letter(self, caller, letter):
        self.already_read_letters_counter += 1

        if self.already_read_letters_counter == self.length:
            caller.add_to_output_length(self.how_many * self.length)
            caller.set_state(StateJustReading())

    def is_ok_to_get_output_length_in_this_state(self):
        return False
