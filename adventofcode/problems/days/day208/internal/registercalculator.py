from ..parsedinput import Instruction


class RegisterCalculator:
    def __init__(self):
        self.registers = {}

    def apply_instruction(self, instruction: Instruction):
        if instruction.register_name not in self.registers.keys():
            self.registers[instruction.register_name] = 0

        self.registers[instruction.register_name] += instruction.value_to_apply

    @property
    def highest_value(self):
        return max(self.registers.values(), default=0)
