#coding=gbk
#
### 4.1.1 Forѭ�� : for����ܻ��ֵ����ִ��print����������ѭ����
#
'''
magicians = ['alice','david','carolina']

for magician in magicians:   #��ȡ��һ��ֵalice��ֵ��magician
	print(magician.title())  #��ӡ���Ѿ���ֵ����magician
'''
#
# 4.1.2 Forѭ�� ����Ĳ���
#
'''
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see ur next trick, " + magician.title() + "\n")
'''
#
# 4.1.3 Forѭ�� ������ִ�е�һЩ����
#
'''
print("Thank you, everyone. That was a great magic show!")
print(magician)  #  Forѭ��������magician�������һ��Ԫ�ص�ֵ��
'''
#
### 4.3 ������ֵ�б�
#
# 4.3.1 ����range()
#
'''
for value in range(1,5): # ��ӡ����1~4,��ֵ�ﵽָ��ֵ5 ��ֹͣ
	print(value)
'''
#
# 4.3.2 ����range()���������б�;
#
'''
numbers = list(range(1,6)) # ʹ�ú���list()��range()�Ľ��ֱ��ת��Ϊ�б�
print(numbers)
'''
#
# 		����range()����ָ������
#
'''
even_numbers = list(range(2,11,2)) # ��ż��, ��2��ʼ�����ϼ�2��ֱ��>=11;
print(even_numbers)
'''
#
#		��1~10��ƽ���������ǰ�����һ���б���
#
'''
squares = []
for value in range(1,11):
	squares.append(value**2)
#	square = value**2
#	squares.append(square)
	
print(squares)
'''
#
# 4.3.3 �������б�ִ�м򵥵�ͳ�Ƽ���
#
'''
digits = [1,2,3,4,5,6,7,8,9,0]
min_value = min(digits)
max_value = max(digits)
sum_value = sum(digits)
print(digits)
print("min: " + str(min_value) + " max: " + str(max_value) + " sum: " + str(sum_value))
'''
#
# 4.3.4 �б����
#
'''
squares = [value**2 for value in range(1,11)]
print(squares)
'''
#
# Hands On
#
# 4-4 һ����
'''
digits = list(range(1,1000001))

for digit in digits:
	print(digit)
'''
# 4-5 ����1~1000000���ܺ�
'''
print(min(digits))
print(max(digits))
print(sum(digits))   # ����ӷ�̫����
'''
# 4-6 ����
'''
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
	print(odd_number)
'''
#
# 4.4 ��Ƭ : ���˶��ӳ�Ա�б�
#
players = ['charles','martina','maichael','florence','eli']
'''
print(players[0:3])  #���˵��ĸ�ֵ�󣬲���ʾ����������
print(players[:4])   #��ָ����һ������������ͷ��ʼ��
print(players[2:])   #��ָ���ڶ�����������ֱ�����
print(players[-2:])  #���︺������Ҳ���ã����Ｔ�����ڶ�����ʼ�����
'''
#
# 4.4.2 ������Ƭ
#
'''
print("Here are the first three players on my team:")
for player in players[:3]:   
	print(player)
'''
#
# 4.4.3 �����б�
#
'''
my_foods = ['pizza','falafel','carrot cake']
'''
#
# ������������ʡ�ԣ�����ͷ��β���������б���my_foods�ĸ����洢����friend_foods
# ע�⣺�˺��������б���������ȫ�������б��ˣ�
#
'''
friend_foods = my_foods[:] 
print("my favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
'''
#
# �﷨ע�⣺ friend_foods = my_foods  
# =>����python���±���friend_foods������������my_foods���б�����ָ��ͬһ���б�
#
#
# 4.5 Ԫ�� : Python�������޸ĵ�ֵ��Ϊ���ɱ�ģ����б��Ϊ Ԫ��
#           �б����[],��Ԫ�����Ϊ()
#
# 
# 4.5.1 ����Ԫ��
#
dimensions = (200,50)
print(dimensions[0])     # ʹ�õ��﷨������б��﷨��ͬ
print(dimensions[1])
# dimensions[0] = 300   =>�� ���ܸ�Ԫ�鸳ֵ����
#
# 4.6 ���ô����ʽ
#
