class Restaurant():
    ''' A simple class representing a restaurant '''
    def __init__(self, restaurant_name, cuisine_type):
        ''' init method to initialize attributes '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        ''' a method to describe the restaurant '''
        print(f'Restaurante name: {self.restaurant_name}\nCuisine type: {self.cuisine_type}')


    def open_restaurant(self):
        ''' a method to show restaurant open or close status '''
        print(f'{self.restaurant_name} is open now.')




if __name__ == '__main__':
    restaurant = Restaurant('Cusine Factory', 'Sour Cusine')
    print(f'Restaurant name: {restaurant.restaurant_name}\nCuisine type: {restaurant.cuisine_type}')

    restaurant.describe_restaurant()
    restaurant.open_restaurant()