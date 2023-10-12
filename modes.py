import os
from abc import ABC, abstractmethod

from utils import (
    get_file_extension,
    mode_allowed,
)

from configs import ALLOWED_MODES
from views import PFOView, UI

class BaseMode(ABC):
    def __init__(self):
        self._mode = None
        self._allowed_modes = ALLOWED_MODES
        self._initialized = False

    def set_mode(self, mode : str):
        mode = mode.lower()
        if not mode_allowed(mode, self.allowed_modes):
            raise ValueError(
                f"Invalid mode. Allowed modes: {self.allowed_modes}, given '{mode}'"
            )
        self._mode = mode
        self._initialized = True
        
    @property
    def mode(self):
        return self._mode
    
    @property
    def allowed_modes(self):
        return self._allowed_modes
    
    @property
    def initialized(self):
        return self._initialized
    
    @abstractmethod
    def display_UI(self):
        pass
                
class DirsMode(BaseMode):
    def display_UI(self):
        UI.dirs()
    
    def create_dirs_from_extensions(self):
        source_dir = PFOView.ask_for_directory()
        source_dir_files = os.listdir(source_dir)
        
        new_dirs = set(get_file_extension(file) for file in source_dir_files)
        
        for new_dir in new_dirs:     
            dir_path = os.path.join(source_dir,new_dir)
            os.makedirs(dir_path)
            
class DesktopMode(BaseMode):
    def display_UI(self):
        print("""THIS IS UI FOR DesktopMode""")
        
