from . import Decrypter


def test_decrypt():
    assert Decrypter.decrypt("ab-cd", 1) == "bc de"
