from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        return [parse_input_value(x) for x in input_string.splitlines()]


def parse_input_value(value):
    sign = value[0]
    number = int(value[1:])

    if sign == "-":
        number = -number

    return number
