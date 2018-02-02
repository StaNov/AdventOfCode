from ..parsedinput import Instruction


class RegisterCalculator:
    def __init__(self):
        self._registers = {}

    def apply_instruction(self, instruction: Instruction):
        self.initialize_required_registers(instruction)

        if not self.condition_is_met(instruction):
            return

        # TODO refactor - call the instruction or some instruction applier
        if instruction.type == Instruction.Type.INC:
            self._registers[instruction.register_name] += instruction.value_to_apply
        elif instruction.type == Instruction.Type.DEC:
            self._registers[instruction.register_name] -= instruction.value_to_apply

    def initialize_required_registers(self, instruction):
        registers_to_initialize = instruction.register_name, instruction.condition_register

        for register_name in registers_to_initialize:
            if register_name not in self._registers.keys():
                self._registers[register_name] = 0

    def condition_is_met(self, instruction):
        return (self._registers[instruction.condition_register] < instruction.condition_value
                or instruction.condition_type != Instruction.ConditionType.LESSER)

    @property
    def highest_value(self):
        return max(self._registers.values(), default=0)
