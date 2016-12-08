class AbbaChecker:

    @staticmethod
    def get_abbas_from_strings(items):
        result = []

        for item in items:
            result += AbbaChecker.get_abbas_from_string(item)

        return result

    @staticmethod
    def get_abbas_from_string(string):
        result = []

        for i in range(0, len(string) - 3):
            checked_string = string[i:i+4]
            if AbbaChecker.is_abba(checked_string):
                result.append(checked_string)

        return result

    @staticmethod
    def is_abba(s):
        return len(s) in range(3, 5) and s[0] == s[-1] and s[1] == s[-2] and s[0] != s[1]
