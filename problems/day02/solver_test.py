from .solver import Solver


def test_1_1():
    assert Solver.solve_1("ULL\nRRDDD\nLURDL\nUUUUD") == "1985"


def test_2_1():
    assert Solver.solve_2("ULL\nRRDDD\nLURDL\nUUUUD") == "5DB3"
