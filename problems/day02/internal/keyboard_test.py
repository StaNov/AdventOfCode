from .keyboard import Keyboard
import pytest


def test_get_key():
    keyboard = Keyboard(8)
    assert keyboard.get_key() == 8


def test_out_of_range():
    with pytest.raises(ValueError):
        keyboard = Keyboard(20)
