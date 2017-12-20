from .program import Program


class ProgramTree:
    def __init__(self, input_):
        self._root = None

        # TODO extract to method
        programs = {}

        while input_:
            processed_program = input_.pop(0)
            name, weight, subprograms = processed_program

            if set(subprograms) <= set(programs.keys()):
                new_program = Program(name, weight, [programs[subprogram_name] for subprogram_name in subprograms])
                programs[name] = new_program
                if not self._root or self._root.name in subprograms:
                    self._root = new_program
            else:
                input_.append(processed_program)

    def get_root_program_name(self):
        return self._root.name
