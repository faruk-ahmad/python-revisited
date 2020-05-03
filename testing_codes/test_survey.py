""" A test module to test the survey module """

import unittest
from survey import AnnonymousSurvey


class TestAnnynymousSurvey(unittest.TestCase):
    """ A class to test AnnonymousSurvery class """

    def setUp(self):
        """ Code that runs before each test """
        self.question = "What is your favorite language?"
        self.my_survey = AnnonymousSurvey(self.question)
        self.responses = ["Bangla", "English", "Japanese"]


    def tearDown(self):
        """ Code that runs after each test """
        pass

    def test_single_response_stored(self):
        """ A method to test when a single response is stored """
        self.my_survey.store_responses(self.responses[0])

        self.assertIn(self.responses[0], self.my_survey.responses, "Single response not stored successfully")


    def test_three_responses_stored(self):
        """ A method to test when three responses are stored """
        for response in self.responses:
            self.my_survey.store_responses(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses, "Three responses are not stored successfully.")