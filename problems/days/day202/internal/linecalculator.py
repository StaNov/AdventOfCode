class LineCalculator:
    def __init__(self, line):
        self.numbers_to_read = map(int, line.split())

    def calculate_line(self):
        for number in self.numbers_to_read:
            self._process_number(number)

        return self._get_result()

    def _process_number(self, number):
        raise NotImplemented()

    def _get_result(self):
        raise NotImplemented()
