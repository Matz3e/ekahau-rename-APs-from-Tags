import json
import os
import zipfile
import shutil

def replace_comcab_with_tag(access_points, tag_keys, old_comcab, floor):
    for access_point in access_points:
        if access_point["name"].startswith("usw" + old_comcab + "-" + floor):
            tags = access_point.get("tags", [])
            if tags:
                tag_key_id = tags[0]["tagKeyId"]
                tag_key = next((key["key"] for key in tag_keys if key["id"] == tag_key_id), None)
                if tag_key is not None:
                    new_name = access_point["name"].replace("usw" + old_comcab + "-" + floor, "usw" + tag_key + "-" + floor)
                    access_point["name"] = new_name

def process_zip_file(zip_file_path, old_comcab, floor):
    # Extract the contents of the original zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('temp_extracted_original')

    # Load and process tagKeys.json and accessPoints.json
    with open('temp_extracted_original/tagKeys.json', 'r') as tag_keys_file:
        tag_keys_data = json.load(tag_keys_file)["tagKeys"]

    with open('temp_extracted_original/accessPoints.json', 'r') as access_points_file:
        access_points_data = json.load(access_points_file)["accessPoints"]

    # Replace old ComCab with the corresponding tag in accessPoints.json
    replace_comcab_with_tag(access_points_data, tag_keys_data, old_comcab, floor)

    # Save the updated data back to accessPoints.json
    os.makedirs('temp_extracted_updated', exist_ok=True)
    with open('temp_extracted_updated/accessPoints.json', 'w') as access_points_file:
        json.dump({"accessPoints": access_points_data}, access_points_file, indent=2)

    # Create a new zip file with the updated contents
    with zipfile.ZipFile('updated_file.esx', 'w') as zip_ref:
        for foldername, subfolders, filenames in os.walk('temp_extracted_original'):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                arcname = os.path.relpath(file_path, 'temp_extracted_original')
                zip_ref.write(file_path, arcname)

        # Add the updated accessPoints.json to the new zip file
        zip_ref.write('temp_extracted_updated/accessPoints.json', 'accessPoints.json')

    # Clean up temporary files and folders
    shutil.rmtree('temp_extracted_original')
    shutil.rmtree('temp_extracted_updated')

if __name__ == "__main__":
    # List all .esx files in the current directory
    esx_files = [file for file in os.listdir() if file.endswith(".esx")]

    if not esx_files:
        print("No .esx files found in the current directory.")
    else:
        print("Found the following .esx files:")
        for i, esx_file in enumerate(esx_files, start=1):
            print(f"{i}. {esx_file}")

        # Ask the user to select a file for processing
        selection = input("Enter the number of the .esx file to process: ")

        try:
            selected_index = int(selection) - 1
            selected_esx = esx_files[selected_index]

            # Ask for the old ComCab and floor to replace
            old_comcab = input("Enter the old ComCab (3-digit number after 'usw'): ")
            floor = input("Enter the floor (e.g., 'u1', 'u2', '00', '01', '02', etc.): ")

            # Process the selected .esx file
            process_zip_file(selected_esx, old_comcab, floor)

            print(f"Processing complete for {selected_esx}.")
        except (ValueError, IndexError):
            print("Invalid selection. Please enter a valid number.")
