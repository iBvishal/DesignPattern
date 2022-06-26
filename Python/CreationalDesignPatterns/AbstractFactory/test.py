from concreteFactory import ModernFurniture, AntiqueFurniture
from client import Client

modernFactory = ModernFurniture()
antiqueFactory = AntiqueFurniture()

client1 = Client(factory= modernFactory)
client1.factory.createChair()
client1.factory.createTable()
client1.factory.createSofa()

client1.update_factory(factory= antiqueFactory)
client1.factory.createChair()
client1.factory.createTable()
client1.factory.createSofa()