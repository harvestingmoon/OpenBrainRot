from pocketsphinx import Pocketsphinx
import os

def force_alignment(dict_path, audio_path, text_path):
    model_path = r'D:\Programming\Python\AI\Project 2024\cmusphinx-en-us-5.2'  # Update this path to the location of your acoustic model

    # Check if the model path contains the necessary files
    if not os.path.exists(os.path.join(model_path, 'mdef')):
        raise FileNotFoundError(f"Acoustic model definition 'mdef' not found in {model_path}")

    # Read the text from the file
    with open(text_path, 'r') as file:
        text = file.read().strip()

    # Create a Pocketsphinx configuration
    config = {
        'hmm': model_path,  # Path to the acoustic model
        'lm': False,  # No language model
        'dict': dict_path, # Path to the dictionary
        'beam': 1e-50,  # Adjust beam threshold
        'wbeam': 1e-40,  # Adjust word beam threshold
        'pbeam': 1e-30  # Adjust phone beam threshold
    }

    # Initialize Pocketsphinx decoder
    ps = Pocketsphinx(**config)

    # Set the text to align
    ps.set_align_text(text)

    # Decode the audio file
    ps.decode(audio_file=audio_path)

    # Get the alignment result
    segments = ps.seg()
    print(segments)

    # Check if segments is None and bypass if necessary
    if segments is None:
        print("Warning: Failed to decode the audio file. Please check the input files and configuration.")
    else:
        # Print the alignment result
        for segment in segments:
            print(f"{segment.word} [{segment.start_frame} - {segment.end_frame}]")

# Example usage
dict_path = 'texts/test.txt'
audio_path = 'output.wav'
text_path = 'texts/oof.text'

force_alignment(dict_path, audio_path, text_path)

# Continue with other tasks if needed
print("Forced alignment process completed.")