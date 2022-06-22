from interface import SubjectInterface, ObserverInterface

class Subject(SubjectInterface):

    def __init__(self):
        self.observers = []
        self.data = None

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update_data(data  = self.data)
    
    def update_data(self, data):
        print("Update subject Data")
        self.data = data
        self.notifyObservers()

class Observer(ObserverInterface):

    def __init__(self):
        self.data = None

    def update_data(self, data):
        self.data = data
        print("Updated Data for Observer")