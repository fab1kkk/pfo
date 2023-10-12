import os
from typing import Union

from configs import MODES


def get_file_extension(file: str) -> str | None:
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

    extension = file.split(".")[-1]
    if extension == file:
        return 'no_filetype'
    return extension


def get_files_from_dir(path: str) -> list[str]:
    """
    Get a list of files in the specified directory.

    Parameters:
    path (str): A string representing the directory path.

    Returns:
    list[str]: A list of file names in the directory.

    Raises:
    TypeError: If the 'path' parameter is not of type str.
    FileNotFoundError: If the specified path is not found.

    Example:
    >>> get_files_from_dir("/path/to/directory")
    ['file1.txt', 'file2.jpg']
    """
    if not isinstance(path, str):
        raise TypeError(f"type must be str type, {type(path)} given")
    try:
        return os.listdir(path)
    except FileNotFoundError as e:
        raise e


def mode_allowed(
    mode: str, allowed_modes: Union[list[str], tuple[str], set[str]]
) -> bool:
    """
    Check if the given mode is allowed based on an iterable of allowed modes.

    Parameters:
    mode (str): A string representing the mode to be checked.
    allowed_modes (Union[list[str], tuple[str], set[str]]):
    An iterable (e.g., list, tuple, or set) of allowed modes.

    Returns:
    bool: True if the mode is allowed (found in the iterable of allowed modes),
          False otherwise.

    Raises:
    TypeError: If the 'mode' parameter is not of type str.
    TypeError: If the 'allowed_modes' parameter is not an iterable containing strings.

    Example:
    >>> allowed_modes = ["read", "write", "execute"]
    >>> mode_allowed("read", allowed_modes)
    True
    >>> mode_allowed("modify", allowed_modes)
    False
    """
    if not isinstance(mode, str):
        raise TypeError(f"type must be str type, {type(mode)} given")
    if not isinstance(allowed_modes, (list, tuple, set)) or not all(
        isinstance(item, str) for item in allowed_modes
    ):
        raise TypeError("allowed_modes must be an iterable containing strings")

    return True if mode.lower() in allowed_modes else False


def create_dir(path: str, suffix: str = "s"):
    os.mkdir(path=path)
