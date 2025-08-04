# storage.py
import json
from json.decoder import JSONDecodeError

def save_archived_task(task, filename="archive.json"):
    try:
        with open(filename, "r") as f:
            archive = json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        archive = []

    archive.append(task)
    with open(filename, "w") as f:
        json.dump(archive, f, indent=4)
