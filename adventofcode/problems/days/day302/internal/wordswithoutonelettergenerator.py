class WordsWithoutOneLetterGenerator:

    def generate(self, input_):
        result = set()

        for position in range(0, len(input_)):
            word_without_letter = input_[:position] + input_[position + 1:]
            result.add(word_without_letter)

        return result
