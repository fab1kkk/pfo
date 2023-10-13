from typing import Union
import os

def get_file_extension(file: str) -> str:
    """
    Extracts and returns the file extension from a given file name or path.

    Returns:
    str : The extracted file extension if found, or 'no_filetype' if the input
                string does not contain a valid file extension.
    """
    
    if not isinstance(file, str):
        raise TypeError(f"file must be str type, {type(file)} given")
    
    if not os.path.isfile(file):
        return None
    
    extension = file.split(".")[-1]
    if extension == file:
        return 'no_filetype'
    return extension


def mode_allowed(
    mode: str, allowed_modes: Union[list[str], tuple[str], set[str]]
) -> bool:
    """
    Check if the given mode is allowed based on an iterable of allowed modes.

    Returns:
    bool: True if the mode is allowed (found in the iterable of allowed modes),
          False otherwise.
    """
    
    if not isinstance(mode, str):
        raise TypeError(f"type must be str type, {type(mode)} given")
    if not isinstance(allowed_modes, (list, tuple, set)) or not all(
        isinstance(item, str) for item in allowed_modes
    ):
        raise TypeError("allowed_modes must be an iterable containing strings")

    return True if mode.lower() in allowed_modes else False