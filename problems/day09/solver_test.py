import pytest

from .solver import Solver


@pytest.fixture
def solver():
    return Solver()


def test_1_full_example_1(solver):
    assert solver.solve_1("ADVENT") == 6


def test_1_full_example_2(solver):
    assert solver.solve_1("A(1x5)BC") == 7


def test_1_full_example_3(solver):
    assert solver.solve_1("(3x3)XYZ") == 9


def test_1_full_example_4(solver):
    assert solver.solve_1("A(2x2)BCD(2x2)EFG") == 11


def test_1_full_example_5(solver):
    assert solver.solve_1("(6x1)(1x3)A") == 6


def test_1_full_example_6(solver):
    assert solver.solve_1("X(8x2)(3x3)ABCY") == 18


def test_1_1(solver):
    assert solver.solve_1("") == 0


def test_1_2(solver):
    assert solver.solve_1("A") == 1


def test_1_4(solver):
    with pytest.raises(Exception):
        solver.solve_1("A((")


def test_1_5(solver):
    assert solver.solve_1("(1x5)A") == 5


def test_1_6(solver):
    with pytest.raises(Exception):
        solver.solve_1("A(1x5")  # No closing parenthesis


def test_1_7(solver):
    with pytest.raises(Exception):
        solver.solve_1("A(2x5)A")  # Not enough input to read


@pytest.mark.skip  # TODO
def test_2_full_example_1(solver):
    assert solver.solve_2("(3x3)XYZ") == 9


@pytest.mark.skip  # TODO
def test_2_full_example_2(solver):
    assert solver.solve_2("X(8x2)(3x3)ABCY") == 20


@pytest.mark.skip  # TODO
def test_2_full_example_3(solver):
    assert solver.solve_2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920


@pytest.mark.skip  # TODO
def test_2_full_example_4(solver):
    assert solver.solve_2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445
