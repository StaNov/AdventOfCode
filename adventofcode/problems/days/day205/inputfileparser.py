from adventofcode.problems.framework import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        lines = input_string.splitlines()
        return [int(x) for x in lines]
