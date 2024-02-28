# main.py
# import VehiclePackage
from vehiclePackage.VehicleClass import *

if __name__ == "__main__":
    # Instantiate an object if type vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to constructor
    myCorvette.printType() # Invoke a method on the object
    
    #invoke the getter for max speed,store the return value in a variable
    max_speed = myCorvette.getSpeed()
    print(max_speed)
    
    #instantiate another Vehicle object, you can name it
    myAccord = Vehicle("Car", 180) #myAccord is an object of type Vehicle
    
    # I want a list of 3 vehicles: Car boat and spaceship
    # you can pick names and properties
    # I want a friendly output to demo my work
    myVehicles = [Vehicle("Tacoma", 150),
                  Vehicle("Waverunner", 120),
                  Vehicle("Falcon", 4000)]
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())