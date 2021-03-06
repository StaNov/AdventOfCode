from . import unbalancefinder
from .program import Program
from .unbalancefinder import UnbalanceFinder


def test_three_programs_one_unbalanced():
    unbalanced_program = Program("unbalanced", 8, [])
    unbalanced_tree = Program("root", 1, [
        Program("balanced_1", 5, []),
        Program("balanced_2", 5, []),
        unbalanced_program,
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


def test_three_programs_one_unbalanced_another():
    unbalanced_program = Program("unbalanced", 4, [])
    unbalanced_tree = Program("root", 1, [
        Program("balanced_1", 2, []),
        unbalanced_program,
        Program("balanced_2", 2, []),
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


def test_three_programs_under_middle_ones():
    unbalanced_program = Program("unbalanced", 10, [])
    unbalanced_tree = Program("root", 1, [
        Program("middle_1", 2, [
            Program("middle_2", 3, [
                Program("middle_3", 3, [
                    Program("balanced_1", 4, []),
                    unbalanced_program,
                    Program("balanced_2", 4, []),
                ])
            ])
        ])
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


def test_unbalanced_among_balanced_ones():
    unbalanced_program = Program("unbalanced", 10, [])
    unbalanced_tree = Program("root", 1, [
        Program("middle_1", 10, [
            Program("balanced_1_1", 5, []),
            Program("balanced_1_2", 5, []),
            Program("balanced_1_3", 5, []),
        ]),
        Program("middle_2", 3, [
            Program("balanced_2_1", 6, []),
            Program("balanced_2_2", 6, []),
            unbalanced_program,
        ]),
        Program("middle_3", 1, [
            Program("balanced_3_1", 8, []),
            Program("balanced_3_2", 8, []),
            Program("balanced_3_3", 8, []),
        ]),
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


def test_unbalanced_with_balanced_children():
    unbalanced_program = Program("unbalanced", 10, [
        Program("balanced_1", 6, []),
        Program("balanced_1", 6, []),
        Program("balanced_1", 6, []),
    ])

    unbalanced_tree = Program("root", 1, [
        unbalanced_program,
        Program("middle_2", 2, []),
        Program("middle_3", 2, []),
    ])

    assert unbalanced_program is UnbalanceFinder(unbalanced_tree).find_unbalanced_program()


def test_get_correct_weight_of_unbalanced_program():
    program = Program("unbalanced", 10, [
        Program("test_1", 6, []),
        Program("test_2", 6, []),
        Program("test_3", 8, []),
    ])

    assert 6 == UnbalanceFinder(program).get_correct_weight_of_unbalanced_program()


def test_get_correct_weight_of_unbalanced_program_with_nested():
    program = Program("unbalanced", 10, [
        Program("balanced_1", 5, [
            Program("nested_1_1", 2, []),
            Program("nested_1_2", 2, []),
            Program("nested_1_3", 2, []),
        ]),
        Program("unbalanced", 20, [
            Program("nested_2_1", 1, []),
            Program("nested_2_2", 1, []),
            Program("nested_2_3", 1, []),
        ]),
        Program("balanced_2", 2, [
            Program("nested_3_1", 3, []),
            Program("nested_3_2", 3, []),
            Program("nested_3_3", 3, []),
        ]),
    ])

    assert 8 == UnbalanceFinder(program).get_correct_weight_of_unbalanced_program()


def test_get_unbalanced_subprogram_empty_list():
    assert None is unbalancefinder._get_unbalanced_subprogram([])


def test_get_unbalanced_subprogram():
    unbalanced_program = Program("unbalanced", 5, [
        Program("test_1", 3, []),
        Program("test_2", 3, []),
        Program("test_3", 4, []),
    ])

    assert unbalanced_program is unbalancefinder._get_unbalanced_subprogram([unbalanced_program])


def test_get_unbalanced_subprogram_balanced():
    balanced_program = Program("unbalanced", 5, [
        Program("test_1", 3, []),
        Program("test_2", 3, []),
        Program("test_3", 3, []),
    ])

    assert None is unbalancefinder._get_unbalanced_subprogram([balanced_program])


def test_different_index_1():
    assert 1 == unbalancefinder._find_different_index([1, 2, 1, 1, 1, 1])


def test_different_index_2():
    assert 2 == unbalancefinder._find_different_index([4, 4, 6, 4, 4, 4])


def test_get_parent_of_program():
    searched_program = Program("searched", 1, [])
    parent = Program("parent", 1, [searched_program])
    root = Program("test_1", 1, [
        Program("test_2", 1, [
            Program("test_3", 1, [
                Program("test_4", 1, []),
                parent
            ])
        ])
    ])

    assert parent is unbalancefinder._get_parent_of_program(searched_program, root)
