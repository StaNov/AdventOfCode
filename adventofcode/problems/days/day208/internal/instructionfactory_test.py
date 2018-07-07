from .instruction import InstructionType
from .instructionfactory import InstructionFactory


def test_create_instruction():
    instruction = InstructionFactory().create_instruction("register_name", InstructionType.INC, 10)
    assert "register_name" == instruction._register_name
