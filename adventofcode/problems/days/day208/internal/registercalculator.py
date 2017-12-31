from ..parsedinput import Instruction


class RegisterCalculator:
    def __init__(self):
        self.value_applied = 0

    def apply_instruction(self, instruction: Instruction):
        self.value_applied = instruction.value_to_apply

    @property
    def highest_value(self):
        return self.value_applied
