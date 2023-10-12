from modes import BaseMode, DirsMode, DesktopMode
mode_classes = {
    'dirs': DirsMode(),
    'desktop' : DesktopMode(),
}


class ModeFactory:
    @staticmethod
    def init(mode: str) -> BaseMode:
        mode = mode.lower()
        mode_instance = ModeFactory.map_mode(mode)
        mode_instance.set_mode(mode)
        return mode_instance
    
    @staticmethod
    def map_mode(mode : str) -> BaseMode:
        mapped_mode = mode_classes.get(mode)
        if mapped_mode is None:
            raise ValueError(f"Invalid mode: {mode}")
        
        return mapped_mode