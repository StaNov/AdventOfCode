class LineCalculatorMinMax:
    def __init__(self):
        pass

    def calculate_line(self, line):
        numbers = map(int, line.split())
        highest = None
        lowest = None

        for number in numbers:
            if highest is None or number > highest:
                highest = number

            if lowest is None or number < lowest:
                lowest = number

        return highest - lowest
