from . import ProgramTreeCreator


def test_one_program_is_root():
    tree = ProgramTreeCreator([("test", 123, [])])
    assert "test" == tree.root_program.name


def test_root_of_one_nested_program():
    tree = ProgramTreeCreator([("test", 123, []), ("root_of_test", 456, ["test"])])
    assert "root_of_test" == tree.root_program.name


def test_root_of_one_nested_program_root_is_first():
    tree = ProgramTreeCreator([("leaf", 987, []), ("root", 456, ["middle"]), ("middle", 123, ["leaf"])])
    assert "root" == tree.root_program.name


def test_root_of_two_programs():
    tree = ProgramTreeCreator([("root", 987, ["leaf_1", "leaf_2"]), ("leaf_1", 456, []), ("leaf_2", 123, [])])
    assert "root" == tree.root_program.name
