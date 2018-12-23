import sys
from argparse import ArgumentParser

import pytest


def run_tests(params):
    return pytest.main(params)


def _script_called_without_arguments():
    return len(sys.argv) == 1


def run_tests_all():
    return run_tests([
        "--timeout", "20"  # in seconds
    ])


def run_tests_only_expensive():
    return run_tests([
        "-m", "time_expensive",
        "--timeout", "20"  # in seconds
    ])


def run_tests_only_cheap():
    return run_tests([
        "-m", "not time_expensive",
        "--timeout", "1"  # in seconds
    ])


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--all',
                        action="store_true",
                        help='Runs all tests.')
    parser.add_argument('--onlycheap',
                        action="store_true",
                        help="Runs tests without those marked as time expensive. "
                             "This is the default option when runtests is called without arguments.")
    parser.add_argument('--onlyexpensive',
                        action="store_true",
                        help="Runs only tests marked as time expensive.")

    args = parser.parse_args()

    if len(sys.argv) > 2:
        print("Maximum arguments passed is one!")
        parser.print_help()
        sys.exit(1)

    if args.all:
        print("Running all tests...")
        exit_code = run_tests_all()
        sys.exit(exit_code)

    if args.onlyexpensive:
        print("Running only expensive tests...")
        exit_code = run_tests_only_expensive()
        sys.exit(exit_code)

    if args.onlycheap or _script_called_without_arguments():
        print("Running only cheap tests...")
        exit_code = run_tests_only_cheap()
        sys.exit(exit_code)
