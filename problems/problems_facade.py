import importlib


def get_available_days():
    result = []
    result.append(1)
    result.append(2)
    result.append(3)
    return result


def get_day_calculator(day_number):
    if day_number not in get_available_days():
        raise DayNotExistsException("Day with number '" + str(day_number) + "' doesn't exist.")

    imported_module = importlib.import_module("problems.days.day" + str(day_number).zfill(2) + ".main")
    calculator_class = getattr(imported_module, "DayCalculator")
    return calculator_class()


class DayNotExistsException(Exception):
    pass
