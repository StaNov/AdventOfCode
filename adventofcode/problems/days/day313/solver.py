from adventofcode.problems.framework import AbstractSolver


class Solver(AbstractSolver):

    def _solve_1_internal(self, ore_mine):
        collision_position = ore_mine.simulate_until_first_collision()
        position_x, position_y = collision_position
        return "{},{}".format(position_x, position_y)

    def _solve_2_internal(self, input_):
        # TODO
        return 0
