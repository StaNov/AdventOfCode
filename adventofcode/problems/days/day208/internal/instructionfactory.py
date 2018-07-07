from .instruction import Instruction


class InstructionFactory:
    @staticmethod
    def create_instruction(register_name, instruction_type, value_to_apply):
        return Instruction(register_name, instruction_type, value_to_apply)
