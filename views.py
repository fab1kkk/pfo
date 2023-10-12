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