import os
from typing import Self

import yaml

from api.schemas import FullResume

DIR = os.path.dirname(__file__)

class CV(FullResume):
    @classmethod
    def load(cls) -> Self:
        cv_path = os.environ.get("CV_FILE_PATH", "../../cv.yaml")
        with open(os.path.join(DIR, cv_path), "r") as file:
            cv_data = yaml.safe_load(file)
            cv = cls.model_validate(cv_data["content"])
        return cv

def load_cv():
    return CV.load()
