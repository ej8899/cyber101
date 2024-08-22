import sys
import re
import os

def read_file(filename):
    # Read the content of the file.
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    # Write the cleaned content to the output file.
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Cleaned file written to {filename}")

def remove_js_comments(content):
    # Remove multiline comments  (/* ... */)
    cleaned_content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    # Remove single-line comments (// ...) 
    cleaned_content = re.sub(r'//.*$', '', cleaned_content, flags=re.MULTILINE)
    return cleaned_content

def main(filename):
    content = read_file(filename)
    cleaned_content = remove_js_comments(content)
    
    # Extract the base filename without the extension
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    # Define the output file name as cleaned_FILENAME.js
    output_filename = f"cleaned_{base_filename}.js"
    
    write_file(output_filename, cleaned_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_obfuscations.py <filename.js>")
    else:
        main(sys.argv[1])
