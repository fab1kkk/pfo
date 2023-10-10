from core import (
    FileDir, 
    FileView,
    PathModel
)

if __name__ == '__main__':
    path = PathModel()
    file_view = FileView()
    file_dir = FileDir(path, file_view)
    
    print(file_dir.get_files())
    
    
    