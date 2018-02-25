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

    @property
    def value_to_apply(self):
        return self._applier(self._value_to_apply)
