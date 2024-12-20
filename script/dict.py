import re
import inflect
import string

# Script to pre-process the dictionary path
# SECTION 1
# converting the scraped text into individual lettering + split lines
def remove_punctuation(text):
    # Define the punctuation to remove
    punctuation_to_remove = r'[.,:!]'

    # Remove punctuation
    text_without_punctuation = re.sub(punctuation_to_remove, '', text)

    return text_without_punctuation

def split_text_into_words(text):
    # Split the text into words
    words = text.split()

    return words

def process_text(input_filename, output_filename):
    try:
        # Read the input text from the file
        with open(input_filename, 'r') as input_file:
            text = input_file.read()

        # Remove punctuation
        text_without_punctuation = remove_punctuation(text)

        # Split the text into words
        words = split_text_into_words(text_without_punctuation)

        # Write each word to the output file
        with open(output_filename, 'w') as output_file:
            for word in words:
                output_file.write(word.upper() + '\n')

        print(f"Output written to {output_filename} successfully.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# SECTION 2
# Literally just more preprocessing (punctuation remova, cleaning up the ordinals)
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



# SECTION 3
# mapping cmu dicitionary to the dictionary path
def read_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().splitlines()
    return words

def create_dict_map(words, cmudict_path):
    cmudict = {}
    with open(cmudict_path, 'r', encoding='latin-1') as file:
        for line in file:
            if line.startswith(";;;"):
                continue
            parts = line.strip().split("  ")
            word = parts[0]
            print(parts)
            phonemes = parts[1]
            cmudict[word] = phonemes

    dict_map = {}
    for word in words:
        if word in cmudict:
            dict_map[word] = cmudict[word]
        else:
            dict_map[word] = "B"
            print(f"Warning: Word '{word}' not found in CMUdict, replacing with B")

    return dict_map

def save_dict_map(dict_map, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word, phonemes in dict_map.items():
            file.write(f"{word} {phonemes}\n")

# Input and output file name
if __name__ == "__main__":
    import sys
    input_filename = 'texts/small_script.txt'
    output_filenameS1 = 'texts/processed_output.txt'
    final_output_filename = 'texts/oof.text'

    process_text(input_filename, output_filenameS1)
    process_text_section2(output_filenameS1, final_output_filename)
    processed_output_file_path = final_output_filename
    cmudict_path = 'cmudict0.7aa'
    output_dict_path = 'texts/test.txt'

    words = read_words(processed_output_file_path)
    dict_map = create_dict_map(words, cmudict_path)
    save_dict_map(dict_map, output_dict_path)
    print(f"Dictionary map saved to {output_dict_path}")