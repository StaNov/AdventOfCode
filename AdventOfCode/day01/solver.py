# -*- coding: utf-8 -*-


def __init__():
    pass


def solve(input_string):
    marshaller = Marshaller()

    for instruction in input_string.split(", "):
        if instruction[0] == 'R':
            marshaller.turn_right()

        if instruction[0] == 'L':
            marshaller.turn_left()

        marshaller.make_steps(int(instruction[1:]))

    return marshaller.steps_from_start()


class Marshaller:

    def __init__(self):
        self._direction = Direction(Direction.up)
        self._x = 0
        self._y = 0

    def turn_left(self):
        self._direction.turn_left()

    def turn_right(self):
        self._direction.turn_right()

    def make_steps(self, steps):
        if self._direction.is_turned_to(Direction.up):
            self._y += steps
            return
        if self._direction.is_turned_to(Direction.right):
            self._x += steps
            return
        if self._direction.is_turned_to(Direction.down):
            self._y -= steps
            return
        if self._direction.is_turned_to(Direction.left):
            self._x -= steps
            return

    def steps_from_start(self):
        return abs(self._x) + abs(self._y)


class Direction:

    up = 0
    right = 1
    down = 2
    left = 3

    def __init__(self, direction):
        self._dir = direction

    def turn_left(self):
        self._dir = (self._dir - 1) % 4

    def turn_right(self):
        self._dir = (self._dir + 1) % 4

    def is_turned_to(self, direction):
        return self._dir == direction
