import os
from abc import ABC, abstractmethod

from utils import (
    get_file_extension,
    mode_allowed,
)
from config import ALLOWED_MODES
import ui
import interaction


class Mode(ABC):
    _allowed_modes = ALLOWED_MODES
    def __init__(self):
        self._mode = None

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

    @abstractmethod
    def handle_selected_option(self, option: int):
        pass
    
    def call_handled_option(self, option, options):
        _call = options.get(option)
        if _call:
            _call()


class DirsMode(Mode):
    def display_UI(self):
        _ui = ui.DirsModeUI(self)
        _ui.show()

    def handle_selected_option(self, option: int):
        options = {
            1: self.create_dirs_from_extensions,
        }
        self.call_handled_option(option, options)

    def create_dirs_from_extensions(self):
        dir = interaction.ask_for_dir_path()
        dir_files= os.listdir(dir)
        file_extensions = set(get_file_extension(os.path.join(dir,file)) for file in dir_files)
        for extension in file_extensions:
            if extension:
                dir_path = os.path.join(dir, extension)
                os.makedirs(dir_path, exist_ok=True)
                interaction.print_success(f"created -> {dir_path}")


class DesktopMode(Mode):
    def display_UI(self):
        pass

    def handle_selected_option(self, option: int):
        pass
