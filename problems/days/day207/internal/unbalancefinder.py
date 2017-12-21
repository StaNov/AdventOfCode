from . import weightcomputer


class UnbalanceFinder:

    def __init__(self, root_program):
        self._root = root_program

    def find_unbalanced_program(self):
        current_root = self._root

        while current_root.subprograms and current_root.subprograms[0].subprograms:
            current_root = current_root.subprograms[0]

        subprogram_weights = [weightcomputer.weight_of(subprogram) for subprogram in current_root.subprograms]
        different_index = _find_different_index(subprogram_weights)
        return current_root.subprograms[different_index]


def _find_different_index(list_):
    first = list_[0]
    second = list_[1]
    third = list_[2]

    if first == second:
        good_one = first
    else:
        good_one = third

    for i, item in enumerate(list_):
        if item != good_one:
            return i
