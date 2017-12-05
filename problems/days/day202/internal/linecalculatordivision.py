from .linecalculator import LineCalculator


class LineCalculatorDivision(LineCalculator):

    def __init__(self, line):
        super().__init__(line)
        self._numbers_read = []
        self._result = None

    def _process_number(self, number):
        if self._result is not None:
            return

        for number_already_read in self._numbers_read:
            if number % number_already_read == 0:
                self._result = number // number_already_read

            if number_already_read % number == 0:
                self._result = number_already_read // number

        self._numbers_read.append(number)

    def _get_result(self):
        if self._result is None:
            raise Exception("No matching numbers found, this should never happen.")

        return self._result
