from . import incremental, decremental
from ..instructiontype import InstructionType


def get_applier_for_instruction_type(instruction_type):
    appliers = {
        InstructionType.INC: incremental.apply,
        InstructionType.DEC: decremental.apply,
    }
    return appliers[instruction_type]
