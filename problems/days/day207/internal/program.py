class Program:
    def __init__(self, name, number, subprograms):
        self.name = name
        self.number = number
        self.subprograms = subprograms

    def __str__(self):
        return "{} ({}) -> {}".format(self.name, self.number, [program.name for program in self.subprograms])
