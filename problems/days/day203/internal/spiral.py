class Spiral:
    def __init__(self, length):
        self.length = length

    def distance_from_start(self):
        if self.length == 1:
            return 0

        return 1 + self.length % 2

    def last_number_in_loop(self):
        i = 1
        while i**2 < self.length:
            i += 2

        return i**2
