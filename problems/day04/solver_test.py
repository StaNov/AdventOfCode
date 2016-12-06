from .solver import Solver


def test_1_1():
    test_input = (
        "aaaaa-bbb-z-y-x-123[abxyz]\n"
        "a-b-c-d-e-f-g-h-987[abcde]\n"
        "not-a-real-room-404[oarel]\n"
        "totally-real-room-200[decoy]"
    )
    assert Solver.solve_1(test_input) == 1514


def test_2_1():
    # TODO assert Solver.solve_2("test test") == 0
    pass
