from . import Keyboard, KeyboardController


def test_move_right():
    kb, ctrl = init(5)
    ctrl.move_right()
    assert kb.get_key() == 6
    ctrl.move_right()
    assert kb.get_key() == 6


def test_move_left():
    kb, ctrl = init(2)
    ctrl.move_left()
    assert kb.get_key() == 1
    ctrl.move_left()
    assert kb.get_key() == 1


def test_move_up():
    kb, ctrl = init(4)
    ctrl.move_up()
    assert kb.get_key() == 1
    ctrl.move_up()
    assert kb.get_key() == 1


def test_move_down():
    kb, ctrl = init(6)
    ctrl.move_down()
    assert kb.get_key() == 9
    ctrl.move_down()
    assert kb.get_key() == 9


def init(keyboard_key=5):
    kb = Keyboard(keyboard_key)
    ctrl = KeyboardController(kb)
    return kb, ctrl
