class CameraApplicationInterface:

    def save(self):
        """Save the file."""
        pass

    def setShareStrategy(self,  shareStrategy):
        """Set the share strategy."""
        pass

class ShareStrategyInterface:
    def share(self):
        """Share the file with set strategy."""
        pass