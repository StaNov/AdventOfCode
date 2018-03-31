from .applier import Applier
from ..instructiontype import InstructionType
from ..registersspy import RegistersSpy


def test_value_is_applied_to_registers():
    applier = Applier("a", InstructionType.INC, 10)
    registers = RegistersSpy()

    applier.apply_on_registers(registers)

    assert ("a", 10) == registers.called_with_name_and_value()