#coding=gbk
#
# ��һ�ַ�ʽ: ��������ģ��
#
'''
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# �ڶ��ַ�ʽ������ָ��ģ���е�ָ������
#
'''
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# �����ַ�ʽ������ָ��ģ���е�ָ������ ���� as ������ȡ�� ����
#
'''
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# �����ַ�ʽ������ָ��ģ���У� ���� as ���׿�ȡ�� ����
#
'''
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# �����ַ�ʽ������ģ���е����к���
#
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
