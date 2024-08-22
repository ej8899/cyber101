import sys
import re
import os

def remove_js_comments(filename):
    # Read the input file in binary mode and decode explicitly
    with open(filename, 'rb') as file:
        content = file.read().decode('utf-8', errors='ignore')  # 'utf-8' can be adjusted if necessary

    # Regular expression to remove multiline comments (/* ... */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Regular expression to remove single-line comments (// ... to the end of the line)
    # This regex should match any // and remove everything that follows until the line ends, handling various line endings.
    content = re.sub(r'//[^\r\n]*', '', content)

    # Remove any leftover empty lines after removing comments
    content = re.sub(r'\n\s*\n', '\n', content)
    
    # Ensure that all carriage returns are normalized to newlines
    content = content.replace('\r\n', '\n').replace('\r', '\n')

    # Extract the base filename without the extension
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    
    # Define the output file name as cleaned_FILENAME.js
    output_filename = f"cleaned_{base_filename}.js"

    # Write the cleaned content to the output file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f"Cleaned file written to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_js_comments.py <filename.js>")
    else:
        remove_js_comments(sys.argv[1])
