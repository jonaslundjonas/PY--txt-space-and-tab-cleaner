"""
Script to Clean Up Text Files
-----------------------------
Author: Jonas Lund, 2023

Description:
This Python script replaces tabs and spaces in `.txt` files with commas.
The script must be placed in the same directory as the `.txt` files you want to clean up.

Requirements:
- Python 3.x installed
- The script must be in the same folder as the `.txt` files to be processed

Usage:
Simply run the script, and it will process all `.txt` files in the current directory.

"""

import os

def replace_tabs_and_spaces_with_commas_in_file(file_path):
    try:
        # Attempt to read the content of the file using iso-8859-1 encoding
        with open(file_path, 'r', encoding='iso-8859-1') as f:
            content = f.read()
    except UnicodeDecodeError:
        # If iso-8859-1 doesn't work, try to read the content and ignore invalid characters
        with open(file_path, 'r', encoding='iso-8859-1', errors='ignore') as f:
            content = f.read()
    
    # Replace tabs and spaces with commas
    new_content = content.replace('\t', ',').replace(' ', ',')
    
    # Save the new version of the file using iso-8859-1 encoding
    with open(file_path, 'w', encoding='iso-8859-1') as f:
        f.write(new_content)

# Get the path of the directory where this Python script is located
directory = os.path.dirname(os.path.realpath(__file__))

# Loop through all the files in the specified directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory, filename)
        replace_tabs_and_spaces_with_commas_in_file(file_path)
        print(f"Processed {file_path}")
