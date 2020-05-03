""" A module to test the person.py module """

import unittest
from person import get_formatted_name

class TestPersonModule(unittest.TestCase):
    """ A class to test person module """

    def setUp(self):
        """ A method to run code that require before each test """
        pass

    def tearDown(self):
        """  A method to run code that require after each test """
        pass


    def test_formatted_name(self):
        """ A method to test formatted name given first name and last name """

        self.assertEqual(get_formatted_name('faruk', 'ahmad'), 'Faruk Ahmad', 'Could not handle formatting.')
