from mode_factory import ModeFactory

class PFO:
    def __init__(self):
        self.mode = None

    def init_mode(self, mode):
        self.mode = ModeFactory.init(mode)
        
    def run(self):
        if self.mode is None:
            raise ValueError(
                "Mode must be initialized with the initialize_mode() method."
            )
        else:
            self.mode.display_UI()