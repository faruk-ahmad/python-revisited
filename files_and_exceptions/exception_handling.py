"""
This module shows how to handle common exceptions
"""

def divide(num1, num2):
    """ A method to divide a number by another number """

    try:
        #code that could raise eceptioin should go in the try block
        answer = num1 / num2
    except ZeroDivisionError:
        #code that will be executed if the mentioned exception occured
        print(f'You can not divide by zero.')
    else:
        #code that will excecuted if the try block is successful will go in the else block
        print(f'Ans: {num1} + {num2} = {answer}')


def read_text_files(file_path):
    """ A method to display the use of exception handling for file if the file is not accessible """

    try:
        with open(file_path, 'r') as rf:
            data = rf.read()
    except FileNotFoundError:
        print('The file does not exist. Please check the file path.')
    else:
        print(f'The file contains: {data}')


if __name__ == '__main__':
    n1 = 10
    n2 = 20
    divide(n1, n2)

    #check file not found error handling
    #file that exists
    file_path = './sample_input.txt'
    read_text_files(file_path)
    #file that does not exist
    file_path = './abcde.txt'
    read_text_files(file_path)