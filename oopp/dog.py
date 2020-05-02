class Dog():
    ''' A simple class that represent a Dog'''
    def __init__(self, name, age):
        ''' init method to initialize default values to the instance'''
        self.name = name
        self.age = age

    def sit(self):
        ''' method to describe the sit behavior '''
        print(f'{self.name.title()} is sitting now.')

    def rolling_over(self):
        ''' metod to describe the roll over behavior '''
        print(f'{self.name.title()} is rolled over now.')




if __name__ == '__main__':
    print('My dog:')
    my_dog = Dog('kitty', 2)
    my_dog.sit()
    my_dog.rolling_over()

    print('Your dog:')
    your_dog = Dog('willie', 3)
    your_dog.sit()
    your_dog.rolling_over()