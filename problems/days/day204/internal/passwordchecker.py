class PasswordChecker:
    def __init__(self):
        self.result = 0

    def check(self, password):
        return len(password.split()) < 2
