class MarshallerController:
    def __init__(self, marshaller):
        self._marshaller = marshaller

    def execute_instruction(self, instruction):
        if instruction[0] == 'R':
            self._marshaller.turn_right()

        if instruction[0] == 'L':
            self._marshaller.turn_left()

        self._marshaller.make_steps(int(instruction[1:]))


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

    def current_position(self):
        return self._x, self._y


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
