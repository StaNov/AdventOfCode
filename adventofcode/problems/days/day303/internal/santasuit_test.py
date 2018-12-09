import pytest

from . import SantaSuit, SantaSuitPiece


@pytest.fixture
def santa_suit():
    return SantaSuit()


def test_no_patches(santa_suit):
    assert 0 == santa_suit.get_overlapping_count()


def test_one_overlapping_square(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 1, 1))
    santa_suit.saw_patch(SantaSuitPiece(2, 1, 1, 1, 1))

    assert 1 == santa_suit.get_overlapping_count()


def test_one_piece_does_not_create_overlap(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 1, 1))

    assert 0 == santa_suit.get_overlapping_count()


def test_bigger_overlap(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 1, 2))
    santa_suit.saw_patch(SantaSuitPiece(2, 1, 1, 1, 2))

    assert 2 == santa_suit.get_overlapping_count()


def test_different_position_no_overlap(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 1, 1))
    santa_suit.saw_patch(SantaSuitPiece(2, 9, 9, 1, 1))

    assert 0 == santa_suit.get_overlapping_count()


def test_different_position_some_overlap(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(2, 2, 2, 2, 2))

    assert 1 == santa_suit.get_overlapping_count()


def test_more_patches(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(2, 5, 5, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(3, 2, 2, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(4, 6, 6, 2, 2))

    assert 2 == santa_suit.get_overlapping_count()


def test_one_patch_is_intact(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 2, 2))

    assert 1 == santa_suit.get_intact_patch_id()


def test_three_patches_last_intact(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(2, 1, 1, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(3, 9, 9, 2, 2))

    assert 3 == santa_suit.get_intact_patch_id()


def test_three_patches_middle_intact(santa_suit):
    santa_suit.saw_patch(SantaSuitPiece(1, 1, 1, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(2, 9, 9, 2, 2))
    santa_suit.saw_patch(SantaSuitPiece(3, 1, 1, 2, 2))

    assert 2 == santa_suit.get_intact_patch_id()
