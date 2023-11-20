Ekahau Access Points Update Script
Description

This script is designed to replace placeholders in Access Point names based on Tag Keys defined in a separate JSON file. The goal is to automatically rename access points in Ekahau by replacing placeholders with the corresponding Tag Keys. The Access Points are expected to follow the naming convention uswXXX-Floor+SequentialNumber in Ekahau.

The script also ensures that in Ekahau, each access point is assigned a tag with the proper number, and only one tag per access point is allowed. The tag should only contain the number, excluding any additional characters like "CC."
Prerequisites

    Python (Version 3.x is recommended)
    Access to the JSON files for Tag Keys (tagKeys.json) and Access Points (accessPoints.json)
    Save the .esx file local. Rename it to .zip - replace the generated accessPoints.json. Zip it and rename it so .esx again.



Run the Script:

Navigate to the cloned repository directory and execute the script:

bash

    python script.py

    Make sure that the tagKeys.json and accessPoints.json files are in the same directory as the script.

    Review the Results:

    The script will replace the placeholders in the Access Point names following the naming convention uswXXX-Floor+SequentialNumber, set the appropriate tag in Ekahau Pro Zone, and ensure only one tag per access point, containing only the number.

Notes

    This script assumes that each access point has only one tag, and the tag key is present in the tag. Ensure these assumptions match your configuration.

    Access Points in Ekahau should adhere to the naming convention uswXXX-Floor+SequentialNumber.

    Each access point in Ekahau is assigned a tag with the proper number, and only one tag per access point is allowed. The tag should only contain the number, excluding any additional characters like "CC."

    For issues or questions, feel free to contact the developer.

Author
