class MemoryBanks:
    def __init__(self, banks):
        self._banks = banks

    def process_until_cycle_is_found(self):
        pass

    def do_step(self):
        highest_index = self.get_highest_index()
        to_distribute = self._banks[highest_index]
        current_index = highest_index + 1
        self._banks[highest_index] = 0

        while to_distribute > 0:
            self._banks[current_index] += 1
            current_index = (current_index + 1) % len(self._banks)
            to_distribute -= 1

    def get_highest_index(self):
        highest_index = -1
        highest_value = -1

        for i, bank in enumerate(self._banks):
            if bank > highest_value:
                highest_index = i
                highest_value = bank

        return highest_index

    def get_steps(self):
        return 0 if not self._banks else 2
