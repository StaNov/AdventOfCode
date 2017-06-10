from utils import AbstractMainCalculator

if __name__ == "__main__":
    from problems.day08.solver import Solver
else:
    from .solver import Solver


class MainCalculator(AbstractMainCalculator):
    def __init__(self):
        super(MainCalculator, self).__init__(Solver(), __file__)


if __name__ == "__main__":
    MainCalculator().calculate_both_parts_and_print_results()
