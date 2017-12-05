class LinesSummer:
    def __init__(self, line_calculator):
        self.line_calculator = line_calculator

    def sum_processed_lines(self, input_string):
        result = 0

        for line in input_string.splitlines():
            result += self.line_calculator.calculate_line(line)

        return result
