# -*- coding: utf-8 -*-
import solver
import os


def main():
    f = open(os.path.join(os.path.dirname(__file__), "input"))

    content = f.read()

    result = solver.solve(content)

    return result


if __name__ == "__main__":
    result = main()

    print("AND THE RESULT IS: " + str(result) + "!!!")