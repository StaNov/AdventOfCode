import pytest
from pyinstrument import Profiler


def profile(arguments):
    profiler = Profiler(use_signal=False)
    profiler.start()

    pytest.main(arguments)

    profiler.stop()

    print(profiler.output_text(unicode=True, color=True))


if __name__ == "__main__":
    # profile all tests
    profile([])
