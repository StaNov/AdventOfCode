from adventofcode.problems.utils import AbstractSolver
from .internal import MemoryBanks


class Solver(AbstractSolver):
    def _solve_1_internal(self, input_):
        banks = MemoryBanks(input_)
        banks.process_until_cycle_is_found()
        return banks.get_steps()

    def _solve_2_internal(self, input_):
        banks = MemoryBanks(input_)
        banks.process_until_cycle_is_found()
        return banks.get_loop_length()
