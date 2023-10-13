import os
from abc import ABC, abstractmethod

from utils import (
    get_file_extension,
    mode_allowed,
)
from config import ALLOWED_MODES
from ui import DirsModeUI

class Mode(ABC):
    _allowed_modes = ALLOWED_MODES

    def __init__(self):
        self._mode = None
        self._ui = None
        
    def __str__(self):
        return self._mode

    def set_mode(self, mode: str):
        mode = mode.lower()
        if not mode_allowed(mode, self.allowed_modes):
            raise ValueError(
                f"Invalid mode. Allowed modes: {self.allowed_modes}, given '{mode}'"
            )
        self._mode = mode

    @property
    def mode(self):
        return self._mode

    @property
    def allowed_modes(self):
        return self._allowed_modes

    @abstractmethod
    def display_UI(self):
        pass

    def handle_selected_option(
        self, option: int, options: dict, *args, **kwargs
    ) -> bool:
        _call = options.get(option)
        if _call:
            _call(*args, **kwargs)
            return True
        return False

class DirsMode(Mode):
    def display_UI(self):
        self.ui = DirsModeUI(self)
        self.ui.show()
        
    def handle_selected_option(self, option: int, *args, **kwargs) -> bool:
        options = {
            1: self.create_dirs_from_file_extensions,
            2: self.move_files_to_dirs,
        }
        return super().handle_selected_option(
            option=option, options=options, *args, **kwargs
        )

    def create_dirs_from_file_extensions(self, dir, overwrite=False):
        dir_files = []
        for item in os.listdir(dir):
            file = os.path.join(dir, item)

            if os.path.isfile(file):
                dir_files.append(file)

        file_extensions = set(get_file_extension(file) for file in dir_files)
        for extension in file_extensions:
            if extension:
                created_file = os.path.join(dir, extension)
                os.makedirs(created_file, exist_ok=overwrite)
                self.ui.print_success(f"created -> {created_file}")

    def move_files_to_dirs(self):
        self.ui.print_success("One day it will work")


class AnotherMode(Mode):
    def display_UI(self):
        pass
    def handle_selected_option(self, option: int):
        pass
    
