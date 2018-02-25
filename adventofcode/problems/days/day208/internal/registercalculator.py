from .instruction import Instruction
from .registers import Registers


class RegisterCalculator:
    def __init__(self):
        self._registers = Registers()

    def apply_instruction(self, instruction: Instruction):
        instruction.apply_on_registers(self._registers)

    @property
    def highest_value(self):
        values = [value for _, value in self._registers.registers]
        return max(values, default=0)
