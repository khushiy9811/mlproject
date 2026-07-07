import os
import sys
import dill
import numpy as np
import pandas as pd

from src.exception import CustomException


def save_object(file_path, obj):
    try:
        # Get the directory path
        dir_path = os.path.dirname(file_path)

        # Create directory if it doesn't exist
        os.makedirs(dir_path, exist_ok=True)

        # Save the object
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)