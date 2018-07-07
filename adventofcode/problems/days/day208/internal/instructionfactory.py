from .instruction import Instruction


class InstructionFactory:
    def create_instruction(self, register_name, instruction_type, value):
        return Instruction(register_name, instruction_type, None)
