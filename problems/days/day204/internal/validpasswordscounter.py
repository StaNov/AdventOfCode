class ValidPasswordsCounter:
    def count(self, input_string, checker):
        valid_passwords_count = 0

        for line in input_string.splitlines():
            if checker.check(line):
                valid_passwords_count += 1

        return valid_passwords_count
