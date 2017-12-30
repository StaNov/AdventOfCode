class LinesSummer:
    def __init__(self, line_calculator_type):
        self.line_calculator_type = line_calculator_type

    def sum_processed_lines(self, input_string):
        result = 0

        for line in input_string.splitlines():
            line_calculator = self.line_calculator_type(line)
            result += line_calculator.calculate_line()

        return result
