import re


class LineParser:

    @staticmethod
    def parse(line):
        regex = re.compile("(.+)-(\d+)\[(.+)\]")
        parsed = regex.match(line)
        letters, number, hash_ = parsed.groups()
        return letters, int(number), hash_
