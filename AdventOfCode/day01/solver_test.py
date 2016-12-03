# -*- coding: utf-8 -*-
import solver


def test_1():
    assert solver.solve_1("R2, L3") == 5


def test_2():
    assert solver.solve_1("R2, R2, R2") == 2


def test_3():
    assert solver.solve_1("R5, L5, R5, R3") == 12
