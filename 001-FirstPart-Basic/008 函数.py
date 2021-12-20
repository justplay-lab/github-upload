#coding=gbk
#
# 函数————带名字的代码块，用于完成具体的工作
#
# 8.1 定义函数
#
# greeter
'''
def greet_user():
    """显示简单的问候语"""  # 文档字符串的注释，用于生成有关程序中函数的文档
    print("Hello!")

greet_user()
'''
#
# 8.1.1 像函数传递信息
#
'''
def greet_user(username):   # 形参
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")

greet_user('jessie')        # 实参
'''
#
# 8.1.2 实参和形参 : 如上
#
#
# 8.2 传递实参
#
# 8.2.1 位置实参 ： 实参和形参 顺序要相同
#
# pets
'''
def des_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")

des_pet('hamster', 'harry')
des_pet('dog','willie')
'''
#
# 8.2.2 关键字实参————传递给函数的 名称-值 对。测试顺序则无关紧要了
#
'''
def des_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")
# 调用时，我们向Python明确地指出了各个实参对应的形参。
des_pet(animal_type = 'hamster', pet_name = 'harry') 
'''
#
# 8.2.3 默认值————给每个形参指定 默认值
#
'''
def des_pet(pet_name, animal_type = 'dog'):  # Python视为位置实参
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ",")

des_pet(pet_name = 'willie')
des_pet('fly')
des_pet(animal_type = 'hamster', pet_name = 'harry')
'''
#
# 8.2.4 等效的函数调用 ：  如上
#
# 8.2.5 避免实参错误：位置 和 数量 的匹配
#
# 8.3 返回值 ： 可使用return语句
#
# 8.3.1 返回简单值
#
# formatted_name
'''
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
'''
#
# 8.3.2 让实参变成可选的
#
'''
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回 整洁 的 姓名"""
    if middle_name:         # 有值即为True
        full_name = first_name + ' ' + middle_name + ' ' + last_name 
    else:
        full_name = first_name + ' ' + last_name 
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print( musician)
'''
#
# 8.3.3 返回字典
#
# person
'''
def build_person(first_name, last_name, age=""):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name} #接受值并封装进字典返回
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix',age = 27)
print(musician)
'''
#
# 8.3.4 结合使用函数和while循环
#
'''
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break 
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
        
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
'''
#
# 8.4 传递列表————使用函数来提高处理列表的效率
#
# greet_users
'''
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)
'''
#
# 8.4.1 在函数中修改列表—————永久性的修改
#
# printing_models ——一个函数
'''
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
'''
'''
# 模拟打印每个设计，直到都打印了，之后，移到列表completed_models中
while unprinted_designs:
    cur_design = unprinted_designs.pop()
    
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + cur_design)
    completed_models.append(cur_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
'''
# printing_models —— 两个函数
'''
def print_models(unprinted_designs, completed_models):
    """ 
    模拟打印每个 设计,直到 没有 未打印的设计为止
    打印每个 设计后,都将其移到列表 completed_ models 中 
    """ 
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # 模拟根据设计制作 3D 打印模型的过程 
        print("Printing model: " + current_design) 
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
'''    
'''    
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
'''
#
# 8.4.2 禁止函数修改列表————即最原始的列表做 >备案<
#                        传递列表的 >副本< 而不是原件 
#
# function_name(list_name(:))   # 切片表示法[:]创建列表的副本
'''
print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
'''
#
# 8.5 传递任意数量的实参
#
'''
def make_pizza(*toppings):   # 创建一个名为toppings的空元组
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the follwing toppings:")
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
'''
#
# 8.5.1 结合使用位置实参和任意数量实参
#
'''
def make_pizza(size, *toppings):   # 创建一个名为toppings的>>空元组<<
    """概述要制作的披萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the follwing toppings:")
    for topping in toppings:
        print(topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers','extra cheese')
'''
#
# 8.5.2 使用任意数量的关键字实参 ： 因为你不可预知会传给函数些什么信息
#
# user_profile
'''
def build_profile(first, last, **user_info): # 创建一个名为user_info>>空字典<<
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert','einstein',
                            location='princeton',
                            field='physics')
print(user_profile)
'''
#
# 8.6 将函数存储在模块中：import语句允许使用导入模块中的代码 
#     
#      >>>>>> 以下实例代码请查看 pizza.py / making_pizzas.py <<<<<<
#
# 8.6.1 导入整个模块 ： 1.pizza.py ; 2. making_pizzas.py 中 import pizza
#                    3.通过pizza.make_pizza(size,*toppings) 格式调用
#
#       通用调用语法：module_name.function_name()
#
#
# 8.6.2 导入特定的函数 ：1. from module_name import function_name
#                     1. from module_name import function_0, function_1,...
#
#
# 8.6.3 使用as给函数指定别名：from module_ name import function_ name as fn
#
# 8.6.4 使用as给模块指定别名：import module_name as mn
#
# 8.6.5 导入模块中的所有函数：from module_name import *
#
#
# 8.7 函数编写指南：
#     1.给形参指定默认值时，等号两边不要有空格
#       def function_ name( parameter_ 0, parameter_ 1=' default value')
#     2.对于函数调用中的关键字实参，也应遵循这种约定：
#       function_name(value_0, parameter_1='value')
#     3.参数过多的格式
#
#       def function_name(
#               parameter_0, parameter_1, parameter_ 2,
#               parameter_3, parameter_4, parameter_5):
#           function body...
#
