from .internal import LineParser, TriangleChecker


class Solver:
    @staticmethod
    def solve_1(input_string):
        result = 0

        for line in input_string.split("\n"):
            x, y, z = LineParser.parse(line)
            is_triangle = TriangleChecker.check(x, y, z)
            if is_triangle:
                result += 1

        return result

    @staticmethod
    def solve_2(input_string):
        return 0  # TODO
