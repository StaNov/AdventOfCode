import pytest

from .registers import Registers


@pytest.fixture
def registers():
    return Registers()


def test_any_register_has_default_value_after_creation(registers: Registers):
    assert 0 == registers.get("untouched register")


def test_get_touched_register(registers: Registers):
    registers.add("register", 12)
    assert 12 == registers.get("register")


def test_untouched_register_has_zero_value(registers: Registers):
    registers.add("touched register", 10)
    assert 0 == registers.get("untouched register")


def test_get_all_registers(registers: Registers):
    registers.add("first", 1)
    registers.add("second", 2)
    assert {("first", 1), ("second", 2)} == registers.registers
