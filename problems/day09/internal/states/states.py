import re
from .lettersprocessorstate import LettersProcessorState


class StateJustReading(LettersProcessorState):
    def process_letter(self, caller, letter):
        if letter != "(":
            caller.add_to_output(letter)
            return

        caller.set_state(StateReadingParenthesesContent())


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

    def return_remaining_letters(self):
        return "(" + self.parentheses_content


class StateReadingWhatToRepeat(LettersProcessorState):

    def __init__(self, length, how_many):
        self.length = length
        self.how_many = how_many
        self.what_to_repeat = ""

    def process_letter(self, caller, letter):
        self.what_to_repeat = self.what_to_repeat + letter

        if len(self.what_to_repeat) == self.length:
            caller.add_to_output(self.how_many * self.what_to_repeat)
            caller.set_state(StateJustReading())