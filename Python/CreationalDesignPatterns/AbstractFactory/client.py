from abstractFactoryInterface import AbstractFactoryInterface

class Client():

    def __init__(self, factory: AbstractFactoryInterface):
        self.factory = factory
    
    def update_factory(self, factory: AbstractFactoryInterface):
        self.factory = factory