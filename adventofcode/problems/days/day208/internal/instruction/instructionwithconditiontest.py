from .instructionconditiontype import InstructionConditionType
from .instructiontype import InstructionType
from .instructionwithcondition import InstructionWithCondition


class RegistersSpy:
    def __init__(self):
        self._called_name = None
        self._called_value = None

    def add(self, name, value):
        self._called_name = name
        self._called_value = value

    def called_with_name_and_value(self):
        return self._called_name, self._called_value


def test_instruction_with_true_condition_applies_value_on_registers():
    instruction = InstructionWithCondition(
        "a", InstructionType.INC, 10,
        "a", InstructionConditionType.EQUALS, 0)
    registers = RegistersSpy()

    instruction.apply_on_registers(registers)

    assert ("a", 10) == registers.called_with_name_and_value()
