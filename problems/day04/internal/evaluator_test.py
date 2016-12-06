from . import Evaluator


def test_evaluate_valid():
    assert Evaluator.evaluate(("aaaaa-bbb-z-y-x", 123, "abxyz")) == 123


def test_evaluate_invalid():
    assert Evaluator.evaluate(("totally-real-room", 200, "decoy")) == 0


def test_compute_hash_1():
    assert Evaluator.compute_hash("aaaaabbbzyx") == "abxyz"


def test_compute_hash_2():
    assert Evaluator.compute_hash("abcdefgh") == "abcde"


def test_compute_hash_3():
    assert Evaluator.compute_hash("notarealroom") == "oarel"
