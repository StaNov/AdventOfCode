from .program import Program


class ProgramTreeCreator:
    def __init__(self, input_):
        self._root = None
        self._input_to_process = input_
        self._created_programs = {}

        self._create_program_tree()

    def _create_program_tree(self):
        while self._input_to_process:
            current_input = self._input_to_process.pop(0)
            current_subprograms = current_input[2]

            if self._all_subprograms_were_already_created(current_subprograms):
                self._create_new_program_and_update_root_if_needed(current_input)
            else:
                self._input_to_process.append(current_input)

    def _all_subprograms_were_already_created(self, subprograms_names):
        return set(subprograms_names) <= set(self._created_programs.keys())

    def _create_new_program_and_update_root_if_needed(self, input_):
        current_name, current_weight, current_subprograms = input_
        subprograms = [self._created_programs[subprogram_name] for subprogram_name in current_subprograms]

        new_program = Program(current_name, current_weight, subprograms)

        self._created_programs[new_program.name] = new_program

        if not self._root or self._root.name in current_subprograms:
            self._root = new_program

    @property
    def root_program(self):
        return self._root
