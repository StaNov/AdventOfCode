class Program:
    def __init__(self, name, weight, subprograms):
        self.name = name
        self.weight = weight
        self.subprograms = subprograms

    def __str__(self):
        return "{} ({}) -> {}".format(self.name, self.weight, [program.name for program in self.subprograms])
