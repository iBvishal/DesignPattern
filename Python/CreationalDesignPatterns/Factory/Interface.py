from abc import abstractmethod

class ButtonInterface:
    def render(self):
        """Render Button on screen"""
        pass

    def on_click(self, function):
        """Create on-click listener for button"""
        pass

class Dialog:

    def __init__(self):
        self.button = None

    @abstractmethod
    def create_button(self):
        """create button method"""
        pass

    def render(self):
        button= self.create_button()
        button.on_click("doing something on click...")
        button.render()