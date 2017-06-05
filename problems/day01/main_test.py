import pytest
from .main import Main


@pytest.fixture
def main():
    return Main()


def test_main_1(main):
    assert main.main_1() == 262


def test_main_2(main):
    assert main.main_2() == 131
