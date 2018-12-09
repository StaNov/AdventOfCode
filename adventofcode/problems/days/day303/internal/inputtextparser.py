import re

from adventofcode.problems.framework import DefaultInputTextParser
# TODO why doesn't work "from . import" ?
from .santasuitpatch import SantaSuitPatch


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        result = []
        lines = input_string.splitlines()

        for line in lines:
            result.append(parse_line(line))

        return result


def parse_line(line):
    groups = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line).groups()
    piece_id, position_x, position_y, size_x, size_y = groups
    return SantaSuitPatch(piece_id, position_x, position_y, size_x, size_y)
