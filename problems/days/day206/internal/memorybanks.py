import copy


class MemoryBanks:
    def __init__(self, banks):
        if not banks:
            raise Exception("Cannot instantiate empty banks!")

        self._banks = banks
        self._initial_banks = banks
        self._banks = copy.copy(banks)
        self._steps_taken = 0

    def process_until_cycle_is_found(self):
        while self._initial_banks != self._banks or self._steps_taken == 0:
            self.do_step()

    def do_step(self):
        highest_index = self.get_highest_index()
        to_distribute = self._banks[highest_index]
        current_index = highest_index
        self._banks[highest_index] = 0

        while to_distribute > 0:
            current_index = (current_index + 1) % len(self._banks)
            self._banks[current_index] += 1
            to_distribute -= 1

        self._steps_taken += 1

    def get_highest_index(self):
        highest_index = -1
        highest_value = -1

        for i, bank in enumerate(self._banks):
            if bank > highest_value:
                highest_index = i
                highest_value = bank

        return highest_index

    def get_steps(self):
        return self._steps_taken
