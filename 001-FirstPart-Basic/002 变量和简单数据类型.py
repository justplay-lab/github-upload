#coding=gbk
# �����ʺ� 2020/3/28 22:12
print("Hello Python people")
#
# �ַ����ĸ�ʽ
#
name = "ada lovelace"
print(name.title())#�ַ�������ĸ��д������Сд
print(name.upper())#�ַ���ȫ��д
print(name.lower())#�ַ���ȫСд
#
# �ַ����ĺϲ�
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
# �ַ����е������ַ�
#
print("Python")
print("\tPython") 
# "\t" = һ�οհ��൱��tab�� ; "\n" = ����(enter)������Ϊ���ʵ��
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
#
# �ַ����ĸ�ֵ
#2-6
famous_person = name
message = famous_person
print(message)
#
# �ַ��� ɾ���հ�
#2-7
name = '  li lei  '
print(name)
print('\t' + name)
print('\n' + name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
#
#  ����������
#2-8
print(5 + 3)
print(11 - 3)
print(2 * 4)
print(16 / 2)
