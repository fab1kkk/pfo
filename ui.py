from abc import ABC, abstractmethod

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
            print("Main Menu:")
            print("1. Create empty directories in given path based on its files extension.")
            print("2. Organize directory.")
            print("Q. Quit")
            
            option = input("Enter your option: ")
            if option.lower() == "q":
                return False
            else:
                try:
                    option = int(option)
                except Exception as e:
                    print(f"An error occured: {str(e)}")
                    continue
                self.mode.handle_selected_option(option)