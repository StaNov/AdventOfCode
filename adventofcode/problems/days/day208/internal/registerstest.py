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


def test_get_other_register(registers: Registers):
    registers.add("setted register", 10)
    assert 0 == registers.get("untouched register")


def test_get_all_registers(registers: Registers):
    registers.add("first", 1)
    registers.add("second", 2)
    assert [("first", 1), ("second", 2)] == registers.registers