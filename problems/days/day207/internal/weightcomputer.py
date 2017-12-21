def weight_of(program):
    result = program.weight

    for subprogram in program.subprograms:
        result += weight_of(subprogram)

    return result
