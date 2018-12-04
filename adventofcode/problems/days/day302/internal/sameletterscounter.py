class SameLettersCounter:
    def __init__(self, word):
        self.word = word

    def has_two_same_letters(self):
        if len(self.word) == 0:
            return False

        first_letter = self.word[0]
        counter = 0

        for letter in self.word:
            if letter == first_letter:
                counter += 1

        return counter == 2
