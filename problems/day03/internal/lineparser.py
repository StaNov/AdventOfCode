class LineParser:
    @staticmethod
    def parse(line):
        values = line.split(" ")
        return int(values[0]), int(values[1]), int(values[2])
