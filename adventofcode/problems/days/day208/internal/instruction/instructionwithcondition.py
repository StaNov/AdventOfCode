from .instruction import Instruction


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
