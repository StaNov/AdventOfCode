from ..parsedinput import Instruction


class RegisterCalculator:
    def __init__(self):
        self.registers = {}

    def apply_instruction(self, instruction: Instruction):
        if instruction.register_name not in self.registers.keys():
            self.registers[instruction.register_name] = 0

        if instruction.condition_register not in self.registers.keys():
            self.registers[instruction.condition_register] = 0

        condition_register_value = self.registers[instruction.condition_register]

        if condition_register_value >= instruction.condition_value and instruction.condition_type == Instruction.ConditionType.LESSER:
            return

        # TODO refactor - call the instruction or some instruction applier
        if instruction.type == Instruction.Type.INC:
            self.registers[instruction.register_name] += instruction.value_to_apply
        elif instruction.type == Instruction.Type.DEC:
            self.registers[instruction.register_name] -= instruction.value_to_apply

    @property
    def highest_value(self):
        return max(self.registers.values(), default=0)
