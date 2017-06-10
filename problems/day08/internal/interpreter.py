import re


class Interpreter:
    def __init__(self, width, height):
        self.array = []
        self._init_array(width, height)

    def _init_array(self, width, height):
        for i in range(0, height):
            line = []
            for j in range(0, width):
                line.append(False)
            self.array.append(line)

    def command(self, line):
        if not line.startswith("rect"):
            raise Exception("Unknown command")

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
