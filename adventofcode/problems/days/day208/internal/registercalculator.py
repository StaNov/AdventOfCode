from .parsedinput import Instruction
from .registers import Registers


class RegisterCalculator:
    def __init__(self):
        self._registers = Registers()

    def apply_instruction(self, instruction: Instruction):
        if not self.condition_is_met(instruction):
            return

        # TODO refactor - call the instruction or some instruction applier
        value_to_apply = instruction.value_to_apply
        if instruction.type == Instruction.Type.DEC:
            value_to_apply = - value_to_apply
            
        self._registers.add(instruction.register_name, value_to_apply)

    def condition_is_met(self, instruction):
        return (self._registers.get(instruction.condition_register) < instruction.condition_value
                or instruction.condition_type != Instruction.ConditionType.LESSER)

    @property
    def highest_value(self):
        values = [value for _, value in self._registers.registers]
        return max(values, default=0)
