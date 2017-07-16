from . import LineParser, AbbaChecker


class SslChecker:
    @staticmethod
    def is_ssl(line):
        including, excluding = LineParser.parse(line)

        including_abbas = AbbaChecker.get_abbas_from_strings(including, True)

        if len(including_abbas) == 0:
            return False

        excluding_abbas = AbbaChecker.get_abbas_from_strings(excluding, True)
        excluding_transposed = SslChecker.transpose(excluding_abbas)

        for included in including_abbas:
            if included in excluding_transposed:
                return True

        return False

    @staticmethod
    def transpose(abbas):
        result = []

        for abba in abbas:
            result.append(abba[1] + abba[0] + abba[1])

        return result