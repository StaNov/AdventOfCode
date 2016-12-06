from .internal import LineParser, Evaluator


class Solver:
    @staticmethod
    def solve_1(input_string):
        result = 0

        for line in input_string.split("\n"):
            parsed_line = LineParser.parse(line)
            line_value = Evaluator.evaluate(parsed_line)
            result += line_value

        return result

    @staticmethod
    def solve_2(input_string):
        return 0  # TODO
