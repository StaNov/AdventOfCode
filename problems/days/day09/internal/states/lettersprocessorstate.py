class LettersProcessorState:
    def process_letter(self, caller, letter):
        raise Exception("Not implemented!")

    def is_ok_to_get_output_length_in_this_state(self):
        raise Exception("Not implemented!")

    def get_class_name(self):
        return self.__class__.__name__
