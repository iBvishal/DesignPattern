from abc import ABC, abstractmethod

from interface import CameraApplicationInterface, ShareStrategyInterface
from shareStrategy import EmailStrategy, SlackStrategy


class CameraApplicationAbstractClass(
    ABC, 
    CameraApplicationInterface, 
    ShareStrategyInterface):

    def __init__(self) -> None:
        self.shareStrategy = None
        super().__init__()

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
        super().__init__()
    
    def edit(self):
        print("edit called for  BasicCameraApplication...")

class CameraPlusApplication(CameraApplicationAbstractClass):
    
    def __init__(self,  shareStrategy = None):
        self.shareStrategy = shareStrategy
        super().__init__()
    
    def edit(self):
        print("edit called for  CameraPlusApplication...")
