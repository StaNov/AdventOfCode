import os


def read_file_to_string(main_calculator_file_name):
    file_path = os.path.join(os.path.dirname(main_calculator_file_name), "input")

    with open(file_path) as f:
        return f.read()
