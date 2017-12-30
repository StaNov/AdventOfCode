from . import balancechecker
from . import weightcomputer


class UnbalanceFinder:

    def __init__(self, root_program):
        self._root = root_program

    def find_unbalanced_program(self):
        current_root = self._root

        while _get_unbalanced_subprogram(current_root.subprograms):
            current_root = _get_unbalanced_subprogram(current_root.subprograms)

        subprogram_weights = [weightcomputer.weight_of(subprogram) for subprogram in current_root.subprograms]
        different_index = _find_different_index(subprogram_weights)
        return current_root.subprograms[different_index]

    def get_correct_weight_of_unbalanced_program(self):
        unbalanced_program = self.find_unbalanced_program()
        siblings = _get_parent_of_program(unbalanced_program, self._root).subprograms
        balanced_sibling = siblings[0] if siblings[0] is not unbalanced_program else siblings[1]
        correct_total_weight = weightcomputer.weight_of(balanced_sibling)
        unbalanced_program_weight = weightcomputer.weight_of(unbalanced_program)

        return unbalanced_program.weight + (correct_total_weight - unbalanced_program_weight)


def _get_unbalanced_subprogram(subprograms):
    for subprogram in subprograms:
        if not balancechecker.is_balanced(subprogram):
            return subprogram

    return None


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


def _get_parent_of_program(program, root):
    for p in root.subprograms:
        if p is program:
            return root

        recursive_parent = _get_parent_of_program(program, p)

        if recursive_parent:
            return recursive_parent

    return None
