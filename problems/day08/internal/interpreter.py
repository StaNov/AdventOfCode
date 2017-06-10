import re


class Interpreter:
    def __init__(self):
        self.array = []
        self._init_array()

    def _init_array(self):
        lines = 20
        columns = 10
        for i in range(0, lines):
            line = []
            for j in range(0, columns):
                line.append(False)
            self.array.append(line)

    def command(self, line):
        match = re.fullmatch("rect (\w+)x(\w+)", line)

        width = int(match.group(1))
        height = int(match.group(2))

        for i in range(0, height):
            for j in range(0, width):
                self.array[i][j] = True

    def get_lightens(self):
        result = 0

        for line in self.array:
            for value in line:
                if value:
                    result += 1

        return result
