from .solver import Solver


def test_1_1():
    assert Solver.solve_1("ULL\nRRDDD\nLURDL\nUUUUD") == 0  # 1985 # TODO


def test_2_1():
    assert Solver.solve_2("test test") == 0
