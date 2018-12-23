from .direction import Direction
from .car import Car
from .oremine import OreMine
from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        cars = []

        if input_string:
            position = (0, 0) if len(input_string) == 1 else (2, 1)
            cars.append(Car(position, Direction.UP))

        return OreMine(cars)
