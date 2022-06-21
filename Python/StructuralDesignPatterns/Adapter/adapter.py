from interface import DuckInterface
from application import Drone

class DroneToDuckAdapter(DuckInterface):

    def __init__(self, drone):
        self.drone = drone
    
    def quack(self):
        """Adapt the beep behaviour of drone as Quack behaviour."""
        self.drone.beep()

    def fly(self):
        """Adapt the Spinroters, takeoff behaviour of drone as Fly behaviour."""
        self.drone.spinRoters()
        self.drone.takeOff()