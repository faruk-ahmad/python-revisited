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


class ElectricCar(Car):
    ''' Represents an electric car '''

    def __init__(self, make, model, year):
        ''' initialize all attributes '''
        super().__init__(make, model, year)
        self.battery_size = 70

    
    def describe_battery(self):
        ''' a method to describe the size of the battery '''
        print(f'The car has a battery of {self.battery_size} KWh.')


if __name__ == '__main__':
    my_electric_car = ElectricCar('audi', 'a4', 2020)
    print(my_electric_car.get_descriptive_name())
    my_electric_car.describe_battery()