from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        input_lines = input_string.splitlines()
        return [parse_input_line(x) for x in input_lines]


def parse_input_line(value):
    sign = value[0]
    number = int(value[1:])

    if sign == "-":
        number = -number

    return number
