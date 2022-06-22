class SubjectInterface:
    def registerObserver(self, observer):
        """Register an observer to the subject."""
        pass

    def removeObserver(self, observer):
        """Remove an observer from the subject."""
        pass

    def notifyObservers(self):
        """Notify observers."""
        pass
    
    def update_data(self, data):
        """Update the subject"""
        pass

class ObserverInterface:
    def update_data(self, data):
        """Update the observer"""
        pass