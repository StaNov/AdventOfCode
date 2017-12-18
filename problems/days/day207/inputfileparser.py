import re

from problems.utils import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        result = {}

        for line in input_string.splitlines():
            self.parse_line(line, result)

        return result

    def parse_line(self, line, result):
        match = re.fullmatch("(.+) \((\d+)\)", line)
        name, number = match.groups()
        result[name] = (int(number), [])
