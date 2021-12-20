#coding=gbk
#
# 学习使用Python模块unittest中的工具来测试代码
#    1. 学习编写测试用例，验证输入将得到预期的输出；
#    2. 测试通过与否是个什么样子
#    3. 如何改进代码
#    4. 学习如何测试函数和类
#    5. 该为项目编写多少个测试
#
# 11.1 测试函数
#      测试案例程序请参考 >>>name_function.py<<<
#                      >>>names.py<<<
#                      >>>test_name_function.py<<< 主要代码都在本文档如下
#      代码版本 ver 11.1
#
# 11.1.1 单元测试和测试用例——概念了解
#        1.单元测试 用于核实函数某个方面没有问题；
#        2.测试用例 是一组 单元测试,这些单元测试一起核实函数在各种情形下的行为都符合要求.
#          良好的 测试用例 考虑到了函数可能收到的各种输入,包含针对所有这些情形的测试。
#
# 11.1.2 可通过的测试 ：结果——第一行的句点表明有一个测试通过了，其余明眼可懂
#

import unittest
from name_function import get_formatted_name

'''
class NamesTestCase(unittest.TestCase):   # 创建类 与 继承父类
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能正确地处理像Janis Joplin这样地姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
'''
#
# 11.1.3 不能通过地测试 code ver11.1.3 
#
#
# 11.1.4 测试未通过时怎么办 code ver11.1.4
#
#
# 11.1.5 添加新测试
#
'''
class NamesTestCase(unittest.TestCase):   # 创建类 与 继承父类
    """测试name_function.py"""
    
    def test_first_last_name(self):
        """能正确地处理像Janis Joplin这样地姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确的处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
  
unittest.main()
'''
#
#
# 11.2 测试类
#
# 11.2.1 各种断言方法
#        unittest Module中的断言方法
#
#               方法                  用途
#         assertEqual(a, b)       核实 a == b 
#         assertNotEqual(a, b)    核实 a != b 
#         assertTrue(x)           核实 x 为 True 
#         assertFalse(x)          核实 x 为 False 
#         assertIn(item, list)    核实 item 在 list 中 
#         assertNotIn(item, list) 核实 item 不在 list 中
#
#
# 11.2.2 一个要测试的类
#        测试案例程序请参考 >>>survey.py<<<
#                        >>>language_survey.py<<<
# 
#
# 11.2.3 测试AnonymousSurvey类 >>>test_survey.py<<<
#
'''
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
        
    def test_store_three_responses(self):
        """测试三个档案会被妥善地存储"""
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
# 11.2.4 方法setup()
#
import unittest
from survey import AnonymouseSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymouseSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    
    def test_store_single_reponse(self):
        """测试单个答案会被妥善地存储"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English', self.my_survey.responses)
        
    def test_store_three_responses(self):
        """测试三个档案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
