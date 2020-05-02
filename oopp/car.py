class Car():
    ''' a simple class to represent a Car '''
    
    def __init__(self, make, model, year):
        ''' init method to initialize the attributes '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        ''' Return a neatly formatted descriptive name '''
        long_name = f'{str(self.year)}-{self.make}-{self.model}'
        return long_name


    def read_odometer(self):
        ''' prints a statement showing the odometer mileage '''
        print(f'The car has {self.odometer_reading} mileage on it.')



if __name__ == '__main__':
    my_car = Car('audi', 'a4', 2014)

    print(my_car.get_descriptive_name())
    my_car.read_odometer()