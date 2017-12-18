import pytest

from . import ProgramTree


def test_one_program_is_root():
    tree = ProgramTree(["test", 123, []])
    assert "test" == tree.get_root_program()


@pytest.mark.skip
def test_root_of_one_nested_program():
    tree = ProgramTree({"test": (123, []), "root_of_test": (456, ["test"])})
    assert "root_of_test" == tree.get_root_program()
