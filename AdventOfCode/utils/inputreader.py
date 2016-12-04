import os


class InputReader:
    @staticmethod
    def read_input(this_file_name):
        f = open(os.path.join(os.path.dirname(this_file_name), "input"))
        input_text = f.read()
        f.close()
        return input_text
