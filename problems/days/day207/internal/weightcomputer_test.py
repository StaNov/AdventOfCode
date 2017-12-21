from . import weightcomputer
from .program import Program


def test_weight_single_program():
    assert 2 == weightcomputer.weight_of(Program("test", 2, []))


def test_weight_multiple_subprograms():
    program = Program("test", 2, [
        Program("test_child", 3, []),
        Program("test_child_2", 5, [
            Program("test_child_3", 4, [])
        ]),
    ])

    assert 2 + 3 + 5 + 4 == weightcomputer.weight_of(program)
