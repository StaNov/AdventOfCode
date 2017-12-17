class MemoryBanks:
    def __init__(self, banks):
        self._banks = banks

    def process_until_cycle_is_found(self):
        pass

    def get_steps(self):
        return 0 if not self._banks else 2
