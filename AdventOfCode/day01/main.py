# -*- coding: utf-8 -*-
import solver
import os


def main_1():
    content = _read_input()
    return solver.solve_1(content)


def main_2():
    content = _read_input()
    return solver.solve_2(content)


def _read_input():
    f = open(os.path.join(os.path.dirname(__file__), "input"))
    input_text = f.read()
    f.close()
    return input_text


if __name__ == "__main__":
    result_1 = main_1()
    print("FIRST RESULT IS: " + str(result_1) + "!!!")

    result_2 = main_2()
    print("SECOND RESULT IS: " + str(result_2) + "!!!")
