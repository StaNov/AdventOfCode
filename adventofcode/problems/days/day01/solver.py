from adventofcode.problems.utils import AbstractSolver
from .internal import Marshaller, MarshallerController, PositionRecorder


class Solver(AbstractSolver):
    def __init__(self):
        super().__init__()
        self.marshaller = Marshaller()
        self.controller = MarshallerController(self.marshaller)
        self.recorder = PositionRecorder()

    def _solve_1_internal(self, input_):
        for instruction in input_.split(", "):
            self.controller.execute_instruction(instruction)

        return self.marshaller.steps_from_start()

    def _solve_2_internal(self, input_):
        for instruction in input_.split(", "):
            self.controller.execute_instruction(instruction)

            current_position = self.marshaller.current_position()
            already_visited = self.recorder.record(current_position)

            if already_visited is not None:
                return abs(already_visited[0]) + abs(already_visited[1])
