from abc import ABC, abstractmethod

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

class UInterface(ABC):
    def __init__(self, mode_instance):
        self.mode = mode_instance
        self.greet()
        
    def greet(self):
        print(f"Mode on: {self.mode}")
        
    @abstractmethod
    def show():
        pass

class DirsModeUI(UInterface):
    def show(self):
        while True:
            print(f"Main Menu:")
            print("1. Create empty directories in given path based on its files extension")
            print("2. Organize directory.")
            print("Q. Quit")
            
            option = input("Enter your option: ")
            
            if option == "Q".lower():
                print("Goodbye!")
                return False
            else:
                option = int(option)
                self.mode.handle_selected_option(option)