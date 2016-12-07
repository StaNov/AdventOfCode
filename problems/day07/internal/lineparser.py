import re


class LineParser:

    pattern = "\[(.+?)\]"
    separator = "|"

    @staticmethod
    def parse(line):
        excluded = re.findall(LineParser.pattern, line)

        included_string = re.sub(LineParser.pattern, LineParser.separator, line)
        included = included_string.split(LineParser.separator)

        return included, excluded
