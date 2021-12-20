#coding=gbk
#
# 9.1 创建和使用类
#
# 9.1.1 创建Dog类  >>> 请参考 dog.py <<<
#
#       Python 2.7中创建类 ：class ClassName(object):
#                                 --snip--
#                         故class Dog(object)
#                                 --snip--
#
# 9.1.2 根据类创建实例：让Python知道如何创建表示特定小狗的实例
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
# 9.2 使用类和实例
#
# 9.2.1 创建Car类  >>> 请参考 car.py <<<
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
# 9.2.3 修改属性的值 : 1.直接通过实例进行修改
#                    2.通过方法进行设置
#                    3.通过方法进行递增
#
# 1.直接通过实例进行修改
#
'''
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
'''
#
# 2.通过方法进行设置
#
'''
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_new_car.update_odometer(14)
'''
#
# 3.通过方法对属性的值进行递增
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
# 9.3 继承 : 即 子类 继承 父类 所有的属性和方法
#
# 9.3.1 子类的方法__init__()
#

from car import Car, ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#
# 9.3.2 Python 2.7中的继承的不同点：1.super(子类名, self); 2.定义父类时括号内指定object
#
# 9.3.3 给子类定义属性和方法
# 
'''
my_tesla.describe_battery()
'''
#
# 9.3.4 重写父类的方法
#
my_tesla.fill_gas_tank()

#
# 9.3.5 将实例用作属性 : 可以将大型类 拆分成 多个协同工作的小类
#
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#
# 9.3.6 模拟实物——找出效率最高的表示法，需要经过一定的实践。
#
# 
# 9.4 导入类 
#
# 9.4.7 自定义工作流程
#
#
# 9.5 Python标准库
#
# 9.6 类编码风格 : 类名应采用 驼峰命名法
#
#
