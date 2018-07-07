from .instruction import InstructionType
from .instructionfactory import InstructionFactory


def test_create_instruction():
    instruction = InstructionFactory().create_instruction("register_name", InstructionType.INC, 10)

    assert "register_name" == instruction._register_name
    assert InstructionType.INC == instruction._instruction_type
    assert 10 == instruction._value_to_apply
