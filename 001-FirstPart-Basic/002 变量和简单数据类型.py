#coding=gbk
# 向大家问好 2020/3/28 22:12
print("Hello Python people")
#
# 字符串的格式
#
name = "ada lovelace"
print(name.title())#字符串首字母大写，其余小写
print(name.upper())#字符串全大写
print(name.lower())#字符串全小写
#
# 字符串的合并
#
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
message = "Hello, " + full_name.title() + "!"
print(message)
# 2-5
name = "Albert Einstein"
message = name + ' once said, "A person who never made a mistake never tried anything new."'
print(message)
#
# 字符串中的特殊字符
#
print("Python")
print("\tPython") 
# "\t" = 一段空白相当于tab键 ; "\n" = 换行(enter)，以下为输出实例
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#
# 字符串的赋值
#2-6
famous_person = name
message = famous_person
print(message)
#
# 字符串 删除空白
#2-7
name = '  li lei  '
print(name)
print('\t' + name)
print('\n' + name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#
#  整数的运算
#2-8
print(5 + 3)
print(11 - 3)
print(2 * 4)
print(16 / 2)
