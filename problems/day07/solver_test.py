from .solver import Solver


def test_1_1():
    input_ = (
        "abba[mnop]qrst\n"
        "abcd[bddb]xyyx\n"
        "aaaa[qwer]tyui\n"
        "ioxxoj[asdfgh]zxcvbn\n"
        "hhttjuhgvcgkisaqof[obpleewrfrrsgpumz]umcmeaytqjlqkyrawp[rhkhciyzmxciiysv]kszzqcmcylslhlpqjag"
    )

    assert Solver.solve_1(input_) == 2


def test_2_1():
    input_ = (
        "aba[bab]xyz\n"
        "xyx[xyx]xyx\n"
        "aaa[kek]eke\n"
        "zazbz[bzb]cdb"
    )

    assert Solver.solve_2(input_) == 3
