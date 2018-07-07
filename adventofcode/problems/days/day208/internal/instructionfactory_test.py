from .instruction import InstructionConditionType
from .instruction import InstructionType
from .instructionfactory import InstructionFactory


def test_create_instruction():
    instruction = InstructionFactory().create_instruction("register_name", InstructionType.INC, 10)

    assert "register_name" == instruction._register_name
    assert InstructionType.INC == instruction._instruction_type
    assert 10 == instruction._value_to_apply


def test_create_instruction_with_condition():
    instruction = InstructionFactory().create_instruction_with_condition(
        "register_name",
        InstructionType.INC,
        10,
        "condition_register_name",
        InstructionConditionType.LESSER,
        20
    )

    assert "register_name" == instruction._register_name
    assert InstructionType.INC == instruction._instruction_type
    assert 10 == instruction._value_to_apply
    assert "condition_register_name" == instruction._condition_register
    assert InstructionConditionType.LESSER == instruction._condition_type
    assert 20 == instruction._condition_value
