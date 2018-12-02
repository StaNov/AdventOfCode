from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        return input_string.splitlines()
