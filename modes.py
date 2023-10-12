import os
from utils import (
    get_file_extension,
    get_files_from_dir,
    create_dir,
)

from views import PFOView

class BaseMode:
    def __init__(self, pfo_instance):
        self.pfo = pfo_instance
    
    def organize(self):
        pass
    
class DirsMode(BaseMode):
    def organize(self):
        source_dir = PFOView.ask_for_directory()
        source_dir_files = os.listdir(source_dir)
        
        new_dirs = set(get_file_extension(file) for file in source_dir_files)
        
        for new_dir in new_dirs:     
            dir_path = os.path.join(source_dir,new_dir)
            os.makedirs(dir_path)
            
class DesktopMode(BaseMode):
    def organize(self):
        print("organize Desktop!")
        
