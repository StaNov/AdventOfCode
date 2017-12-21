class UnbalanceFinder:

    def __init__(self, root_program):
        self._root = root_program

    def find_unbalanced_program(self):
        return self._root.subprograms[2]
