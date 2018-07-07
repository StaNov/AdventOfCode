from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        return [int(x) for x in input_string.split()]
