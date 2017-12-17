from . import MemoryBanks


def test_empty_banks():
    banks = MemoryBanks([])
    banks.process_until_cycle_is_found()
    assert 0 == banks.get_steps()


def test_two_banks():
    banks = MemoryBanks([0, 1])
    banks.process_until_cycle_is_found()
    assert 2 == banks.get_steps()


def test_two_banks_swap():
    banks = MemoryBanks([0, 1])
    banks.do_step()
    assert [1, 0] == banks._banks
