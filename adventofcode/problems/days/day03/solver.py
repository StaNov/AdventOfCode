from .internal import InputParser, TriangleChecker


class Solver:
    @staticmethod
    def solve_1(input_string):
        result = 0

        for line in input_string.splitlines():
            x, y, z = InputParser.parse_line(line)
            is_triangle = TriangleChecker.check(x, y, z)
            if is_triangle:
                result += 1

        return result

    @staticmethod
    def solve_2(input_string):
        result = 0
        triangles = InputParser.parse_vertically(input_string)

        for x, y, z in triangles:
            is_triangle = TriangleChecker.check(x, y, z)
            if is_triangle:
                result += 1

        return result
