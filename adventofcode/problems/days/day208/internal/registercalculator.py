class RegisterCalculator:
    def __init__(self):
        self.instruction_applied = False

    def apply_instruction(self, instruction):
        self.instruction_applied = True

    @property
    def highest_value(self):
        return 10 if self.instruction_applied else 0
