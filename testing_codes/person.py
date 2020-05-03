""" A module that represent functions describing a person """

def get_formatted_name(first_name, last_name):
    """ A method to return formatted name from first name and last name """

    full_formatted_name = f'{first_name.title()} {last_name.title()}'
    return full_formatted_name


if __name__ == '__main__':
    first_name = 'faruk'
    last_name = 'ahmad'
    print(get_formatted_name(first_name, last_name))