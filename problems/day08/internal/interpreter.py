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
        processor = CommandProcessor.create(line)
        processor.process(self.array)

    def get_lightens(self):
        result = 0

        for line in self.array:
            for value in line:
                if value:
                    result += 1

        return result


class CommandProcessor:
    def __init__(self):
        raise Exception("This is abstract class, use the static create method instead.")

    def process(self, array):
        raise Exception("Abstract method not implemented.")

    @staticmethod
    def create(command):
        if command.startswith("rect"):
            return RectCommandProcessor(command)

        raise Exception("Unknown command")


class RectCommandProcessor(CommandProcessor):
    def __init__(self, command):
        match = re.fullmatch("rect (\w+)x(\w+)", command)

        self.rect_width = int(match.group(1))
        self.rect_height = int(match.group(2))

    def process(self, array):
        for i in range(0, self.rect_height):
            for j in range(0, self.rect_width):
                array[i][j] = True
