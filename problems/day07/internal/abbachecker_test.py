from . import AbbaChecker


def test_check_true():
    assert AbbaChecker.check("xyzxyzabbaxyzxyz")


def test_check_false():
    assert not AbbaChecker.check("abcdefghijklm")


def test_check_false_2():
    assert not AbbaChecker.check("xyzxyzaaaaxyzxyz")


def test_is_abba_true():
    assert AbbaChecker.is_abba("abba")


def test_is_abba_false_1():
    assert not AbbaChecker.is_abba("xyzw")


def test_is_abba_false_2():
    assert not AbbaChecker.is_abba("aaaa")
