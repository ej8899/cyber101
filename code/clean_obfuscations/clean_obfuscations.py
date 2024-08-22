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
    
    # Remove single-line comments that start with // followed by at least one space (tab, etc)
    cleaned_content = re.sub(r'//\s+.*$', '', cleaned_content, flags=re.MULTILINE)
    
    return cleaned_content

def remove_blank_lines(content):
    return re.sub(r'\n\s*\n', '\n', content)

def trim_whitespace(content):
    # Trim leading/trailing whitespace from each line and condense multiple spaces.
    # Trim leading and trailing whitespace from each line
    content = "\n".join([line.strip() for line in content.splitlines()])
    # Condense multiple spaces into a single space
    content = re.sub(r'\s{2,}', ' ', content)
    return content

def remove_empty_functions(content):
    # Remove empty functions.
    # Remove functions with empty bodies or bodies containing only whitespace or comments
    content = re.sub(r'function\s+\w+\s*\([^)]*\)\s*\{\s*\}', '', content)
    return content

def main(filename):
    content = read_file(filename)
    content = remove_js_comments(content)
    content = remove_blank_lines(content)
    content = trim_whitespace(content)
    content = remove_empty_functions(content)
    
    # Extract the base filename without the extension
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    # Define the output file name as cleaned_FILENAME.js
    output_filename = f"CLEANED_{base_filename}.js"
    
    write_file(output_filename, content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python clean_obfuscations.py <filename.js>")
    else:
        main(sys.argv[1])
