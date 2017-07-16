from problems.utils import InputReader
if __name__ == "__main__":
    from problems.days.day04.solver import Solver
else:
    from .solver import Solver


class Main:
    @staticmethod
    def main_1():
        content = InputReader.read_input(__file__)
        return Solver.solve_1(content)

    @staticmethod
    def main_2():
        content = InputReader.read_input(__file__)
        return Solver.solve_2(content)


if __name__ == "__main__":
    result_1 = Main.main_1()
    print("FIRST RESULT IS: " + str(result_1) + " !!!")

    result_2 = Main.main_2()
    print("SECOND RESULT IS: " + str(result_2) + " !!!")
