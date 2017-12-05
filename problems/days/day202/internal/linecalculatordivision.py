from .linecalculator import LineCalculator


class LineCalculatorDivision(LineCalculator):
    # TODO refactor: only override processing single number and returning result one
    def calculate_line(self, line):
        numbers_to_read = map(int, line.split())
        numbers_read = []

        for number_new in numbers_to_read:
            for number_already_read in numbers_read:
                if number_new % number_already_read == 0:
                    return number_new // number_already_read

                if number_already_read % number_new == 0:
                    return number_already_read // number_new

            numbers_read.append(number_new)

        raise Exception("No matching numbers found, this should never happen.")
