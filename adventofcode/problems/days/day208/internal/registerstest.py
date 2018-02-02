import pytest

from .registers import Registers


@pytest.fixture
def registers():
    return Registers()


def test_get_untouched_register(registers: Registers):
    assert 0 == registers.get("untouched register")


def test_get_setted_register(registers: Registers):
    registers.add("register", 12)
    assert 12 == registers.get("register")
