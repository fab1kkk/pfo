import os

def get_file_extension(file : str):
    return file.split('.')[-1]

def get_files_from_dir(path) -> list:
    return os.listdir(path)