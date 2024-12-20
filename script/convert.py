def convert_dict_format(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            # Skip comments and empty lines
            if line.startswith(';') or not line.strip():
                continue
            # Replace tab with two spaces
            converted_line = line.replace('\t', '  ')
            outfile.write(converted_line)

# Example usage
input_path = 'cmudict_actual-0.7a'
output_path = 'cmudict0.7aa'
convert_dict_format(input_path, output_path)