import json


def write_to_json(file_path):
    """ A method to write in json file """

    numbers = [1, 2, 3, 4, 5, 6, 7]

    with open(file_path, 'w') as wf:
        json.dump(numbers, wf)


def read_from_json(file_path):
    """ A method to read from json file """

    with open(file_path, 'r') as rf:
        data = json.load(rf)
    print(f'The file contains: {data}')



if __name__ == '__main__':
    print(f'Writing data to json file-')
    write_to_json('numbers.txt')

    print(f'Reading data from json file-')
    read_from_json('numbers.txt')


