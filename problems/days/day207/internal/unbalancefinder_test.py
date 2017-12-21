import pytest

from .unbalancefinder import UnbalanceFinder
from .program import Program


def test_three_programs_one_unbalanced():
    unbalanced_program = Program("unbalanced", 8, [])
    unbalanced_tree = Program("root", 1, [
        Program("balanced_1", 5, []),
        Program("balanced_2", 5, []),
        unbalanced_program,
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


@pytest.mark.skip
def test_three_programs_under_one_middle():
    unbalanced_program = Program("unbalanced", 10, [])
    unbalanced_tree = Program("root", 1, [
        Program("middle", 2, [
            Program("balanced_1", 3, []),
            unbalanced_program,
            Program("balanced_2", 3, []),
        ])
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()
