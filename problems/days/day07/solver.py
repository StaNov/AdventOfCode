from .internal import LineParser, AbbaChecker, SslChecker


class Solver:
    @staticmethod
    def solve_1(input_string):
        result = 0

        for line in input_string.splitlines():
            including, excluding = LineParser.parse(line)

            including_abbas = AbbaChecker.get_abbas_from_strings(including)
            excluding_abbas = AbbaChecker.get_abbas_from_strings(excluding)

            if len(including_abbas) == 0 or len(excluding_abbas) > 0:
                continue

            result += 1

        return result

    @staticmethod
    def solve_2(input_string):
        result = 0

        for line in input_string.splitlines():
            if SslChecker.is_ssl(line):
                result += 1

        return result
