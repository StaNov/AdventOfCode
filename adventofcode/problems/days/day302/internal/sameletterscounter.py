class SameLettersCounter:
    def __init__(self, word):
        self.word = word

    def has_two_same_letters(self):
        return len(self.word) != 0
