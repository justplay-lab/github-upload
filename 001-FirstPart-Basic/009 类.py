#coding=gbk
#
# 9.1 ������ʹ����
#
# 9.1.1 ����Dog��  >>> ��ο� dog.py <<<
#
#       Python 2.7�д����� ��class ClassName(object):
#                                 --snip--
#                         ��class Dog(object)
#                                 --snip--
#
# 9.1.2 �����ഴ��ʵ������Python֪����δ�����ʾ�ض�С����ʵ��
#
'''
from dog import Dog

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy',3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
'''
#
# 9.2 ʹ�����ʵ��
#
# 9.2.1 ����Car��  >>> ��ο� car.py <<<
#
'''
from car import Car
'''
'''
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()
'''
#
# 9.2.3 �޸����Ե�ֵ : 1.ֱ��ͨ��ʵ�������޸�
#                    2.ͨ��������������
#                    3.ͨ���������е���
#
# 1.ֱ��ͨ��ʵ�������޸�
#
'''
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
'''
#
# 2.ͨ��������������
#
'''
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_new_car.update_odometer(14)
'''
#
# 3.ͨ�����������Ե�ֵ���е���
#
'''
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
'''
#
# 9.3 �̳� : �� ���� �̳� ���� ���е����Ժͷ���
#
# 9.3.1 ����ķ���__init__()
#

from car import Car, ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#
# 9.3.2 Python 2.7�еļ̳еĲ�ͬ�㣺1.super(������, self); 2.���常��ʱ������ָ��object
#
# 9.3.3 �����ඨ�����Ժͷ���
# 
'''
my_tesla.describe_battery()
'''
#
# 9.3.4 ��д����ķ���
#
my_tesla.fill_gas_tank()

#
# 9.3.5 ��ʵ���������� : ���Խ������� ��ֳ� ���Эͬ������С��
#
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#
# 9.3.6 ģ��ʵ����ҳ�Ч����ߵı�ʾ������Ҫ����һ����ʵ����
#
# 
# 9.4 ������ 
#
# 9.4.7 �Զ��幤������
#
#
# 9.5 Python��׼��
#
# 9.6 ������� : ����Ӧ���� �շ�������
#
#
