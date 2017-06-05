from utils import AbstractMain

if __name__ == "__main__":
    from problems.day01.solver import Solver
else:
    from .solver import Solver


class Main(AbstractMain):

    def __init__(self):
        super(Main, self).__init__(Solver(), __file__)


if __name__ == "__main__":
    main = Main()

    result_1 = Main().main_1()
    print("FIRST RESULT IS: " + str(result_1) + " !!!")

    result_2 = Main().main_2()
    print("SECOND RESULT IS: " + str(result_2) + " !!!")
