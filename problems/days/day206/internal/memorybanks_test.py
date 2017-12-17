from . import MemoryBanks


def test_helper_method():
    banks = MemoryBanks([])
    banks.process_until_cycle_is_found()
    assert 0 == banks.get_steps()
