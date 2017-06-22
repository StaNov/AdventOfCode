from utils import AbstractSolver
from .internal import Marshaller, MarshallerController, PositionRecorder


class Solver(AbstractSolver):
    def __init__(self):
        self.marshaller = Marshaller()
        self.controller = MarshallerController(self.marshaller)
        self.recorder = PositionRecorder()

    def solve_1_internal(self, input_string):
        for instruction in input_string.split(", "):
            self.controller.execute_instruction(instruction)

        return self.marshaller.steps_from_start()

    def solve_2_internal(self, input_string):
        for instruction in input_string.split(", "):
            self.controller.execute_instruction(instruction)

            current_position = self.marshaller.current_position()
            already_visited = self.recorder.record(current_position)

            if already_visited is not None:
                return abs(already_visited[0]) + abs(already_visited[1])
