from .direction import Direction
from .car import Car
from .oremine import OreMine
from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        cars = []

        for y, line in enumerate(input_string.splitlines()):
            for x, letter in enumerate(line):
                if letter == "^":
                    cars.append(Car((x, y), Direction.UP))

        return OreMine(cars)
