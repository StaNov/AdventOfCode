import re

from problems.utils import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        result = {}

        for line in input_string.splitlines():
            self.parse_line(line, result)

        return result

    def parse_line(self, line, result):
        parts = line.split(" -> ")
        name_and_number = parts[0]
        subprograms = parts[1].split(", ") if len(parts) == 2 else []
        match = re.fullmatch("(.+) \((\d+)\)", name_and_number)
        name, number = match.groups()
        result[name] = (int(number), subprograms)
