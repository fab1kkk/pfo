from modes import DesktopMode, DirsMode
from views import PFOView
from utils import mode_allowed, get_files_from_dir, get_file_extension
from configs import MODES

class BasePFO:
    def __init__(self):
        self._mode = None
        self._allowed_modes = MODES
        self._initialized = False

    @property
    def mode(self):
        return self._mode

    @property
    def allowed_modes(self):
        return self._allowed_modes

    def init_mode(self, mode: str):
        if not mode_allowed(mode, self._allowed_modes):
            raise ValueError(
                f"Invalid mode. Allowed modes: {self._allowed_modes}, given '{mode}'"
            )
        self._initialized = True
        self._mode = mode.lower()

    @property
    def initialized(self):
        return self._initialized
    
    def check_init_mode(self):
        if not self.initialized:
            raise ValueError(
                "init_mode must be called before calling organize"
            )
        return True

class PFO(BasePFO):
    def get_files(self):
        path = PFOView.ask_for_directory()
        files = get_files_from_dir(path)
        return files

    def organize(self):
        if self.mode is None:
            raise ValueError(
                "Mode must be initialized with the init_mode() method."
            )
        
        mode_classes = {
            'dirs' : DirsMode(self),
            'desktop' : DesktopMode(self),
        }
        
        mode_class = mode_classes.get(self.mode)
        mode_class.organize()
