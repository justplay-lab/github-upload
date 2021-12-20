#coding=gbk
#
# 10.1 ���ļ��ж�ȡ���� �� ����һ�ζ�ȡ�ļ�ȫ������ / ÿ��һ���𲽶�ȡ
#
# 10.1.1 ��ȡ�����ļ�
#
# 10.1.2 �ļ�·�� �� 
#        1.���·�� with open('text_files\filename.txt') as file_object:
#        2.����·�� file_path = 'C:\...\filename.txt'
#                  with open(file_path) as file_object:
# 1.���·�� ���� ���г�������Ŀ¼Ϊ���
#
'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
#
# 2.����·��
#
'''
file_path = 'D:\python.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''
#
# 10.1.3 ���ж�ȡ
#
filename = 'pi_digits.txt'
'''
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
'''
#
# 10.1.4 ����һ�������ļ��������ݵ��б�
#
'''
with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
'''
#
# 10.1.5 ʹ���ļ�������
#
'''
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
'''
#
# 10.1.6 ����һ����λ�Ĵ����ļ�������һ������������Ƽ���
#
# 10.1.7 Բ����ֵ�а�����������𣺼� if birthday in pi_string ... else ...����
#
#
#
# 10.2 д���ļ� ���������ݵ���򵥷�ʽ
#
#
#
# 10.2.1 д����ļ�
#
'''
filename = 'output.txt'
'''
'''
with open(filename, 'w') as file_object:
    file_object.write("I love Python")
'''
#
# 10.2.2 д�����
#
'''
with open(filename, 'w') as file_object:
    file_object.write("I love Python\n")
    file_object.write("I love creating new games.\n")
'''
#
# 10.2.3 ���ӵ��ļ�
#
'''
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browers.\n")
'''
#
#
# 10.3 �쳣
#
#
# 10.3.1 ����ZeroDivisionError�쳣
#
#print(5 / 0)
#
# 10.3.2 ʹ��try-except�����
#
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
'''
#
# 10.3.3 ʹ���쳣�������
#
#
# 10.3.4 else����� : try����ɹ�ִ�к�
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
# 10.3.5 ����FileNotFoundError�쳣
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
# 10.3.6 �����ı�
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
    # �����ļ����°������ٸ�����
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) +
            " words.")
'''            
#
# 10.3.7 ʹ�ö���ļ� : ���ϴ����Ƶ� >>>word_count.py<<<
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
# 10.3.8 ʧ��ʱһ������
#
#        Python��һ�� pass ���,���ڴ������ʹ��������Pythonʲô����Ҫ����
#
# 10.3.9 ����������Щ����
#
#
# 10.4 �洢���ݡ�������һ�ּ򵥵ķ�ʽ����ʹ��>>>ģ��json<<<���洢���ݣ�
#                                     JS������ף�һ�ַ�Pythonר�õ����ݸ�ʽ
#
# 10.4.1 ʹ��json.dump()��json.load()
#

import json

#        ����json.dump()��������ʵ�Σ�1. Ҫ�洢������
#                                  2. �����ڴ洢���ݵ��ļ�����
'''
numbers = [2, 3, 5, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
'''
#
#        
#        json.load() ������б��ȡ���ڴ���, һ���ڳ���֮�乲�����ݵļ򵥷�ʽ
#
'''
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
'''
#
# 10.4.2 ����Ͷ�ȡ�û����ɵ�����
#
#        ����
'''
username = input("What is your name?\t")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when your come back, " + username.title() + "!")
'''
#        ��ȡ
'''
filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username.title() + "!")
'''
#
#   10.4.3 �ع� ���� �����뻮��Ϊһϵ����ɾ��幤���� �����Ĺ��̣�
#                 �ع��ô������������������⡢������ ��չ��
#                  >>> remember_me.py <<<
#

from remember_me import *

# ~ get_new_username()
greet_user()
