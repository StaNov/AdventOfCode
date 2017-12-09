from . import PasswordChecker


class PasswordCheckerAnagramic(PasswordChecker):
    def _pre_prepare_words(self, words):
        return [_sort_letters_in_word(word) for word in words]


def _sort_letters_in_word(word):
    return "".join(sorted(word))
