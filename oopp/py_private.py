"""
Python private variable and private methods

--> private variable: Variable names starting with double underscore e.g. __name is private and can only be accessed from the class

--> private method: Method names starting with double underscore e.g. __has_number() is private and can only be accessed inside the class
external access is not possible.
"""

class Person:
    def __init__(self, name, email):
        self.__name = name
        self.email = email

    
    def get_name(self):
        return self.__name

    
    def set_email(self, new_email):
        self.email = new_email

    
person = Person("faruk", "faruk.csebrur@gmail.com")

print(f"Name: {person.get_name()}")

# can not access directly, because __name is a private variable
print(f"Name direct acces: {person.__name}")
