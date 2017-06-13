class Car(object):
    """ A car class """
    def __init__(self, car_name):
        self.car_name = car_name



class Honda(Car):
    def __init__(self, car_model, car_type):
        self.car_model = car_model
        self.car_type = car_type