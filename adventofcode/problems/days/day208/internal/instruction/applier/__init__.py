from . import incremental, decremental
from .applier import Applier
from ..instructiontype import InstructionType

_value_to_apply_processors = {
    InstructionType.INC: incremental.apply,
    InstructionType.DEC: decremental.apply,
}


def get_applier_for_instruction_type(register_name, instruction_type, value_to_apply):
    value_to_apply_processor = _value_to_apply_processors[instruction_type]

    return Applier(
        register_name,
        value_to_apply_processor(value_to_apply)
    )
