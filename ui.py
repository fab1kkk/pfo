from abc import ABC, abstractmethod

class UI(ABC):
    def __init__(self, mode_instance):
        self.mode = mode_instance
        self.greet()
        
    def greet(self):
        print(f"Mode on: {self.mode}")
        
    @abstractmethod
    def show():
        pass
    
    def ask_for_overwrite_choice(self, positive = 'y', negative = 'n'):
        while True:
            answer = input(f"Do you want to overwrite existing files? ({positive}/{negative}): ")
            answer = answer.lower()
            if answer == positive:
                return True
            elif answer == negative:
                return False
            else:
                print(f"Invalid choice. Please enter '{positive}' or '{negative}'.")
    
    def ask_for_dir_path(self):
        return input("Enter the directory path: ")
    
    def print_success(self, content):
        print(f"\033[92m{content}\033[0m")



class DirsModeUI(UI):
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
                
                if option == 1:
                    dir = self.ask_for_dir_path()
                    overwrite = self.ask_for_overwrite_choice()
                    self.mode.handle_selected_option(option, dir=dir, overwrite = overwrite)