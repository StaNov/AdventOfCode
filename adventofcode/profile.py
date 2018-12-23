import sys

from pyinstrument import Profiler

from adventofcode import runtests


def profile():
    profiler = Profiler()
    profiler.start()

    exit_code = runtests.run_tests_all()

    profiler.stop()

    print(profiler.output_text(unicode=False, color=True))
    return exit_code


if __name__ == "__main__":
    exit_code_main = profile()
    sys.exit(exit_code_main)
