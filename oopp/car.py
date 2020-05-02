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


    def update_odometer(self, mileage):
        ''' a method to update the odometer_reading attribute value '''
        self.odometer_reading = mileage


if __name__ == '__main__':
    my_car = Car('audi', 'a4', 2014)

    print(my_car.get_descriptive_name())
    my_car.read_odometer()

    #modifying the attribute value directly by accesing using the instance
    my_car.odometer_reading = 50
    my_car.read_odometer()

    #modify the attribute value using a method
    my_car.update_odometer(100)
    my_car.read_odometer()