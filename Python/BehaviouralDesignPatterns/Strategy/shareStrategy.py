from interface import ShareStrategyInterface

class EmailStrategy(ShareStrategyInterface):
    
    def __init__(self):
        pass

    def share(self):
        print("Called email share strategy")

class SlackStrategy(ShareStrategyInterface):
    
    def __init__(self):
        pass

    def share(self):
        print("Called slack share strategy")
