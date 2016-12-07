from .solver import Solver


def test_1_1():
    assert Solver.solve_1(
        "abba[mnop]qrst\n"
        "abcd[bddb]xyyx\n"
        "aaaa[qwer]tyui\n"
        "ioxxoj[asdfgh]zxcvbn\n"
        "hhttjuhgvcgkisaqof[obpleewrfrrsgpumz]umcmeaytqjlqkyrawp[rhkhciyzmxciiysv]kszzqcmcylslhlpqjag"
    ) == 2


def test_2_1():
    # TODO assert Solver.solve_2("test test") == 0
    pass
