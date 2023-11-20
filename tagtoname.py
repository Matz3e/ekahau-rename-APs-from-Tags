import json

def replace_placeholders(access_points, tag_keys):
    for access_point in access_points:
        tags = access_point.get("tags", [])
        if tags:
            tag_key_id = tags[0]["tagKeyId"]
            tag_key = next((key["key"] for key in tag_keys if key["id"] == tag_key_id), None)
            if tag_key is not None:
                access_point["name"] = access_point["name"].replace("XXX", tag_key)

if __name__ == "__main__":
    # Lese die Inhalte der JSON-Dateien
    with open("tagKeys.json", "r") as tag_keys_file:
        tag_keys_data = json.load(tag_keys_file)["tagKeys"]

    with open("accessPoints.json", "r") as access_points_file:
        access_points_data = json.load(access_points_file)["accessPoints"]

    # Ersetze die Platzhalter
    replace_placeholders(access_points_data, tag_keys_data)

    # Speichere die aktualisierten Daten zurück in die accessPoints.json-Datei
    with open("accessPoints.json", "w") as access_points_file:
        json.dump({"accessPoints": access_points_data}, access_points_file, indent=2)

    print("Platzhalter erfolgreich ersetzt.")
