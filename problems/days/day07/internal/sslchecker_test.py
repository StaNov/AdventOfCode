from . import SslChecker


def test_check_true():
    assert SslChecker.is_ssl("aba[bab]xyz")


def test_check_false_1():
    assert not SslChecker.is_ssl("xyx[xyx]xyx")


def test_check_false_2():
    assert not SslChecker.is_ssl("abc[xyx]abc")


def test_transpose():
    assert SslChecker.transpose(["aba", "cdc", "ere"]) == ["bab", "dcd", "rer"]
