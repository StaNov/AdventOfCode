from .instruction import Applier
from .instruction import InstructionWithCondition
from .instruction import Instruction


class InstructionFactory:
    @staticmethod
    def create_instruction(register_name, instruction_type, value_to_apply):
        applier = Applier(register_name, instruction_type, value_to_apply)
        return Instruction(applier)

    @staticmethod
    def create_instruction_with_condition(
        register_name,
        instruction_type,
        value_to_apply,
        condition_register_name,
        condition_type,
        condition_value
    ):
        return InstructionWithCondition(
            register_name,
            instruction_type,
            value_to_apply,
            condition_register_name,
            condition_type,
            condition_value
        )
