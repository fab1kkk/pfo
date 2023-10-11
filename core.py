from utils import type_allowed, get_files_from_dir, get_file_extension

from configs import TYPES


class FileOrganizer:
    def __init__(self, type: str): 
        self._type = type

    @property
    def type(self):
        return self._type
            
    @type.setter
    def type(self, newtype):
        if not type_allowed(newtype):
           raise Exception(f"Type must ba an allowed type.\nAllowed types:\n{TYPES}")
        self._type = newtype.lower()
        
    def organize(self):
        pass


class OrganizerIO:
    """A utility class for handling file organization input and output.

    This class provides methods for interacting with the user to obtain
    file paths to be organized and for displaying information related to
    selected paths.
    """

    @staticmethod
    def get_path_from_user():
        return input("Enter a path to be organized: ")

    @staticmethod
    def display_path(path):
        print(f"Selected path {path}")


class FileDir:
    def __init__(self, path_model, view):
        self.path_model = path_model
        self.view = view

    def ask_for_path(self):
        file_path = self.view.get_path_from_user()
        self.path_model.set_path(file_path)

    def show_path(self):
        file_path = self.path_model.get_path()
        self.view.display_path(file_path)

    def get_files(self) -> list | None:
        if not self.path_model.get_path():
            p = self.view.get_path_from_user()
            self.path_model.set_path(p)
        files = get_files_from_dir(self.path_model.get_path())
        return files

    def get_extensions(self) -> list | None:
        extensions = []
        files_in_dir = self.get_files()
        for f in files_in_dir:
            ext = get_file_extension(f)
            extensions.append(ext)

        return extensions
