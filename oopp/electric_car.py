class Car():
    ''' a simple class to represent a Car '''
    
    def __init__(self, make, model, year):
        ''' init method to initialize the attributes '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gass_remaining = 0


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


    def fill_gass_tank(self, gass_to_fill):
        ''' a simple method to fill gass tank '''
        if gass_to_fill > 0:
            self.gass_remaining += gass_to_fill
        else:
            print(f'Invalid quantity.')

'''
If the number of attributes and methods for an object in a class gets larger and too many in 
numbers, then we can move those attributes and methods to a different class, like the bellow 
class Battery. Initially we defined the attributes inside the ElectricCar class, but it seems
that the number was increasing too fast. So we moved those in this class. And now we can get
an instance of Battery class as attributes in the ElectricCar class and access all the attributes
and methos in the similar way as done previously.
'''
class Battery():
    ''' a class represents the battery attributes and methods of Electric car '''

    def __init__(self, battery_size = 70):
        ''' initialize attributes '''
        self.battery_size = battery_size


    def describe_battery(self):
        ''' a method to describe the size of the battery '''
        print(f'The car has a battery of {self.battery_size} KWh.')


    def get_range(self):
        ''' a method that describes the range based on the current battery size '''
        if self.battery_size > 80:
            range = 240
        elif self.battery_size > 60:
            range = 180
        else:
            range = 100
        
        print(f'The car can go around {range} on a full charge.')


class ElectricCar(Car):
    ''' Represents an electric car '''

    def __init__(self, make, model, year):
        ''' initialize all attributes '''
        super().__init__(make, model, year)
        self.battery = Battery()

    
    def fill_gass_tank(self, gass_to_fill):
        ''' since electric car does not need gass, let override this method and ignore if called '''
        print(f'Electric car does not require gass.')


if __name__ == '__main__':
    my_electric_car = ElectricCar('audi', 'a4', 2020)
    print(my_electric_car.get_descriptive_name())
    my_electric_car.battery.describe_battery()
    my_electric_car.battery.get_range()
    my_electric_car.fill_gass_tank(10)