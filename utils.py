import os
from configs import TYPES

def get_file_extension(file : str):
    return file.split('.')[-1]

def get_files_from_dir(path) -> list:
    return os.listdir(path)

def type_allowed(type):
    if type:
        return True if type.lower() in TYPES else False
    return False
