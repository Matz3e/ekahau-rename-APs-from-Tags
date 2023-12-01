Ekahau Access Points Update Script

Description

This script is designed to replace placeholders in Access Point names based on Tag Keys defined in a separate JSON file. The goal is to automatically rename access points in Ekahau by replacing placeholders with the corresponding Tag Keys. The Access Points are expected to follow the naming convention uswXXX-Floor+SequentialNumber in Ekahau.
The script also ensures that in Ekahau, each access point is assigned a tag with the proper number, and only one tag per access point is allowed. The tag should only contain the number, excluding any additional characters like "CC."

Prerequisites

Python (Version 3.x is recommended)
Ekahau Projekt local saved


Run the Script:

Navigate to the cloned repository directory and execute the script:
Make sure that the ekahau projekt file are in the same directory as the script.

python3 cc_to_tags_v1.1.py 

Found the following .esx files:
1. modified_updated_file.esx
2. test.esx
3. updated_file.esx
4. modified_Untitled.esx

Enter the number of the .esx file to process: 2
Enter the old ComCab (3-digit number after 'usw'): XXX
Enter the floor (e.g., 'u1', 'u2', '00', '01', '02', etc.): 00
Processing complete for USB_LC2023_OP-OST.esx.


Notes

This script assumes that each access point has only one tag, and the tag key is present in the tag. Ensure these assumptions match your configuration.
Access Points in Ekahau should adhere to the naming convention uswXXX-Floor+SequentialNumber.
Each access point in Ekahau is assigned a tag with the proper number, and only one tag per access point is allowed. The tag should only contain the number, excluding any additional characters like "CC."
For issues or questions, feel free to contact the developer.

