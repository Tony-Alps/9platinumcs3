#1. 
#    a. Duck typing is when "if something looks like a duck and quacks like a duck, then it is a duck". Based on the video, it's when something has a method that is the same as the other objects' method, even if it isn't in the same class as the other objects, it can be run. Just as Bro Code said, "If it looks like a duck and quacks like a duck, then its a duck".

#    b. All the car object needed is a method that has the same name as the other objects in the Animal class.

#2. 
#    a.
class Car():
    def move(self):
        print("The car drives on the road.")

class Boat():
    def move(self):
        print("The boat sails on water.")

class Drone(): 
    def move(self):
        print("The drone flies in the sky")

car1=Car()
boat1=Boat()
drone1=Drone()

def start_trip(vehicle):
    vehicle.move()

start_trip(car1)
start_trip(boat1)
start_trip(drone1)


# b. The code in 2.2 demonstrates polymorphism by giving a single method to many classes and letting multiple objects run it