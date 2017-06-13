class Car(object):
    """ A car class to depict the type, model, and name of various vehicles """

    def __new__(myclass, name="General", model="GM", car_type="saloon", num_of_wheels=4
        ,parked_speed=0, moving_speed=1000):
            return super(Car, myclass).__new__(myclass)


    def __init__(self, name="General", model="GM", car_type="saloon", speed=0):
            self.name = name
            self.model = model
            self.car_type = car_type
            self.speed = speed
            self.num_of_wheels = 4
        
            if self.name == "Porshe" or self.name == "Koenigsegg":
                self.num_of_doors = 2
            else:
                self.num_of_doors = 4
            
            if self.car_type=="trailer":
                self.num_of_wheels = 8
                self.speed = 0    


    def is_saloon(self):
        if self.car_type is not "trailer":
            return True
        return False


    def drive(self, speed):
            if self.car_type is not "trailer":
                self.speed = 10 ** speed
            else:
                self.speed = 77
            return self