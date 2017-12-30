from .program import Program


def test_program_to_string():
    leaf_1 = Program("leaf_1", 456, [])
    leaf_2 = Program("leaf_2", 123, [])
    root = Program("root", 987, [leaf_1, leaf_2])

    assert "root (987) -> ['leaf_1', 'leaf_2']" == str(root)
