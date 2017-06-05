from .solver import Solver


def test_1_1():
    # TODO it is not very clean to call one Solver with arguments for only one call, or is it?
    assert Solver("R2, L3").solve_1() == 5


def test_1_2():
    assert Solver("R2, R2, R2").solve_1() == 2


def test_1_3():
    assert Solver("R5, L5, R5, R3").solve_1() == 12


def test_2_1():
    assert Solver("R8, R4, R4, R8").solve_2() == 4
