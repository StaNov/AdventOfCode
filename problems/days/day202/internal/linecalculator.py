class LineCalculator:
    def __init__(self):
        pass

    def calculate_line(self, line):
        number1, number2 = line.split(" ")
        return int(number1) - int(number2)
