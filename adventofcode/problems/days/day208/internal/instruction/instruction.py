from . import applier


class Instruction:
    def __init__(self,
                 register_name,
                 instruction_type,
                 value_to_apply):
        self._applier = applier.get_applier_for_instruction_type(register_name, instruction_type, value_to_apply)

        # TODO only for testing, can be removed somehow?
        self.register_name = register_name
        self._instruction_type = instruction_type
        self._value_to_apply = value_to_apply

    def apply_on_registers(self, registers):
        self._applier.apply_on_registers(registers)
