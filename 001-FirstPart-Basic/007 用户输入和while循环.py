#coding=gbk
#
# 7.1 函数input()的工作原理 : 让程序暂停，等待用户输入一些 > 文本 <。
#
# parrot
'''
message = input("Tell me sth, and i will repeat it back to you:")
print(message)
'''
#
# 7.1.1 编写清晰的程序
#
# greeter1
'''
name = input("Please enter your name: ")
print("Hello, " + name + "!")
'''
# greeter2
'''
prompt = 'If you tell us who you are, we can personalize the message you see.'
prompt += "\nWhat is your first name? "
name = input(prompt)

print("\nHello, " + name + '!')
'''
#
# 7.1.2 使用int()来获取>数值<输入
#
'''
age = input("How old are you?")
print(int(age) + 1)
'''
#
# 7.1.3 求模运算符：% 即将两个数相除并返回余数
#
# even or odd
'''
number = input("Enter a num, and I'll tell u if it's ever or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd")
'''
#
# 7.2 while 循环介绍 : 循环不断的运行，直到指定的条件不满足位置。
#
# counting
'''
cur_number = 1
while cur_number <=5:
    print(cur_number)
    cur_number += 1

print("after out of while,cur_number's value is : " + str(cur_number))
'''
#
# 7.2.2 让用户选择何时推出
#
# parrot
'''
prompt = "\nTell me sth, and i'll repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
'''
'''
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)
'''
#
# 7.2.3 使用标志 ： 定义一个变量，用于判断整个程序是否处于活动状态。
#  
'''               充当程序的交通信号灯。
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
'''
#
# 7.2.4 使用break退出循环 ： 立即退出，不再运行循环中余下的代码
#                         在任何Pthon循环中都可使用break语句。
# cities
'''
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
'''
#
# 7.2.5 在循环中使用continue：返回到循环开头，并根据条件测试结果决定是否继续执行循环
#
# counting
'''
cur_num = 0
while cur_num < 10:
    cur_num += 1
    if cur_num % 2 == 0:   # 即只打印奇数咯
        continue           # 忽略循环体余下的代码，返回到循环的开头
    
    print(cur_num)
'''
#
# 7.2.6 避免无限循环 ： 如果程序陷入无限循环，可按Ctrl + C，或关闭终端窗口；
# 
#
# 7.3 使用while循环来处理列表和字典
# 
# confrimed_users
'''
# 首先，创建一个待验证用户列表 和 一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止，将每个经过验证的列表都移动到已验证用户列表中
while unconfirmed_users:
    cur_user = unconfirmed_users.pop()
    
    print("Verifying users: " + cur_user.title())
    confirmed_users.append(cur_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''
#
# 7.3.2 删除包含特定值的所有列表元素
#
# pets
'''
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)
'''
#
# 7.3.3 使用用户输入来填充字典
#
# mountain_poll
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    
    # 将答卷存储在字典中
    responses[name] = response
    
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes or no)")
    if repeat == 'no':
        polling_active = False
        
# 调查结束，显示结果
print("\n--- Poll Result ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
