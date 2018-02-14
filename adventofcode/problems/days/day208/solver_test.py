import pytest

from .internal import ParsedInput, InstructionType, InstructionConditionType
from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def test_input():
    parsed_input = ParsedInput()

    parsed_input.add_instruction("b", InstructionType.INC, 5, "a", InstructionConditionType.GREATER, 1)
    parsed_input.add_instruction("a", InstructionType.INC, 1, "b", InstructionConditionType.LESSER, 5)
    parsed_input.add_instruction("c", InstructionType.DEC, -10, "a", InstructionConditionType.GREATER_EQUALS, 1)
    parsed_input.add_instruction("c", InstructionType.INC, -20, "c", InstructionConditionType.EQUALS, 10)

    return parsed_input


# TODO
@pytest.mark.skip
def test_1_full_example(solver, test_input):
    assert 1 == solver.solve_1(test_input)


# TODO
@pytest.mark.skip
def test_2_full_example(solver, test_input):
    # TODO
    assert 0 == solver.solve_2("test test")
