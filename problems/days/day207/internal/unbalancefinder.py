from . import weightcomputer


class UnbalanceFinder:

    def __init__(self, root_program):
        self._root = root_program

    def find_unbalanced_program(self):
        subprogram_weights = [weightcomputer.weight_of(subprogram) for subprogram in self._root.subprograms]
        different_index = _find_different_index(subprogram_weights)
        return self._root.subprograms[different_index]


def _find_different_index(list):
    return 1
