#coding=gbk
#
# 第一种方式: 导入整个模块
#
'''
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# 第二种方式：导入指定模块中的指定函数
#
'''
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# 第三种方式：导入指定模块中的指定函数 并用 as 给函数取个 别名
#
'''
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# 第四种方式：导入指定模块中， 并用 as 给米块取个 别名
#
'''
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
#
# 第五种方式：导入模块中的所有函数
#
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
