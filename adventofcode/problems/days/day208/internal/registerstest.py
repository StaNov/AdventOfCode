from .registers import Registers


def test_get_untouched_register():
    assert 0 == Registers().get("untouched register")
