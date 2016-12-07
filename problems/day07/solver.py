from .internal import LineParser, AbbaChecker


class Solver:
    @staticmethod
    def solve_1(input_string):
        result = 0

        for line in input_string.splitlines():
            including, excluding = LineParser.parse(line)

            if not AbbaChecker.at_least_one_is_abba(including) or not AbbaChecker.all_are_not_abba(excluding):
                continue

            result += 1

        return result

    @staticmethod
    def solve_2(input_string):
        return 0  # TODO
