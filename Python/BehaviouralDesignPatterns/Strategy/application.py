from abc import abstractmethod

from interface import CameraApplicationInterface, ShareStrategyInterface
from shareStrategy import EmailStrategy, SlackStrategy


class CameraApplicationAbstractClass(
    CameraApplicationInterface, 
    ShareStrategyInterface):

    def __init__(self):
        self.shareStrategy = None

    """
    As of every camera applicatiom, they will have different edit mechanism
    """
    @abstractmethod
    def edit(self):
        pass

    def setShareStrategy(self, shareStrategy):
        self.shareStrategy = shareStrategy

    def save(self):
        print("save called")
    
    def share(self):
        self.shareStrategy.share()

class BasicCameraApplication(CameraApplicationAbstractClass):
    
    def __init__(self,  shareStrategy = None):
        self.shareStrategy = shareStrategy
    
    def edit(self):
        print("edit called for  BasicCameraApplication...")

class CameraPlusApplication(CameraApplicationAbstractClass):
    
    def __init__(self,  shareStrategy = None):
        self.shareStrategy = shareStrategy
    
    def edit(self):
        print("edit called for  CameraPlusApplication...")
