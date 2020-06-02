"""
A class to represent a fraction
"""

class Fraction:
    def __init__(self, num, den):
        """
        initializing numerator and denominator for the fraction
        """
        self.num = num
        self.den = den


    def __str__(self):
        """
        override the __str__ method to print the object in a neaty way
        """
        return f"{self.num}/{self.den}"


    def __add__(self, otherfraction):
        """
        A method to implement addition of fraction object.
        by default, you can not add two fractions by +
        """
        new_den = self.den * otherfraction.den
        new_num = self.den * otherfraction.num + otherfraction.den * self.num

        #return f"{new_num}/{new_den}"

        # lets create a new object of Fraction class with the new num and den, so that 
        # the fraction will be represented by the __str__() method and we can simply print it
        return Fraction(new_num, new_den)


    def __eq__(self, otherfraction):
        """
        A overridden method to compare two fraction object if they are equal
        """
        first_ = self.num * otherfraction.den
        second_ = self.den * otherfraction.num

        return first_ == second_



if __name__ == '__main__':
    frac = Fraction(10, 5)
    print(frac)

    frac1 = Fraction(1, 3)
    frac2 = Fraction(2, 6)

    sum = frac1 + frac2
    print(sum)

    print(frac1 == frac2)
