from . import PasswordCheckerAnagramic


def test_empty_password_passes():
    assert PasswordCheckerAnagramic().check("")
