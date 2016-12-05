class InputParser:
    @staticmethod
    def parse_line(line):
        values = line.split(" ")
        return int(values[0]), int(values[1]), int(values[2])

    @staticmethod
    def parse_vertically(input_string):
        buffer = []
        result = []

        for line in input_string.split("\n"):
            parsed_line = InputParser.parse_line(line)
            buffer.append(parsed_line)

            if len(buffer) < 3:
                continue

            result.append((buffer[0][0], buffer[1][0], buffer[2][0]))
            result.append((buffer[0][1], buffer[1][1], buffer[2][1]))
            result.append((buffer[0][2], buffer[1][2], buffer[2][2]))

            buffer.clear()

        return result
