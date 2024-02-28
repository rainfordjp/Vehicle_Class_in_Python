# VehicleClass.py

class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change Order: we need to add maximum speed to the model.
    Change Order: need a way to 'read' the maximum speed from the model
    Change Order: Some developers need to use the constructor without having to provide max speed
    '''
    # Constructor. It's called when ... we instantiate an object of Vehicle type
    def __init__(self, type, max_speed = None):
        '''
        @param type: The kind of vehicle
        @param max_speed: maximum speed of the Vehicle , defaults to None
        '''
        self.type = type;
        self._thisisprivate = 42     # This is a weak attempt to 'support' data hiding
        self.max_speed = max_speed # Save a copy in the current object
        
    #An instance method. It operates on an instance of a Vehicle class 
    def printType(self):
        print (self.type)
    
    def getSpeed(self) :
        return self.max_speed
    
if __name__ == "__main__":
    # Some code can go here, if not pass
    pass