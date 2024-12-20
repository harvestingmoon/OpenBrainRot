import re

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

# Input and output file names
input_filename = 'texts/output.txt'
output_filename = 'texts/processed_output.txt'

# Process the text
process_text(input_filename, output_filename)