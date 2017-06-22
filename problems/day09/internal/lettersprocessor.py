from enum import Enum

import re


class LettersProcessor:
    def __init__(self):
        self.output = ""
        self.stateOld = LettersProcessorStateOld.JUST_READING
        self.state = StateJustReading()
        self.parentheses_content = ""
        self.what_to_repeat = ""
        self.what_to_repeat_length = 0
        self.what_to_repeat_how_many = 0

    def process_letter(self, letter):
        if len(letter) != 1:
            raise Exception("Argument must be one letter!")

        if self.stateOld == LettersProcessorStateOld.JUST_READING:
            self.state.process_letter(self, letter)
            return

        if self.stateOld == LettersProcessorStateOld.READING_PARENTHESES_CONTAINS:
            self._read_parentheses_content(letter)
            return

        if self.stateOld == LettersProcessorStateOld.READING_WHAT_TO_REPEAT:
            self._read_what_to_repeat(letter)
            return

    def _read_parentheses_content(self, letter):
        if letter == "(":
            raise Exception("No parenthesis inside parentheses!")

        if letter != ")":
            self.parentheses_content = self.parentheses_content + letter
            return

        match = re.fullmatch("(\w+)x(\w+)", self.parentheses_content)

        if match is None:
            raise Exception("Bad format of parentheses content: " + self.parentheses_content)

        self.what_to_repeat_length = int(match.group(1))
        self.what_to_repeat_how_many = int(match.group(2))
        self.what_to_repeat = ""

        self.stateOld = LettersProcessorStateOld.READING_WHAT_TO_REPEAT

    def _read_what_to_repeat(self, letter):
        self.what_to_repeat = self.what_to_repeat + letter

        if len(self.what_to_repeat) == self.what_to_repeat_length:
            self.output = self.output + self.what_to_repeat_how_many * self.what_to_repeat
            self.parentheses_content = ""
            self.stateOld = LettersProcessorStateOld.JUST_READING

    def _set_state(self, state):
        pass # TODO

    def add_to_output(self, content_to_add):
        self.output = self.output + content_to_add

    def get_processed_output(self):
        if self.parentheses_content != "":
            self.output = self.output + "(" + self.parentheses_content

        return self.output


# TODO delete
class LettersProcessorStateOld(Enum):
    JUST_READING = 1
    READING_PARENTHESES_CONTAINS = 2
    READING_WHAT_TO_REPEAT = 3


class LettersProcessorState:
    def process_letter(self, caller, letter):
        raise Exception("Not implemented!")


class StateJustReading(LettersProcessorState):
    def process_letter(self, caller, letter):
        if letter != "(":
            caller.add_to_output(letter)
            return

        caller.parentheses_content = ""
        # TODO swap
        caller.stateOld = LettersProcessorStateOld.READING_PARENTHESES_CONTAINS
        #caller._set_state(StateReadingParenthesesContent)