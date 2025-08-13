filename = 'dice_results.json'
import json, os

def load_file_exists():
    return os.path.isfile(filename) and os.path.getsize(filename)

def load_content():
    if not load_file_exists():
        print("File doesn't exist. Can't load due to missing file.")
        return []
    else:
        with open(filename, 'r+', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data


def save_content(data):
    with open(filename, 'w+', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
