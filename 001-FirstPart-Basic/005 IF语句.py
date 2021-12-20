#coding=gbk
#
# 5.1 简单示例
#
'''
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
'''
#
# 5.2 条件测试 ： True or False
#   
# car = 'bmw'    =>赋值语句，可解读为“将变量car的值设置为“bmw””
# car == 'bmw'   =>比教语句，变量car的值为'bmw'吗？
# car.lower() == 'audi' => 这里car原来的值不会改变
#
# 5.2.3 检查是否不相等
#
'''
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':  # 有时候检测是否不等效率更高
    print("Hold the anchovies!")
'''
#
# 5.2.5 检测多个条件
#
# 1.使用and检测多个条件
# 2.使用or检测多个条件
#
# 5.2.6 检测特定值是否  包含 在列表中
#
'''
requested_toppings = ['mushrooms','onions','pineapple']
requested_topping = 'fish'
if requested_topping in requested_toppings:
    print(requested_topping + " in requested toppings!")
else:
    print(requested_topping + " not in requested toppings! ")
'''
#
# 5.2.6 检测特定值是否  不包含 在列表中
#
'''
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ",you can post a response if you wish")
'''
#
# 5.2.7 布尔表达式 => 条件测试 的别名，区别在于其结果 为 True Or False
#                   例如: game_active = True 或 can_edit = Flase
#
# 5.3 IF 语句结构 ： if / if-else / if-else-else
#
# 5.3.4 使用多个elif代码块: 更适用于知道最终要测试的条件；
#
'''
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
    
print("your admission cost is $" + str(price) + ".")
'''
#
# 5.4 使用if语句处理列表
#
# 5.4.2 确定列表不是空的
#
'''
requested_toppings = []

if requested_toppings:  ## 列表至少包含一个元素时返回true,为空时返回flase
    for requested_topping in requested_toppings:
        print("adding " + requested_topping)
    print("\nFinished makeing your pizza!")
else:
    print("Are you sure you want a plain pizza?")
'''
#
# 5.4.3 使用多个列表
#
available_toppings = ['mushrooms','olives','green peppers',
                        'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(" Adding " + requested_topping + ".")
    else:
        print(" Sorry, we don' t have " + requested_topping + ".")

print("\nFinished making your pizza!")
