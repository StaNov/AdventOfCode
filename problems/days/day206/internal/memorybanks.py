class MemoryBanks:
    def __init__(self, banks):
        self._banks = banks

    def process_until_cycle_is_found(self):
        pass

    def do_step(self):
        to_distribute = self._banks[0]
        current_index = 1
        self._banks[0] = 0

        while to_distribute > 0:
            self._banks[current_index] += 1
            current_index += 1
            to_distribute -= 1

    def get_steps(self):
        return 0 if not self._banks else 2
