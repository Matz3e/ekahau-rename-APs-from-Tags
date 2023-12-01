import os
import zipfile
import json
import re
import sys

def replace_names(data):
    pattern = r'(usw\d{3})-([a-zA-Z0-9]+)-(\d{3})'
    def replace(match):
        prefix, suffix, number = match.groups()
        new_number = str(int(number) + 1).zfill(3)
        return f"{prefix}-{suffix}-{new_number}"
    return re.sub(pattern, replace, data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_names.py file.esx")
        sys.exit(1)
    filename = sys.argv[1]
    directory = os.path.splitext(filename)[0]
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(directory)
    with open(os.path.join(directory, 'accessPoints.json'), 'r') as f:
        data = f.read()
        modified_data = replace_names(data)
    with open(os.path.join(directory, 'accessPoints.json'), 'w') as f:
        f.write(modified_data)
    new_filename = os.path.join(os.path.dirname(filename), f"modified_{os.path.basename(filename)}")
    with zipfile.ZipFile(new_filename, 'w') as zip_ref:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zip_ref.write(file_path, os.path.relpath(file_path, directory))
    print(f"Modified file saved as {new_filename}")
    # optional: delete temporary directory
    os.rmdir(directory)
