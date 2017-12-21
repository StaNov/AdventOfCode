import pytest

from . import balancechecker
from .program import Program


def test_is_balanced_single_program():
    assert balancechecker.is_balanced(Program("test", 1, []))


def test_is_balanced_two_programs_unbalanced():
    program = Program("root", 1, [
        Program("child_1", 2, []),
        Program("child_2", 3, []),
    ])

    assert not balancechecker.is_balanced(program)


@pytest.mark.skip
def test_is_balanced_nested_subprograms():
    program = Program("root", 1, [
        Program("child_1", 6, [
            Program("child_1_1", 3, []),
            Program("child_1_2", 3, []),
            Program("child_1_3", 3, []),
        ]),
        Program("child_2", 3, [
            Program("child_1_1", 4, []),
            Program("child_1_2", 4, []),
            Program("child_1_3", 4, []),
        ]),
    ])

    assert balancechecker.is_balanced(program)
