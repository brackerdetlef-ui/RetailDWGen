from pathlib import Path
import yaml


class Config:

    def __init__(self, filename: str = "config/config.yaml"):

        with open(filename, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, *keys):

        value = self.data

        for key in keys:
            value = value[key]

        return value
