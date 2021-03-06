import pytest

from . import PositionRecorder


def test_record_position():
    recorder = PositionRecorder()
    visited_position = recorder.record((5, 0))

    assert visited_position is None

    visited_position = recorder.record((5, 5))

    assert visited_position is None

    visited_position = recorder.record((3, 5))

    assert visited_position is None

    visited_position = recorder.record((3, -10))

    assert visited_position == (3, 0)

    with pytest.raises(Exception):
        recorder.record((10, -10))


def test_record_bad_position():
    recorder = PositionRecorder()
    with pytest.raises(ValueError):
        recorder.record((2, 3))
