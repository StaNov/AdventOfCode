from . import weightcomputer


def is_balanced(program):
    subprogram_weights = [weightcomputer.weight_of(subprogram) for subprogram in program.subprograms]
    subprograms_balanced = [is_balanced(subprogram) for subprogram in program.subprograms]

    return all(subprograms_balanced) and _all_weights_are_the_same(subprogram_weights)


def _all_weights_are_the_same(subprogram_weights):
    return len(set(subprogram_weights)) <= 1
