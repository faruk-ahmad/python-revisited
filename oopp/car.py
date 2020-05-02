''' A class that can be used to represent a Car '''

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
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f'You can not roll back to an odometer reading.')


    def increment_odometer(self, mileage):
        ''' a method to increment the odometer reading by a certain amount of mileage '''
        if mileage > 0:
            self.odometer_reading += mileage
        else:
            print('You can not decrease the odometer reading.')


if __name__ == '__main__':
    my_car = Car('audi', 'a4', 2014)

    print(my_car.get_descriptive_name())
    my_car.read_odometer()

    #modifying the attribute value directly by accesing using the instance
    my_car.odometer_reading = 50
    my_car.read_odometer()

    #modify the attribute value using a method
    my_car.update_odometer(10)
    my_car.read_odometer()

    #incrementing attributes value by a method
    my_used_car = Car('Toyota', 'ac3', 2019)
    my_used_car.increment_odometer(2389)
    print(my_used_car.get_descriptive_name())
    my_used_car.read_odometer()
    my_used_car.increment_odometer(-5)
    my_used_car.read_odometer()