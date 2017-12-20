import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


TEST_INPUT = [
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


def test_1_full_example(solver):
    assert "tknk" == solver.solve_1(TEST_INPUT)


@pytest.mark.skip
def test_2_full_example(solver):
    assert 60 == solver.solve_2(TEST_INPUT)
