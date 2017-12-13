from .trampolinemaze import TrampolineMaze


class TrampolineMazeDecrementing(TrampolineMaze):
    def _value_to_add_to_source_item(self, jump_distance):
        return 1 if jump_distance < 3 else -1
