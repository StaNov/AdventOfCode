from problems.utils import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        return [] if not input_string else [int(input_string)]
