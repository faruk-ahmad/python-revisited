"""
1. __str__ method: To print the content of the object is currently holding
2. __repr__ method: For debuging purpose, if this method is overridded, then it will print helpful message
"""

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # we can write a get summary method to print the current content of an object
    def get_summary(self):
        return f"Name: {self.name}\nEmail: {self.email}"

    # alternatively we can override the __str__ method to print the object with its contents
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}"



person = Person("faruk", "faruk.csebrur@gmail.com")

# option 1 to get summary
print(person.get_summary())

# option 2 to get summary, now we can only print the object
print(person)