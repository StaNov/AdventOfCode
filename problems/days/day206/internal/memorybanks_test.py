import pytest

from . import MemoryBanks


def test_empty_banks_raises_exception():
    with pytest.raises(Exception):
        MemoryBanks([])


def test_one_step():
    banks = MemoryBanks([1])
    banks.process_until_cycle_is_found()
    assert 1 == banks.get_steps()


def test_two_steps():
    banks = MemoryBanks([0, 1])
    banks.process_until_cycle_is_found()
    assert 2 == banks.get_steps()


def test_three_steps():
    banks = MemoryBanks([1, 0, 0])
    banks.process_until_cycle_is_found()
    assert 3 == banks.get_steps()


def test_two_banks_swap():
    banks = MemoryBanks([1, 0])
    banks.do_step()
    assert [0, 1] == banks._banks


def test_three_banks_distribution():
    banks = MemoryBanks([2, 0, 0, 0])
    banks.do_step()
    assert [0, 1, 1, 0] == banks._banks


def test_distribute_highest_not_first_one():
    banks = MemoryBanks([0, 1, 2, 0, 0, 0])
    banks.do_step()
    assert [0, 1, 0, 1, 1, 0] == banks._banks


def test_distribute_over_start():
    banks = MemoryBanks([0, 1, 5, 0])
    banks.do_step()
    assert [1, 2, 1, 2] == banks._banks


def test_loop_length():
    banks = MemoryBanks([2, 0, 0])
    banks.process_until_cycle_is_found()
    # 2, 0, 0
    # 0, 1, 1  <----
    # 0, 0, 2
    # 1, 1, 0
    # 0, 2, 0
    # 1, 0, 1
    # 0, 1, 1  <----
    assert 5 == banks.get_loop_length()
