from Interface import Dialog, ButtonInterface

class WebButton(ButtonInterface):
    def render(self):
        print("WebButton: Rendering the button...")

    def on_click(self, function):
        print("WebButton: set on click listener on the button...")

class WindowsButton(ButtonInterface):
    def render(self):
        print("WindowsButton: Rendering the button...")

    def on_click(self, function):
        print("WindowsButton: set on click listener on the button...")

class WebDialog(Dialog):
    def create_button(self):
        print("Created web dialog button...")
        return WebButton()


class WindowsDialog(Dialog):
    def create_button(self):
        print("Created web windows dialog button...")
        return WindowsButton()

class Application():
    def __init__(self):
        self.dialog = None
        self.initialize()
        self.dialog.render()
    
    def initialize(self):
        config = {
            "OS" : "Windows"
        }

        if config.get("OS") == "Windows":
            print("Creating Windows dialog....")
            self.dialog = WindowsDialog()
        
        elif config.get("OS") == "Web":
            print("Creating Web dialog....")
            self.dialog = WebDialog()
        
        else:
            raise Exception("Error! Unknown Operating System...")
