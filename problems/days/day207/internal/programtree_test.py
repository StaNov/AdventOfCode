from . import ProgramTree


def test_helper_method():
    tree = ProgramTree({"test": (123, [])})
    assert "test" == tree.get_root_program()
