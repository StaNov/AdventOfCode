from . import ValidPasswordsCounter


class TestChecker:
    VALID_LINE = "validPassword"

    def check(self, password):
        return password == self.VALID_LINE


def test_zero_valid_passwords_in_empty_string():
    assert 0 == ValidPasswordsCounter().count("", TestChecker())


def test_one_valid_password():
    assert 1 == ValidPasswordsCounter().count("validPassword", TestChecker())


def test_one_invalid_password():
    assert 0 == ValidPasswordsCounter().count("invalid", TestChecker())


def test_two_valid_passwords():
    assert 2 == ValidPasswordsCounter().count("validPassword\nvalidPassword", TestChecker())


def test_valid_and_invalid_passwords():
    assert 1 == ValidPasswordsCounter().count("validPassword\ninvalid", TestChecker())
