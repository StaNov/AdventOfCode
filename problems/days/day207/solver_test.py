import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


@pytest.mark.skip
def test_1_full_example(solver):
    input_ = [
        ("pbga", 66, []),
        ("xhth", 57, []),
        ("ebii", 61, []),
        ("havc", 66, []),
        ("ktlj", 57, []),
        ("fwft", 72, ["ktlj", "cntj", "xhth"]),
        ("qoyq", 66, []),
        ("padx", 45, ["pbga", "havc", "qoyq"]),
        ("tknk", 41, ["ugml", "padx", "fwft"]),
        ("jptl", 61, []),
        ("ugml", 68, ["gyxo", "ebii", "jptl"]),
        ("gyxo", 61, []),
        ("cntj", 57, []),
    ]
    assert "tknk" == solver.solve_1(input_)


def test_2_full_example(solver):
    # TODO
    # assert 0 == solver.solve_2("test test")
    pass
