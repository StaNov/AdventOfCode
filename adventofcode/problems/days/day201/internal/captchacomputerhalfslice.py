from .captchacomputer import CaptchaComputer


class CaptchaComputerHalfSlice(CaptchaComputer):
    def _get_second_digit_index_offset(self, input_string_length):
        return input_string_length // 2
