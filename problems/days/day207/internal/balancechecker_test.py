from . import balancechecker
from .program import Program


def test_is_balanced_single_program():
    assert balancechecker.is_balanced(Program("test", 1, []))
