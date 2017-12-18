class ProgramTree:
    def __init__(self, input_):
        self._root = None

        for name, number, subprograms in input_:
            if not self._root or self._root in subprograms:
                self._root = name

    def get_root_program(self):
        return self._root


# class Program:
#     def __init__(self, name, number, subprograms):
#         self.name = name
#         self.number = number
#         self.subprograms = subprograms
