import os
import json
import random
import requests
import warnings
from pathlib import Path
from base64 import b64decode

from .images import image_ids

def random_image_id():
    return random.choice(image_ids)

class EarthViewImage():
    def __init__(self,
                 id=random_image_id(),
                 retrieve_metadata=True):
        if id in image_ids:
            self.id = str(id)
        else:
            raise ValueError("ID {id} not found in known list of Earth View images.")

        if retrieve_metadata:
            self.retrieve_metadata()

    def retrieve_metadata(self):
        raw_json = requests.get(f"https://www.gstatic.com/prettyearth/assets/data/v3/{self.id}.json")
        metadata = json.loads(raw_json.content)

        strip_prefix = lambda b: b[b.find("/9"):]

        self.image_data = b64decode(strip_prefix(metadata.pop("dataUri")))

        for k, v in metadata.items():
            setattr(self, k, v)

    def save(self, path=None, overwrite=False):
        path = Path(path or os.getcwd())

        if path.is_dir():
            target_file = path / f"{self.id}.jpg"
        else:
            if path.is_file() and not overwrite:
                warnings.warn(f"Skipped download to {path.as_posix()} because overwrite is set to false.")
            target_file = path

        with open(target_file, "wb") as dst:
            dst.write(self.image_data)

        return target_file.as_posix()
