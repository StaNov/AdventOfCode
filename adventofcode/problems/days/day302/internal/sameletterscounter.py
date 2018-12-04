class SameLettersCounter:
    def __init__(self, word):
        self.word = word

    def has_two_same_letters(self):
        if len(self.word) == 0:
            return False

        return self.word[0] == self.word[1]
