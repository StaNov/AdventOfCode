class PasswordChecker:

    def __init__(self) -> None:
        super().__init__()

    def check(self, password):
        original_words = password.split()
        pre_prepared_words = self._pre_prepare_words(original_words)
        return len(original_words) == len(set(pre_prepared_words))

    def _pre_prepare_words(self, words):
        return words
