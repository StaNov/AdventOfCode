from .solver import Solver


def test_1_1():
    test_input = (
        "4 5 6\n"
        "7 8 9\n"
        "5 10 25"
    )
    assert Solver.solve_1(test_input) == 2


def test_2_1():
    input_ = "101 201 301\n102 202 302\n103 203 303\n401 501 601\n402 502 602\n403 503 1"
    assert Solver.solve_2(input_) == 5
