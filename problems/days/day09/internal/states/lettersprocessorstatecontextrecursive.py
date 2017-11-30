from . import LettersProcessorStateContext


class LettersProcessorStateContextRecursive(LettersProcessorStateContext):

    def process_read_text_chunk(self, repeat_count, read_text_chunk):
        recursive_context = LettersProcessorStateContextRecursive()

        for char in read_text_chunk:
            recursive_context.process_letter(char)

        self.add_to_output_length(recursive_context.get_processed_output_length() * repeat_count)
