from . import Evaluator


def test_evaluate_valid():
    # TODO assert Evaluator.evaluate(("aaaaa-bbb-z-y-x", 123, "abxyz")) == 123
    pass


def test_evaluate_invalid():
    assert Evaluator.evaluate(("totally-real-room", 200, "decoy")) == 0
