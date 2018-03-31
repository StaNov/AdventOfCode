from .instruction import Instruction
from .instructionconditiontype import InstructionConditionType


class InstructionWithCondition(Instruction):
    def __init__(self,
                 register_name,
                 instruction_type,
                 value_to_apply,
                 condition_register,
                 condition_type,
                 condition_value):
        super().__init__(register_name, instruction_type, value_to_apply)
        self.condition_register = condition_register
        self.condition_type = condition_type
        self.condition_value = condition_value

    def apply_on_registers(self, registers):
        if not self._condition_is_met(registers):
            return

        super().apply_on_registers(registers)

    def _condition_is_met(self, registers):
        return (registers.get(self.condition_register) < self.condition_value
                or self.condition_type != InstructionConditionType.LESSER)