from audio import audio

def testing_ground(text_path):
    # Read the text from the file
    with open(text_path, 'r') as file:
        text = file.read().strip()
    
    # Process the text (e.g., convert to speech, print, etc.)
    print("Text content from the file:")
    audio(text)

# Example usage
if __name__ == "__main__":
    testing_ground("texts/small_script.txt")