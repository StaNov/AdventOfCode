from . import Keyboard, KeyboardAdvanced
import pytest


def test_get_key():
    keyboard = Keyboard((0, 0))
    assert keyboard.get_key() == "1"


def test_out_of_range():
    with pytest.raises(ValueError):
        Keyboard((20, 20))

    with pytest.raises(ValueError):
        Keyboard((-1, 1))


def test_advanced_get_key():
    keyboard = KeyboardAdvanced((2, 3))
    assert keyboard.get_key() == "8"


def test_advanced_out_of_range():
    with pytest.raises(ValueError):
        KeyboardAdvanced((0, 0))
