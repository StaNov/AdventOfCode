from . import weightcomputer
from .program import Program


def test_weight_single_program():
    assert 2 == weightcomputer.weight_of(Program("test", 2, []))
