from problems.utils import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        return [int(x) for x in input_string.split()]
