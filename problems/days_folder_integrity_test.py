import os
import re


def test_directory_names_in_days():
    days_folder_path = os.path.join(os.path.dirname(__file__), "days")

    for folder_name in os.listdir(days_folder_path):
        _check_folder_name(folder_name)


def _check_folder_name(folder_name):
    match = re.fullmatch("day\d\d|template|__pycache__", folder_name)

    if not match:
        raise Exception("Folder '" + folder_name + "' does not belong to the days folder!")
