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
                
                if option == 1:
                    overwrite = self.ask_for_overwrite_choice()
                    self.mode.handle_selected_option(option, overwrite = overwrite)