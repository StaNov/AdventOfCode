class Evaluator:

    @staticmethod
    def evaluate(input_):
        letters = input_[0].replace("-", "")
        value = input_[1]
        hash_ = input_[2]

        computed_hash = Evaluator.compute_hash(letters)

        return value if computed_hash == hash_ else 0

    @staticmethod
    def compute_hash(letters):
        counts = Evaluator.compute_counts(letters)
        sorted_counts = Evaluator.sort_counts(counts)
        return Evaluator.counts_to_hash(sorted_counts)

    @staticmethod
    def compute_counts(letters):
        counts = {}

        for char in letters:
            if char not in counts:
                counts[char] = 0

            counts[char] += 1

        return counts.items()

    @staticmethod
    def sort_counts(counts):
        return sorted(counts, key=lambda item: -item[1] * 1000 + ord(item[0]))

    @staticmethod
    def counts_to_hash(counts):
        result = ""

        for item in counts:
            result += item[0]

            if len(result) == 5:
                break

        return result
