from .internal import Marshaller, MarshallerController, PositionRecorder


class Solver:
    @staticmethod
    def solve_1(input_string):
        marshaller = Marshaller()
        controller = MarshallerController(marshaller)

        for instruction in input_string.split(", "):
            controller.execute_instruction(instruction)

        return marshaller.steps_from_start()

    @staticmethod
    def solve_2(input_string):
        marshaller = Marshaller()
        controller = MarshallerController(marshaller)
        recorder = PositionRecorder()

        for instruction in input_string.split(", "):
            controller.execute_instruction(instruction)

            current_position = marshaller.current_position()
            already_visited = recorder.record(current_position)

            if already_visited is not None:
                return abs(already_visited[0]) + abs(already_visited[1])