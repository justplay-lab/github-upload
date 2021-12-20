#coding=gbk
#
# 10.1 从文件中读取数据 ： 可以一次读取文件全部内容 / 每次一行逐步读取
#
# 10.1.1 读取整个文件
#
# 10.1.2 文件路径 ： 
#        1.相对路径 with open('text_files\filename.txt') as file_object:
#        2.绝对路径 file_path = 'C:\...\filename.txt'
#                  with open(file_path) as file_object:
# 1.相对路径 —— 运行程序所在目录为相对
#
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
#
# 2.绝对路径
#
'''
file_path = 'D:\python.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
#
# 10.1.3 逐行读取
#
filename = 'pi_digits.txt'
'''
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
'''
#
# 10.1.4 创建一个包含文件各行内容的列表
#
'''
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
'''
#
# 10.1.5 使用文件的内容
#
'''
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
'''
#
# 10.1.6 包含一百万位的大型文件：代码一样，输出加限制即可
#
# 10.1.7 圆周率值中包含你的生日吗：加 if birthday in pi_string ... else ...即可
#
#
#
# 10.2 写入文件 ：保存数据的最简单方式
#
#
#
# 10.2.1 写入空文件
#
'''
filename = 'output.txt'
'''
'''
with open(filename, 'w') as file_object:
    file_object.write("I love Python")
'''
#
# 10.2.2 写入多行
#
'''
with open(filename, 'w') as file_object:
    file_object.write("I love Python\n")
    file_object.write("I love creating new games.\n")
'''
#
# 10.2.3 附加到文件
#
'''
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browers.\n")
'''
#
#
# 10.3 异常
#
#
# 10.3.1 处理ZeroDivisionError异常
#
#print(5 / 0)
#
# 10.3.2 使用try-except代码块
#
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
'''
#
# 10.3.3 使用异常避免崩溃
#
#
# 10.3.4 else代码块 : try代码成功执行后
#
'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    
    if not first_num.isdigit():
        print("Please enter digit: \n")
        continue        
    
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
        
    if not second_num.isdigit():
        print("Please enter digit from start.\n")
        continue  

    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("\nYou can't divide by 0!")
    else:
        print("\nThe answer is : " + str(answer))
'''
#
# 10.3.5 处理FileNotFoundError异常
#
'''
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
'''
#
# 10.3.6 分析文本
#
'''
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) +
            " words.")
'''            
#
# 10.3.7 使用多个文件 : 以上代码移到 >>>word_count.py<<<
#
'''
from word_count import count_words
'''
'''
filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt','moby.txt','siddhartha.txt']
for filename in filenames:
    count_words(filename)
'''
#
# 10.3.8 失败时一声不吭
#
#        Python有一个 pass 语句,可在代码块中使用它来让Python什么都不要做；
#
# 10.3.9 决定报告哪些错误
#
#
# 10.4 存储数据————一种简单的方式就是使用>>>模块json<<<来存储数据：
#                                     JS对象简谱，一种非Python专用的数据格式
#
# 10.4.1 使用json.dump()和json.load()
#

import json

#        函数json.dump()接受两个实参：1. 要存储的数据
#                                  2. 可用于存储数据的文件对象
'''
numbers = [2, 3, 5, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
'''
#
#        
#        json.load() 将这个列表读取到内存中, 一种在程序之间共享数据的简单方式
#
'''
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
'''
#
# 10.4.2 保存和读取用户生成的数据
#
#        保存
'''
username = input("What is your name?\t")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when your come back, " + username.title() + "!")
'''
#        读取
'''
filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username.title() + "!")
'''
#
#   10.4.3 重构 —— 将代码划分为一系列完成具体工作的 函数的过程；
#                 重构让代码更清晰、更易于理解、更容易 扩展。
#                  >>> remember_me.py <<<
#

from remember_me import *

# ~ get_new_username()
greet_user()
