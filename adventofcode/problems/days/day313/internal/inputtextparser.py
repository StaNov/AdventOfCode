from .roadtype import RoadType
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

_roads_map = {
    "\\": RoadType.LEFT_TO_UP,
}


class InputTextParser(DefaultInputTextParser):
    def __init__(self):
        self.cars = []
        self.roads = []

    def parse(self, input_string):
        for y, line in enumerate(input_string.splitlines()):
            for x, letter in enumerate(line):
                self._process_letter(letter, (x, y))

        return OreMine(self.cars, self.roads)

    def _process_letter(self, letter, position):
        if letter in _directions_map.keys():
            direction = _directions_map[letter]
            self.cars.append(Car(position, direction))

        if letter in _roads_map.keys():
            road = (position, _roads_map[letter])
            self.roads.append(road)
