from .instruction import InstructionConditionType, InstructionWithCondition
from .registers import Registers


class RegisterCalculator:
    def __init__(self):
        self._registers = Registers()

    def apply_instruction(self, instruction: InstructionWithCondition):
        if not self.condition_is_met(instruction):
            return

        self._registers.add(instruction.register_name, instruction.value_to_apply)

    def condition_is_met(self, instruction):
        return (self._registers.get(instruction.condition_register) < instruction.condition_value
                or instruction.condition_type != InstructionConditionType.LESSER)

    @property
    def highest_value(self):
        values = [value for _, value in self._registers.registers]
        return max(values, default=0)
