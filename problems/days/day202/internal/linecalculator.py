class LineCalculator:
    def __init__(self):
        pass

    def calculate_line(self, line):
        numbers = map(int, line.split())
        highest = None
        lowest = None

        for number in numbers:
            if not self.accept_number(number):
                continue

            if highest is None or number > highest:
                highest = number

            if lowest is None or number < lowest:
                lowest = number

        return highest - lowest

    def accept_number(self, number):
        return True


class LineCalculatorOnlyEvens(LineCalculator):
    def accept_number(self, number):
        return number % 2 == 0
