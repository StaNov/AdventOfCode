class ValidPasswordsCounter:
    def __init__(self, checker):
        self.checker = checker

    def count(self, input_string):
        valid_passwords_count = 0

        for line in input_string.splitlines():
            if self.checker.check(line):
                valid_passwords_count += 1

        return valid_passwords_count
