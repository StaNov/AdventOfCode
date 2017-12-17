import pytest
import sys


def run_tests(params):
    exit_code = pytest.main(params)
    sys.exit(exit_code)


if __name__ == "__main__":
    run_tests(sys.argv[1:])
