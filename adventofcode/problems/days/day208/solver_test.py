import pytest

from .parsedinput import ParsedInput, Instruction
from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def test_input():
    parsed_input = ParsedInput()

    parsed_input.add_instruction("b", Instruction.Type.INC, 5, "a", Instruction.ConditionType.GREATER, 1)
    parsed_input.add_instruction("a", Instruction.Type.INC, 1, "b", Instruction.ConditionType.LESSER, 5)
    parsed_input.add_instruction("c", Instruction.Type.DEC, -10, "a", Instruction.ConditionType.GREATER_EQUALS, 1)
    parsed_input.add_instruction("c", Instruction.Type.INC, -20, "c", Instruction.ConditionType.EQUALS, 10)

    return parsed_input


def test_1_full_example(solver, test_input):
    # TODO
    assert 0 == solver.solve_1(test_input)


def test_2_full_example(solver, test_input):
    # TODO
    assert 0 == solver.solve_2("test test")
