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





if __name__ == '__main__':
    frac = Fraction(10, 5)
    print(frac)