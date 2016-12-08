from . import AbbaChecker


def test_get_abbas_from_strings():
    assert AbbaChecker.get_abbas_from_strings(["xyzx", "xyzabbaxyz", "xyzx", "xyzxybaabxyz"]) == ["abba", "baab"]


def test_get_abbas_from_string_1():
    assert AbbaChecker.get_abbas_from_string("xyzxyzabbaxyzbaabxyz") == ["abba", "baab"]


def test_get_abbas_from_string_2():
    assert AbbaChecker.get_abbas_from_string("abcdefghijklm") == []


def test_get_abbas_from_string_3():
    assert AbbaChecker.get_abbas_from_string("xyzxyzaaaaxyzxyz") == []


def test_is_abba_true():
    assert AbbaChecker.is_abba("abba")


def test_is_abba_false_1():
    assert not AbbaChecker.is_abba("xyzw")


def test_is_abba_false_2():
    assert not AbbaChecker.is_abba("aaaa")
