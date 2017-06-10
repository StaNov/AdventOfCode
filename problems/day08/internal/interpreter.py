import re


class Interpreter:
    def __init__(self):
        self.max_size = 0

    def command(self, line):
        match = re.fullmatch("rect (\w+)x(\w+)", line)
        size = int(match.group(1)) * int(match.group(2))
        if size > self.max_size:
            self.max_size = size

    def get_lightens(self):
        return self.max_size
