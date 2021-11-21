import unittest
from survey_class import AnonymousSurvey



# The unittest.TestCase
# class has a setUp() method that allows you to create these objects once and
# then use them in each of your test methods
class Anonymous_Survey(unittest.TestCase):
    def setUp(self):
        question='What languages you know??'
        self.my_survey=AnonymousSurvey(question)
        self.response=['English','Hindi','Marathi']
    def test_response_stored(self):
        self.my_survey.store_response(self.response[0])
        self.assertIn('English',self.my_survey.response)

    def test_three_stored_survey(self):
        for response in self.response:
            self.my_survey.store_response(response)
        # for response in self.response:
        #     self.assertIn(response, self.my_survey.response)
            print(response)
        # if you dont want to repeat use loop for loop
        # self.assertIn('English',self.my_survey.response)
        # self.assertIn('Hindi',self.my_survey.response)
        # self.assertIn('Marathi', self.my_survey.response)
        for response in self.response:
            self.assertIn(response,self.my_survey.response)
