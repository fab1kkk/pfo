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
    _running = True

    @staticmethod
    def stop():
        UI._running = False

    @classmethod
    def dirs(cls):
        while cls._running:
            print(
                """
                Select what you want to do. You can select multiple options at once.
                - [] Create directories based on file extensions within the directory.
                - [] Create blab blaba
                - [] Create blab blaba
                - [] Create blab blaba
                - [] Create blab blaba
                """
            )
            option = input('What you want to do. Q to exit.\nOption:')
            if option.lower() == 'q':
                UI.stop()
