import argparse

def escape_quotes(input_file, output_file):
    # Use 'utf-8' encoding to handle special characters
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as f:
        for line in content:
            # Escape double quotes and single quotes
            escaped_line = line.replace('"', '\\"').replace("'", "\\'")
            f.write(escaped_line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='[Bulk escape double & single quotes in file containing payloads.]')
    parser.add_argument('input', type=str, help='- input your file which contains the payloads you want to inject into the JSON body.')
    parser.add_argument('--output', type=str, required=True, help='- output file contains your payloads with escaped quotes.')

    args = parser.parse_args()

    # Call the function with input and output file paths
    escape_quotes(args.input, args.output)