from .unbalancefinder import UnbalanceFinder
from .program import Program


def test_three_programs_one_unbalanced():
    unbalanced_tree = Program("root", 1, [
        Program("balanced_1", 5, []),
        Program("balanced_2", 5, []),
        Program("unbalanced", 8, []),
    ])

    assert 5 == UnbalanceFinder(unbalanced_tree).find_balanced_value()
