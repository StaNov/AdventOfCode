import pytest
import sys


def run_tests(params):
    exit_code = pytest.main(params)
    sys.exit(exit_code)


if __name__ == "__main__":
    params = ["-m", "not time_expensive"] if len(sys.argv) == 1 else sys.argv[1:]
    run_tests(params)
