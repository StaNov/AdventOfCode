class SameLettersCounter:
    def __init__(self, word):
        self.word = word

    def has_n_same_letters(self, n):
        if len(self.word) == 0:
            return False

        letters_and_counts = {}

        for letter in self.word:
            current_count = letters_and_counts.get(letter, 0)
            letters_and_counts[letter] = current_count + 1

        return n in letters_and_counts.values()
