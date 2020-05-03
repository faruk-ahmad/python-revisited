"""
This module shows how to handle common exceptions
"""

def divide(num1, num2):
    """ A method to divide a number by another number """

    try:
        answer = num1 / num2
    except ZeroDivisionError:
        print(f'You can not divide by zero.')
    else:
        print(f'Ans: {num1} + {num2} = {answer}')



if __name__ == '__main__':
    n1 = 10
    n2 = 20
    divide(n1, n2)