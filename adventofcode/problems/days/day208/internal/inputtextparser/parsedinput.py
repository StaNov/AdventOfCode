from adventofcode.problems.days.day208.internal.instruction import InstructionWithCondition


class ParsedInput:
    def __init__(self):
        self._instructions = []

    def add_instruction(self,
                        register_name,
                        instruction_type,
                        value_to_apply,
                        condition_register,
                        condition_type,
                        condition_value):
        self._instructions.append(InstructionWithCondition(
            register_name,
            instruction_type,
            value_to_apply,
            condition_register,
            condition_type,
            condition_value))

    @property
    def instructions(self):
        return tuple(self._instructions)
