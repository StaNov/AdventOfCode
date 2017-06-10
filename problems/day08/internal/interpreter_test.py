import pytest

from . import Interpreter


@pytest.fixture
def interpreter():
    return Interpreter(7, 3)


def test_1_one_rect(interpreter):
    interpreter.command("rect 3x2")
    assert interpreter.get_lightens() == 6


def test_1_two_rects_the_same(interpreter):
    interpreter.command("rect 3x2")
    interpreter.command("rect 3x2")
    assert interpreter.get_lightens() == 6


def test_1_two_rects_second_bigger(interpreter):
    interpreter.command("rect 3x2")
    interpreter.command("rect 4x3")
    assert interpreter.get_lightens() == 12


def test_1_two_rects_second_smaller(interpreter):
    interpreter.command("rect 3x2")
    interpreter.command("rect 1x1")
    assert interpreter.get_lightens() == 6


def test_1_two_rects_non_inclusive(interpreter):
    interpreter.command("rect 3x2")
    interpreter.command("rect 2x3")
    assert interpreter.get_lightens() == 8


def test_1_three_rects(interpreter):
    interpreter.command("rect 3x2")
    interpreter.command("rect 2x3")
    interpreter.command("rect 5x1")
    assert interpreter.get_lightens() == 10


def test_1_unknown_command(interpreter):
    with pytest.raises(Exception):
        interpreter.command("unknown command")


def test_with_exception():
    # TODO
    with pytest.raises(Exception):
        raise Exception("Test exception in test")
