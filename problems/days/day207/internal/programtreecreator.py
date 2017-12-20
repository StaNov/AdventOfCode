from .program import Program


class ProgramTreeCreator:
    def __init__(self, input_):
        self._root = None
        self._input_to_process = input_
        self._create_program_tree()

    def get_root_program_name(self):
        return self._root.name

    def _create_program_tree(self):
        created_programs = {}

        while self._input_to_process:
            current_input = self._input_to_process.pop(0)
            current_name, current_weight, current_subprograms = current_input

            if set(current_subprograms) <= set(created_programs.keys()):
                new_program = Program(current_name, current_weight, [created_programs[subprogram_name] for subprogram_name in current_subprograms])
                created_programs[current_name] = new_program

                if not self._root or self._root.name in current_subprograms:
                    self._root = new_program
            else:
                self._input_to_process.append(current_input)
