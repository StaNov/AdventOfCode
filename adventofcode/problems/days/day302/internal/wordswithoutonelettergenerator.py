class WordsWithoutOneLetterGenerator:

    def __init__(self, input_word):
        self.word = input_word

    def generate(self):
        result = set()

        for position in range(0, len(self.word)):
            word_without_letter = self.word_without_letter(position)
            result.add(word_without_letter)

        return result

    def word_without_letter(self, position):
        return (
            self.word[:position]
            +
            self.word[position + 1:]
        )
