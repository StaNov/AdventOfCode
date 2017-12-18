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

        name, number = self.parse_name_and_number(parts[0])
        subprograms = self.parse_subprograms(parts[1]) if len(parts) == 2 else []

        result[name] = (int(number), subprograms)

    def parse_name_and_number(self, name_and_number):
        match = re.fullmatch("(.+) \((\d+)\)", name_and_number)
        name, number = match.groups()
        return name, number

    def parse_subprograms(self, subprograms_string):
        return subprograms_string.split(", ")
