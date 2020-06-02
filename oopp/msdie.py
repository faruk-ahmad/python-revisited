import random


class MSDie:
    """
    A class to represent multi side die

    Instance variables:
        current_value
        num_of_sides
    """

    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.current_value = self.roll()


    def roll(self):
        self.current_value = random.randrange(1, self.num_of_sides + 1)
        return self.current_value


    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return f"MSDie({self.num_of_sides}): {self.current_value}"


if __name__ == '__main__':
    die = MSDie(6)

    for i in range(5):
        print(f"Current value: {die.current_value}")
        die.roll()

    
    d_list = [MSDie(6), MSDie(4)]

    print(d_list)

