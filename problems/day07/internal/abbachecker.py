class AbbaChecker:

    long_length = 4
    short_length = 3

    @staticmethod
    def get_abbas_from_strings(items, short=False):
        result = []

        for item in items:
            result += AbbaChecker.get_abbas_from_string(item, short)

        return result

    @staticmethod
    def get_abbas_from_string(string, short=False):
        result = []
        abba_length = 3 if short else 4

        for i in range(0, len(string) - (abba_length-1)):
            checked_string = string[i:i+abba_length]
            if AbbaChecker.is_abba(checked_string):
                result.append(checked_string)

        return result

    @staticmethod
    def is_abba(s):
        return len(s) in range(3, 5) and s[0] == s[-1] and s[1] == s[-2] and s[0] != s[1]
