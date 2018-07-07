from .instructionconditiontype import InstructionConditionType
from .instructiontype import InstructionType
from .instructionwithcondition import InstructionWithCondition
from .registersspy import RegistersSpy


def test_instruction_with_true_condition_applies_value_on_registers():
    instruction = InstructionWithCondition(
        "a", InstructionType.INC, 10,
        "a", InstructionConditionType.EQUALS, 0)
    registers = RegistersSpy()

    instruction.apply_on_registers(registers)

    assert (("a", 10),) == registers.called_commands()


def test_instruction_with_false_condition_applies_nothing():
    instruction = InstructionWithCondition(
        "a", InstructionType.INC, 10,
        "a", InstructionConditionType.LESSER, 0)
    registers = RegistersSpy()

    instruction.apply_on_registers(registers)

    assert () == registers.called_commands()
