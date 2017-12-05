from .linecalculator import LineCalculator


class LineCalculatorMinMax(LineCalculator):

    def __init__(self, line):
        super().__init__(line)
        self._highest = None
        self._lowest = None

    def _process_number(self, number):
        if self._highest is None or number > self._highest:
            self._highest = number

        if self._lowest is None or number < self._lowest:
            self._lowest = number

    def _get_result(self):
        return self._highest - self._lowest
