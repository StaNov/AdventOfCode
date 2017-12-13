from .trampolinemaze import TrampolineMaze


class TrampolineMazeDecrementing(TrampolineMaze):
    def _value_to_add_to_source_item(self):
        return -1
