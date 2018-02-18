from .instruction import InstructionWithCondition


class ParsedInput:
    def __init__(self):
        self.instructions = []

    def add_instruction(self,
                        register_name,
                        instruction_type,
                        value_to_apply,
                        condition_register,
                        condition_type,
                        condition_value):
        self.instructions.append(InstructionWithCondition(
            register_name,
            instruction_type,
            value_to_apply,
            condition_register,
            condition_type,
            condition_value))
