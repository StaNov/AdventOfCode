import re


class Interpreter:
    def __init__(self, width, height):
        self.array = []
        self._init_array(width, height)

    def _init_array(self, width, height):
        for _ in range(0, height):
            line = []
            for _ in range(0, width):
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

    def get_display(self):
        result = ""
        for line in self.array:
            for value in line:
                if value:
                    result += "X"
                else:
                    result += " "
            result += "\n"

        return result


class CommandProcessor:
    def __init__(self):
        raise Exception("This is abstract class, use the static create method instead.")

    def process(self, array):
        raise NotImplementedError("Abstract method not implemented.")

    @staticmethod
    def create(command):
        if command.startswith("rect"):
            return RectCommandProcessor(command)
        if command.startswith("rotate row"):
            return RotateRowCommandProcessor(command)
        if command.startswith("rotate column"):
            return RotateColumnCommandProcessor(command)

        raise Exception("Unknown command")


class RectCommandProcessor(CommandProcessor):
    def __init__(self, command):
        match = re.fullmatch(r"rect (\w+)x(\w+)", command)

        self.rect_width = int(match.group(1))
        self.rect_height = int(match.group(2))

    def process(self, array):
        for i in range(0, self.rect_height):
            for j in range(0, self.rect_width):
                array[i][j] = True


class RotateRowCommandProcessor(CommandProcessor):
    def __init__(self, command):
        match = re.fullmatch(r"rotate row y=(\w+) by (\w+)", command)

        self.row = int(match.group(1))
        self.by = int(match.group(2))

    def process(self, array):
        for _ in range(0, self.by):
            self._move_by_one_step(array)

    def _move_by_one_step(self, array):
        line = array[self.row]
        last = line[len(line) - 1]
        for i in reversed(range(0, len(line) - 1)):
            line[i + 1] = line[i]
        line[0] = last


class RotateColumnCommandProcessor(CommandProcessor):
    def __init__(self, command):
        match = re.fullmatch(r"rotate column x=(\w+) by (\w+)", command)

        self.column = int(match.group(1))
        self.by = int(match.group(2))

    def process(self, array):
        for _ in range(0, self.by):
            self._move_by_one_step(array)

    def _move_by_one_step(self, array):
        last = array[len(array) - 1][self.column]
        for i in reversed(range(0, len(array) - 1)):
            array[i + 1][self.column] = array[i][self.column]
        array[0][self.column] = last
