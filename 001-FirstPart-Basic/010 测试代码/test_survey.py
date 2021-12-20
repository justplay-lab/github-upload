#coding=gbk
#
# ver11.2.3
#
import unittest
from survey import AnonymouseSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def test_store_single_reponse(self):
        """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymouseSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)

unittest.main()
