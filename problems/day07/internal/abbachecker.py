class AbbaChecker:

    @staticmethod
    def at_least_one_is_abba(items):
        for item in items:
            if AbbaChecker.check(item):
                return True

        return False

    @staticmethod
    def all_are_not_abba(items):
        for item in items:
            if AbbaChecker.check(item):
                return False

        return True

    @staticmethod
    def check(string):
        for i in range(0, len(string) - 3):
            if AbbaChecker.is_abba(string[i:i+4]):
                return True

        return False

    @staticmethod
    def is_abba(s):
        return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]
