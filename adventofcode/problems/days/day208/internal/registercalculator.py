from ..parsedinput import Instruction


class RegisterCalculator:
    def __init__(self):
        self.max_value = 0

    def apply_instruction(self, instruction: Instruction):
        self.max_value = max(self.max_value, instruction.value_to_apply)

    @property
    def highest_value(self):
        return self.max_value
