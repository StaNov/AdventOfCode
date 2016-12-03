# -*- coding: utf-8 -*-
from . import solver


def test():
    assert solver.solve("R2, L3") == 5
    assert solver.solve("R2, R2, R2") == 2
    assert solver.solve("R5, L5, R5, R3") == 12