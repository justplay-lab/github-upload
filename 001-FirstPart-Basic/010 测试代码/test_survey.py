#coding=gbk
#
# ver11.2.3
#
import unittest
from survey import AnonymouseSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """���AnonymousSurvey��Ĳ���"""
    def test_store_single_reponse(self):
        """���Ե����𰸻ᱻ���Ƶش洢"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymouseSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)

unittest.main()
