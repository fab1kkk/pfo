import os
from configs import MODES

def get_file_extension(file : str) -> str | None:
    """
    Extracts and returns the file extension from a given file name or path.

    Parameters:
    file (str): A string representing the file name or path.

    Returns:
    str | None: The extracted file extension if found, or None if the input
                string does not contain a valid file extension.

    Raises:
    TypeError: If the 'file' parameter is not of type str.

    Example:
    >>> get_file_extension("document.txt")
    'txt'
    >>> get_file_extension("image.png")
    'png'
    >>> get_file_extension("no_extension")
    None
    """
    if not isinstance(file, str):
        raise TypeError(f"file must be str type, {type(file)} given")
    
    extension = file.split('.')[-1]
    
    if extension == file:
        return None
    return extension

def get_files_from_dir(path) -> list[str]:
    return os.listdir(path)

def mode_allowed(mode: str) -> bool:
    if not isinstance(mode, str):
        raise TypeError(f"type must be str type, {type(mode)} given")
    
    return True if mode.lower() in MODES else False
