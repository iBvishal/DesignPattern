from interface import DroneInterface, DuckInterface

class Duck(DuckInterface):

    def __init__(self):
        pass

    def quack(self):
        print("Duck: Quack Quack!")
    
    def fly(self):
        print("Duck: Flying!")

class Drone(DroneInterface):

    def __init__(self):
        pass

    def beep(self):
        print("Drone: beep beep!")
    
    def spinRoters(self):
        print("Drone: spinRoters!")

    def takeOff(self):
        print("Drone: takeOff!")