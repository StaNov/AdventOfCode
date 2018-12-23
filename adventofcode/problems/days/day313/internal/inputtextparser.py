from .oremine import OreMine
from adventofcode.problems.framework import DefaultInputTextParser


class InputTextParser(DefaultInputTextParser):
    def parse(self, input_string):
        return OreMine([])
