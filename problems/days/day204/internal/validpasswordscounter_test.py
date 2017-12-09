from . import ValidPasswordsCounter


def test_zero_valid_passwords_in_empty_string():
    ValidPasswordsCounter().count("")