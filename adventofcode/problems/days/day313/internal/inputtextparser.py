from .direction import Direction
from .car import Car
from .oremine import OreMine
from adventofcode.problems.framework import DefaultInputTextParser

_directions_map = {
    "^": Direction.UP,
    "v": Direction.DOWN,
    ">": Direction.RIGHT,
    "<": Direction.LEFT,
}


class InputTextParser(DefaultInputTextParser):
    def __init__(self):
        self.cars = []

    def parse(self, input_string):
        for y, line in enumerate(input_string.splitlines()):
            for x, letter in enumerate(line):
                self.process_letter(letter, (x, y))

        return OreMine(self.cars)

    def process_letter(self, letter, position):
        if letter not in _directions_map.keys():
            return

        direction = _directions_map[letter]
        self.cars.append(Car(position, direction))
