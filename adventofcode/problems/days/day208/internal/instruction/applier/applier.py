from . import incremental, decremental
from ..instructiontype import InstructionType

_value_to_apply_processors = {
    InstructionType.INC: incremental.apply,
    InstructionType.DEC: decremental.apply,
}


class Applier:
    def __init__(self, register_name, instruction_type, value_to_apply) -> None:
        value_to_apply_processor = _value_to_apply_processors[instruction_type]

        self._register_name = register_name
        self._value_to_apply = value_to_apply_processor(value_to_apply)

    def apply_on_registers(self, registers):
        registers.add(self._register_name, self._value_to_apply)
