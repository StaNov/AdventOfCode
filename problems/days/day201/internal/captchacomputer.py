class CaptchaComputer:
    def compute_captcha(self, input_string, second_digit_index_offset=1):  # TODO offset to subclass
        if len(input_string) < 3:
            raise Exception("Input must be longer than 3 characters.")

        result = 0

        for i in range(len(input_string)):
            digit_1 = input_string[i]
            digit_2 = input_string[(i + second_digit_index_offset) % len(input_string)]

            if digit_1 == digit_2:
                result += int(digit_1)

        return result
