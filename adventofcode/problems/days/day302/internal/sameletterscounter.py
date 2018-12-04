class SameLettersCounter:
    def __init__(self, word):
        self.word = word

    def has_two_same_letters(self):
        if len(self.word) == 0:
            return False

        first_letter = self.word[0]

        for letter in self.word[1:]:
            if letter == first_letter:
                return True

        return False
