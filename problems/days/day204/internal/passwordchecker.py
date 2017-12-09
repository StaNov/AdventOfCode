class PasswordChecker:
    def check(self, password):
        words = password.split()
        return len(words) == len(set(words))
