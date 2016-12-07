from .internal import LineParser, Evaluator, Decrypter


class Solver:
    @staticmethod
    def solve_1(input_string):
        result = 0

        for line in input_string.splitlines():
            parsed_line = LineParser.parse(line)
            line_value = Evaluator.evaluate(parsed_line)
            result += line_value

        return result

    @staticmethod
    def solve_2(input_string, finding_room_name="northpole object storage"):
        for line in input_string.splitlines():
            parsed_line = LineParser.parse(line)

            encrypted_string = parsed_line[0]
            encryption_key = parsed_line[1]

            decrypted = Decrypter.decrypt(encrypted_string, encryption_key)

            if decrypted == finding_room_name and Evaluator.evaluate(parsed_line) != 0:
                return encryption_key
