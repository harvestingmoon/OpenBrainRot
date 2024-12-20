import inflect
import string
import re

def process_text_section2(input_file_path, output_file_path):
    p = inflect.engine()
    
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # # Remove punctuation
    # text = text.translate(str.maketrans('', '', string.punctuation))

    # Split text into words
    words = text.split()

    def convert_number(word):
        # Store original for returning if not a match
        original_word = word

        # Convert word to lowercase for matching ordinals
        lw = word.lower()

        if lw.isdigit() or re.match(r'^\d+(st|nd|rd|th)$', lw):
            # Convert ordinal numbers (e.g. "7th", "11th")
            return convert_ordinal_to_words(lw)
        return original_word

    def convert_ordinal_to_words(ordinal):
        """Converts an ordinal number (e.g., 7th) to its cardinal form (e.g., 7).

        Args:
            ordinal: The ordinal number as a string.

        Returns:
            The cardinal form of the number as a string.
        """
        try:
            # Remove the ordinal suffix (st, nd, rd, th)
            cardinal = re.sub(r'(st|nd|rd|th)$', '', ordinal.lower())
            word = p.number_to_words(cardinal)
            text = p.ordinal(word).upper()
            text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
            text = text.replace('-', ' ')
            return text
        except ValueError:
            return "Invalid input"

    # Convert numbers and ordinals to words
    words = [convert_number(word) for word in words]

    # Convert to uppercase and split the resulting phrase into sub-words
    processed_words = []
    for word in words:
        for sub_word in word.split():
            processed_words.append(sub_word.upper())

    # Write each word on a new line
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word in processed_words:
            file.write(word + '\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python test.py <input_file> <output_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    process_text_section2(input_file_path, output_file_path)
    print(f"Processed text saved to {output_file_path}")