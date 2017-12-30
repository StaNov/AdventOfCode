import importlib
import os
import re


def get_available_days():
    result = []

    days_folder_path = os.path.join(os.path.dirname(__file__), "days")

    for folder_name in os.listdir(days_folder_path):
        match = re.fullmatch("day(\d+)", folder_name)
        if match:
            result.append(int(match.group(1)))

    return result


def get_day_calculator(day_number):
    if day_number not in get_available_days():
        raise DayNotExistsException("Day with number '" + str(day_number) + "' doesn't exist.")

    calculator_class = _get_dynamically_imported_class(day_number)

    return calculator_class()


def _get_dynamically_imported_class(day_number):
    imported_module = importlib.import_module("adventofcode.problems.days.day" + str(day_number).zfill(2) + ".main")
    return getattr(imported_module, "DayCalculator")


class DayNotExistsException(Exception):
    pass
