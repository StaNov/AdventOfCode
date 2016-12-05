from .solver import Solver


def test_1_1():
    assert Solver.solve_1("4 5 6\n7 8 9\n5 10 25") == 2


def test_2_1():
    input_ = "101 201 301\n102 202 302\n103 203 303\n401 501 601\n402 502 602\n403 503 1"
    assert Solver.solve_2(input_) == 5
