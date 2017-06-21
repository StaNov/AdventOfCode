class LettersProcessor:
    def __init__(self):
        self.output = ""

    def process_letter(self, letter):
        if letter == "":
            raise Exception("Argument must be one letter!")

        self.output = self.output + letter

    def get_processed_output(self):
        return self.output
