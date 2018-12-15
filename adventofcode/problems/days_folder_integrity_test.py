import os
import re

VALID_FOLDER_NAMES_SUBREGEXES = [
    r"day\d+",
    r"template",
    r"__pycache__",
    r".pytest_cache",
    r".cache",
    r"__init__.py",
]

VALID_FOLDER_NAMES_REGEX = str.join("|", VALID_FOLDER_NAMES_SUBREGEXES)


def test_directory_names_in_days():
    days_folder_path = os.path.join(os.path.dirname(__file__), "days")

    for folder_name in os.listdir(days_folder_path):
        _check_folder_name(folder_name)


def _check_folder_name(folder_name):
    match = re.fullmatch(VALID_FOLDER_NAMES_REGEX, folder_name)

    if not match:
        raise Exception("Folder '" + folder_name + "' does not belong to the days folder!")
