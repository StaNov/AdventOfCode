from utils import AbstractMainCalculator

if __name__ == "__main__":
    from problems.template.solver import Solver
else:
    from .solver import Solver


class MainCalculator(AbstractMainCalculator):
    def __init__(self):
        super(MainCalculator, self).__init__(__file__)

    def create_new_solver(self):
        return Solver()


if __name__ == "__main__":
    MainCalculator().calculate_both_parts_and_print_results()
