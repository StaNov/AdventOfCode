from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        lines = input_string.splitlines()
        return [int(x) for x in lines]
