# -*- coding: utf-8 -*-

def solve(inputString):
    marshaller = Marshaller()

    for instruction in inputString.split(", "):
        if instruction[0] == 'R':
            marshaller.turn_right()

        if instruction[0] == 'L':
            marshaller.turn_left()

        marshaller.make_steps(int(instruction[1:]))

    return marshaller.steps_from_origin()


class Marshaller():

    def __init__(self):
        self._direction = Direction.up
        self._x = 0
        self._y = 0

    def turn_right(self):
        self._direction = (self._direction + 1) % 4

    def turn_left(self):
        self._direction = (self._direction - 1) % 4

    def make_steps(self, steps):
        if self._direction == Direction.up:
            self._y += steps
            return
        if self._direction == Direction.right:
            self._x += steps
            return
        if self._direction == Direction.down:
            self._y -= steps
            return
        if self._direction == Direction.left:
            self._x -= steps
            return

    def steps_from_origin(self):
        return abs(self._x) + abs(self._y)


class Direction():
    up = 0
    right = 1
    down = 2
    left = 3
