from . import applier


class Instruction:
    def __init__(self,
                 register_name,
                 instruction_type,
                 value_to_apply):
        self.register_name = register_name
        # TODO only for testing, can be removed somehow?
        self._instruction_type = instruction_type
        self._applier = applier.get_applier_for_instruction_type(instruction_type)
        self._value_to_apply = value_to_apply

    def apply_on_registers(self, registers):
        value_to_apply = self._applier(self._value_to_apply)
        registers.add(self.register_name, value_to_apply)
