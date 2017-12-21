import pytest

from . import unbalancefinder
from .unbalancefinder import UnbalanceFinder
from .program import Program


@pytest.mark.skip
def test_three_programs_one_unbalanced():
    unbalanced_program = Program("unbalanced", 8, [])
    unbalanced_tree = Program("root", 1, [
        Program("balanced_1", 5, []),
        Program("balanced_2", 5, []),
        unbalanced_program,
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


@pytest.mark.skip
def test_three_programs_one_unbalanced_another():
    unbalanced_program = Program("unbalanced", 4, [])
    unbalanced_tree = Program("root", 1, [
        Program("balanced_1", 2, []),
        unbalanced_program,
        Program("balanced_2", 2, []),
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


def test_different_index_1():
    assert 1 == unbalancefinder._find_different_index([1, 2, 1, 1, 1, 1])


def test_different_index_2():
    assert 2 == unbalancefinder._find_different_index([4, 4, 6, 4, 4, 4])
