class CaptchaComputer:
    def compute_captcha(self, input_string):
        if len(input_string) < 3:
            raise Exception("Input string must be at least 3 characters long.")

        result = 0

        for i in range(len(input_string)):
            digit_1 = input_string[i]
            digit_2 = input_string[(i + self._get_second_digit_index_offset(len(input_string))) % len(input_string)]

            if digit_1 == digit_2:
                result += int(digit_1)

        return result

    def _get_second_digit_index_offset(self, input_string_length):
        return 1
