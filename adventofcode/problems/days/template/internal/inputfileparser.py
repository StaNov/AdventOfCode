from adventofcode.problems.framework import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        # TODO
        return input_string.splitlines()
