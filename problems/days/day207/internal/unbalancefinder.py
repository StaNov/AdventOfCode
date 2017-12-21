from . import weightcomputer


class UnbalanceFinder:

    def __init__(self, root_program):
        self._root = root_program

    def find_unbalanced_program(self):
        subprogram_weights = [weightcomputer.weight_of(subprogram) for subprogram in self._root.subprograms]
        different_index = _find_different_index(subprogram_weights)
        return self._root.subprograms[different_index]


def _find_different_index(list):
    first = list[0]
    second = list[1]
    third = list[2]

    if first == second:
        good_one = first
    else:
        good_one = third

    for i, item in enumerate(list):
        if item != good_one:
            return i
