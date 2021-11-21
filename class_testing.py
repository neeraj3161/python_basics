import unittest
from survey_class import AnonymousSurvey

# inheriting the unit test class
class Testing_survey(unittest.TestCase):
    # def test_testingSurvey(self):
    #     question = 'What language did you first learn to speak??'
    #     my_survey=AnonymousSurvey(question)
    #     my_survey.store_response('English')
    #     # here we are testing if the survey includes the response English
    #     self.assertIn('English',my_survey.response)
    def test_three_response(self):
        question='What language do you know'
        my_survey_check=AnonymousSurvey(question)
        # we can also use for statement to store multiple responses
        response_taken='English',"Hindi",'Marathi'
        my_survey_check.store_response(response_taken)
        self.assertIn(response_taken,my_survey_check.response)
if __name__=='__main__':
    unittest.main()



