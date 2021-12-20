#coding=gbk
#
# ѧϰʹ��Pythonģ��unittest�еĹ��������Դ���
#    1. ѧϰ��д������������֤���뽫�õ�Ԥ�ڵ������
#    2. ����ͨ������Ǹ�ʲô����
#    3. ��θĽ�����
#    4. ѧϰ��β��Ժ�������
#    5. ��Ϊ��Ŀ��д���ٸ�����
#
# 11.1 ���Ժ���
#      ���԰���������ο� >>>name_function.py<<<
#                      >>>names.py<<<
#                      >>>test_name_function.py<<< ��Ҫ���붼�ڱ��ĵ�����
#      ����汾 ver 11.1
#
# 11.1.1 ��Ԫ���ԺͲ����������������˽�
#        1.��Ԫ���� ���ں�ʵ����ĳ������û�����⣻
#        2.�������� ��һ�� ��Ԫ����,��Щ��Ԫ����һ���ʵ�����ڸ��������µ���Ϊ������Ҫ��.
#          ���õ� �������� ���ǵ��˺��������յ��ĸ�������,�������������Щ���εĲ��ԡ�
#
# 11.1.2 ��ͨ���Ĳ��� �����������һ�еľ�������һ������ͨ���ˣ��������ۿɶ�
#

import unittest
from name_function import get_formatted_name

'''
class NamesTestCase(unittest.TestCase):   # ������ �� �̳и���
    """����name_function.py"""
    
    def test_first_last_name(self):
        """����ȷ�ش�����Janis Joplin������������"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
'''
#
# 11.1.3 ����ͨ���ز��� code ver11.1.3 
#
#
# 11.1.4 ����δͨ��ʱ��ô�� code ver11.1.4
#
#
# 11.1.5 ����²���
#
'''
class NamesTestCase(unittest.TestCase):   # ������ �� �̳и���
    """����name_function.py"""
    
    def test_first_last_name(self):
        """����ȷ�ش�����Janis Joplin������������"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """�ܹ���ȷ�Ĵ�����Wolfgang Amadeus Mozart������������"""
        formatted_name = get_formatted_name(
            'wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
  
unittest.main()
'''
#
#
# 11.2 ������
#
# 11.2.1 ���ֶ��Է���
#        unittest Module�еĶ��Է���
#
#               ����                  ��;
#         assertEqual(a, b)       ��ʵ a == b 
#         assertNotEqual(a, b)    ��ʵ a != b 
#         assertTrue(x)           ��ʵ x Ϊ True 
#         assertFalse(x)          ��ʵ x Ϊ False 
#         assertIn(item, list)    ��ʵ item �� list �� 
#         assertNotIn(item, list) ��ʵ item ���� list ��
#
#
# 11.2.2 һ��Ҫ���Ե���
#        ���԰���������ο� >>>survey.py<<<
#                        >>>language_survey.py<<<
# 
#
# 11.2.3 ����AnonymousSurvey�� >>>test_survey.py<<<
#
'''
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
        
    def test_store_three_responses(self):
        """�������������ᱻ���Ƶش洢"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymouseSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
'''
#
# 11.2.4 ����setup()
#
import unittest
from survey import AnonymouseSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """���AnonymousSurvey��Ĳ���"""
    
    def setUp(self):
        """
        ����һ����������һ��𰸣���ʹ�õĲ��Է���ʹ��
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymouseSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    
    def test_store_single_reponse(self):
        """���Ե����𰸻ᱻ���Ƶش洢"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)
        
    def test_store_three_responses(self):
        """�������������ᱻ���Ƶش洢"""
        for response in self.responses:
            self.my_survey.store_response(response)        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
