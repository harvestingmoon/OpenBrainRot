import string   

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
            phonemes = parts[1]
            cmudict[word] = phonemes

    dict_map = {}
    for word in words:
        if word in cmudict:
            dict_map[word] = cmudict[word]
        else:
            print(f"Warning: Word '{word}' not found in CMUdict")

    return dict_map

def save_dict_map(dict_map, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word, phonemes in dict_map.items():
            file.write(f"{word} {phonemes}\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python create_dict_map.py <processed_output_file> <cmudict_path> <output_dict_path>")
        sys.exit(1)

    processed_output_file_path = sys.argv[1]
    cmudict_path = sys.argv[2]
    output_dict_path = sys.argv[3]

    words = read_words(processed_output_file_path)
    dict_map = create_dict_map(words, cmudict_path)
    save_dict_map(dict_map, output_dict_path)
    print(f"Dictionary map saved to {output_dict_path}")