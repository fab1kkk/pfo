import utils

class PathModel:
    def __init__(self):
        self._path = None
        
    def set_path(self, path):
        self._path = path
        
    def get_path(self):
        return self._path
    
class FileView:
    def get_path_from_user(self):
        return input("Enter a path to be organized: ")
    
    def display_path(self, path):
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
        files = utils.get_files_from_dir(self.path_model.get_path())
        return files
        
    def get_extensions(self) -> list | None:
        extensions = []
        files_in_dir = utils.get_files_from_dir(self.path_model.get_path())
        for f in files_in_dir:
            ext = utils.get_file_extension(f)
            extensions.append(ext)
        
        