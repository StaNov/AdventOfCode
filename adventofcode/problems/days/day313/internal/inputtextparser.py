from .direction import Direction
from .car import Car
from .oremine import OreMine
from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        cars = []

        if input_string:
            cars.append(Car((0, 0), Direction.UP))

        return OreMine(cars)
