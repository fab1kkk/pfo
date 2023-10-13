from mode import Mode, DirsMode
from ui import UI, DirsModeUI

mode_classes = {
    'dirs': DirsMode()
}


class ModeFactory:
    @staticmethod
    def init(mode: str) -> Mode:
        mode_instance = ModeFactory.map_mode(mode)
        mode_instance.set_mode(mode)
        return mode_instance
    
    @staticmethod
    def map_mode(mode : str) -> Mode:
        mapped_mode = mode_classes.get(mode)
        if mapped_mode is None:
            raise ValueError(f"Invalid mode: {mode}")
        
        return mapped_mode
    
