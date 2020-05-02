class Restaurant():
    ''' A simple class representing a restaurant '''
    def __init__(self, restaurant_name, cuisine_type):
        ''' init method to initialize attributes '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restaurant(self):
        ''' a method to describe the restaurant '''
        print(f'Restaurante name: {self.restaurant_name}\nCuisine type: {self.cuisine_type}')


    def open_restaurant(self):
        ''' a method to show restaurant open or close status '''
        print(f'{self.restaurant_name} is open now.')


    def set_number_served(self, new_num_served):
        ''' a method to reset the num_served attribute with new value '''
        if new_num_served >= self.num_served:
            self.num_served = new_num_served
        else:
            print('You can not decrease the number of served customer.')

    
    def increment_number_served(self, num_of_increment):
        ''' a method to make increment to the number of served customer '''
        if num_of_increment > 0:
            self.num_served += num_of_increment
        else:
            print('You can not decrease the number of customer served.')


class User():
    ''' A simple class that represent a user '''
    def __init__(self, first_name, last_name, gender, phone_number, email, address):
        ''' init method to initialize attributes '''
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.login_attempts = 0


    def describe_user(self):
        ''' a method to displaye the summary of a user '''
        print(f'\nUser summary:')
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Phone number: {self.phone_number}')
        print(f'Login attempts: {self.login_attempts}')


    def greet_user(self):
        ''' a method to personalized greet to user '''
        if self.gender.lower() == 'male':
            print(f'Hello and welcoome Mr. {self.first_name}')
        elif self.gender.lower() == 'female':
            print(f'Hello and welcome Ms. {self.first_name}')
        else:
            print(f'Hello and welcome {self.first_name}')


    def increment_login_attempts(self):
        self.login_attempts += 1

    
    def reset_login_attempts(self):
        self.login_attempts = 0



if __name__ == '__main__':
    #excercise 9.1
    print('Excercise-9.1')
    restaurant = Restaurant('Cusine Factory', 'Sour Cusine')
    print(f'Restaurant name: {restaurant.restaurant_name}\nCuisine type: {restaurant.cuisine_type}')

    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    #excercise 9.2
    print('\nExcercise-9.2')
    restaurant1 = Restaurant('Restaurant1', 'Cuisine1')
    restaurant2 = Restaurant('Restaurant2', 'Cuisine2')
    restaurant3 = Restaurant('Restaurant3', 'Cuisine3')

    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

    #excercise 9.3
    print('\nExcercise-9.3')
    user1 = User('Faruk', 'Ahmad', 'Male', '09093493602', 'faruk.csebrur@gmail.com', 'katsushika-ku')
    user2 = User('Luna', 'Deshai', 'Female', '01742128964', 'luna.deshai@gmail.com', 'Mumbai')
    user3 = User('Hemlock', 'Hem', 'others', '09333393993', 'hemlock@yahoo.com', 'hemlock society')

    print('\nUser-1')
    user1.describe_user()
    user1.greet_user()

    print('\nUser-2')
    user2.describe_user()
    user2.greet_user()

    print('\nUser-3')
    user3.describe_user()
    user3.greet_user()

    #test number of served in restaurant class
    restaurant = Restaurant('Caffe Picaso', 'abcd')
    restaurant.describe_restaurant()
    print(restaurant.num_served)
    restaurant.set_number_served(300)
    restaurant.increment_number_served(50)
    restaurant.set_number_served(60)
    restaurant.increment_number_served(-5)


    #test login  attempts attribute
    user = User('faruk', 'ahmad', 'male', '03747474', 'faruk@gmail.com', 'katsushika')
    user.describe_user()
    user.increment_login_attempts()
    user.describe_user()
    user.reset_login_attempts()
    user.describe_user()