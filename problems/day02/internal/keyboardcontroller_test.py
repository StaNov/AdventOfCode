from . import Keyboard, KeyboardAdvanced, KeyboardController


def test_move_right():
    kb, ctrl = init((2, 1))
    ctrl.move_right()
    assert kb.get_key() == "9"
    ctrl.move_right()
    assert kb.get_key() == "9"


def test_move_left():
    kb, ctrl = init((0, 1))
    ctrl.move_left()
    assert kb.get_key() == "1"
    ctrl.move_left()
    assert kb.get_key() == "1"


def test_move_up():
    kb, ctrl = init((1, 1))
    ctrl.move_up()
    assert kb.get_key() == "2"
    ctrl.move_up()
    assert kb.get_key() == "2"


def test_move_down():
    kb, ctrl = init((1, 2))
    ctrl.move_down()
    assert kb.get_key() == "9"
    ctrl.move_down()
    assert kb.get_key() == "9"


def test_advanced():
    kb, ctrl = init((2, 0), True)
    ctrl.move_up()
    assert kb.get_key() == "5"
    ctrl.move_left()
    assert kb.get_key() == "5"
    ctrl.move_down()
    assert kb.get_key() == "5"
    ctrl.move_right()
    assert kb.get_key() == "6"


def init(index, use_advanced=False):
    kb = KeyboardAdvanced(index) if use_advanced else Keyboard(index)
    ctrl = KeyboardController(kb)
    return kb, ctrl
