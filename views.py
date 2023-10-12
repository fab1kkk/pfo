class PFOView:
    """A utility class for handling file organization input and output.

    This class provides methods for interacting with the user to obtain
    file paths to be organized and for displaying information related to
    selected paths.
    """

    @staticmethod
    def ask_for_directory():
        return input("Enter the directory path to organize files: ")

    @staticmethod
    def display_message(message):
        print(message)


class UI:
    def __init__(self, mode_instance):
        self.mode_instance = mode_instance
        self.running = True
        self.selected = None
    
    def stop(self):
        self.running = False
        
    def run(self):
        self.map_UI()

    def map_UI(self):
        if self.mode_instance.mode == 'dirs':
            self.show_dirs_ui()
        else:
            raise ValueError(f"UI not found for {self.mode_instance}")
            
    def show_dirs_ui(self):
        while self.running:
            print(
                f"""
Currently in {self.mode_instance}.

Select what you want to do. You can select multiple options at once.
[1] Create directories based on file extensions within the directory.
[2] Create blab blaba
[3] Create blab blaba
[4] Create blab blaba
[5] Create blab blaba
"""
            )
            option = input("What you want to do. Q to exit.\nOption: ")
            
            if option.lower() == "q":
                self.stop()
            else:
                self.mode_instance.handle_selected_option(option)
