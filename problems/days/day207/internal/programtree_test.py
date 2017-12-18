import pytest

from . import ProgramTree


def test_one_program_is_root():
    tree = ProgramTree([("test", 123, [])])
    assert "test" == tree.get_root_program_name()


def test_root_of_one_nested_program():
    tree = ProgramTree([("test", 123, []), ("root_of_test", 456, ["test"])])
    assert "root_of_test" == tree.get_root_program_name()


def test_root_of_one_nested_program_root_is_first():
    tree = ProgramTree([("leaf", 987, []), ("root", 456, ["middle"]), ("middle", 123, ["leaf"])])
    assert "root" == tree.get_root_program_name()


@pytest.mark.skip
def test_root_of_two_programs():
    tree = ProgramTree([("root", 987, ["leaf_1, leaf_2"]), ("leaf_1", 456, []), ("leaf_1", 123, [])])
    assert "root" == tree.get_root_program_name()