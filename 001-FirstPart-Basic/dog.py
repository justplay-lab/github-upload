#coding=gbk
#
class Dog():
    """һ��ģ���С���ļ򵥳���"""
    
    def __init__(self, name, age):  # ÿ�δ���ʵ��ʱ,Python�����Զ�������
        """��ʼ������name��age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """ģ��С��������ʱ����"""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """ģ��С��������ʱ���"""
        print(self.name.title() + " rolled over!")
