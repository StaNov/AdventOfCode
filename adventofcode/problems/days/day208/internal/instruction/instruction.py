class Instruction:
    def __init__(self, applier):
        self._applier = applier

    def apply_on_registers(self, registers):
        self._applier.apply_on_registers(registers)
