from application import Drone, Duck
from adapter import DroneToDuckAdapter

drone = Drone()
duck  = Duck()

drone_adapted_as_duck = DroneToDuckAdapter(drone = drone)
drone_adapted_as_duck.quack()
drone_adapted_as_duck.fly()