import re

from problems.utils import InputFileParser as BaseParser


class InputFileParser(BaseParser):
    def parse(self, input_string):
        if not input_string:
            return {}

        match = re.fullmatch("(.+) \((\d+)\)", input_string)
        name, number = match.groups()
        return {name: int(number)}
        # return input_string.splitlines()
