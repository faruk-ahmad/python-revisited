""" A test module to test the survey module """

import unittest
from survey import AnnonymousSurvey


class TestAnnynymousSurvey(unittest.TestCase):
    """ A class to test AnnonymousSurvery class """

    def setUp(self):
        """ Code that runs before each test """
        pass

    def tearDown(self):
        """ Code that runs after each test """
        pass

    def test_single_response_stored(self):
        """ A method to test when a single response is stored """
        question = "What is your favorite language?"
        survey = AnnonymousSurvey(question)
        survey.store_responses("English")

        self.assertIn("English", survey.responses, "Single response not stored successfully")


    def test_three_responses_stored(self):
        """ A method to test when three responses are stored """
        question = "What is your favorite language?"
        responses = ["Bangla", "English", "Japanese"]

        survey = AnnonymousSurvey(question)
        for response in responses:
            survey.store_responses(response)

        for response in responses:
            self.assertIn(response, survey.responses, "Three responses are not stored successfully.")