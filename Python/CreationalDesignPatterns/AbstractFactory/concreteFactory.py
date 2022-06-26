from abstractFactoryInterface import AbstractFactoryInterface

class ModernFurniture(AbstractFactoryInterface):
    def createChair(self):
        print("Create Modern Chair")

    def createTable(self):
        print("Create Modern Table")
    
    def createSofa(self):
        print("Create Modern Sofa")

class AntiqueFurniture(AbstractFactoryInterface):
    def createChair(self):
        print("Create Antique Chair")

    def createTable(self):
        print("Create Antique Table")
    
    def createSofa(self):
        print("Create Antique Sofa")
        
