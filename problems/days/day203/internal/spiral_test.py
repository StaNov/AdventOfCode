from .spiral import Spiral


def test_get_last_number_of_empty_spiral():
    assert 1 == Spiral().get_last_number()
