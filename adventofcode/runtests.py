import sys
from argparse import ArgumentParser

import pytest


def run_tests(timeout_seconds=1, mark="", parallel=True):
    arguments = [
        "--timeout", str(timeout_seconds),
        "-m", mark
    ]

    if parallel:
        arguments.append("-n")
        arguments.append("auto")

    return pytest.main(arguments)


def _script_called_without_arguments():
    return len(sys.argv) == 1


def run_tests_all(parallel):
    return run_tests(30, parallel=parallel)


def run_tests_only_expensive(parallel):
    return run_tests(30, "time_expensive", parallel)


def run_tests_only_cheap(parallel):
    return run_tests(mark="not time_expensive", parallel=parallel)


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
    parser.add_argument('--sequential',
                        action="store_true",
                        help="Forces sequential execution.")

    args = parser.parse_args()

    if args.all:
        print("Running all tests...")
        exit_code = run_tests_all(not args.sequential)
        sys.exit(exit_code)

    if args.onlyexpensive:
        print("Running only expensive tests...")
        exit_code = run_tests_only_expensive(not args.sequential)
        sys.exit(exit_code)

    if args.onlycheap or _script_called_without_arguments():
        print("Running only cheap tests...")
        exit_code = run_tests_only_cheap(not args.sequential)
        sys.exit(exit_code)
